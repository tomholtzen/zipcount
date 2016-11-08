import cherrypy
import collections
import Queue
import threading
import re
import zipfile


num_worker_threads = 3


class zipcount(object):
    exposed = True

    def __init__(self):
        self.q = Queue.Queue()
        self.threads = []
        self.wordcount = collections.Counter()
        cherrypy.engine.subscribe('stop', self.shutdown)
        for i in range(num_worker_threads):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
            self.threads.append(t)

    def shutdown(self):
        print("Stopping %s" % str(self))
        for i in range(num_worker_threads):
            self.q.put(None)
        for t in self.threads:
            t.join()

    def worker(self):
        while True:
            item = self.q.get()
            if item is None:
                print "Exiting worker"
                break
            self.count_words(item)
            self.q.task_done()

    def count_words(self, data):
        try:
            for word in filter(None, re.split("\W+", data)):
                self.wordcount[word.lower()] += 1
        except Exception as e:
            print(e)

    def format_response(self):
        results = []
        for wc in sorted(self.wordcount.most_common(10), key = lambda x: (x[1], x[0])):
            results.append({'word': wc[0], 'count': wc[1]})
        items = {"results": results}
        return items

    @cherrypy.tools.json_out()
    def POST(self, filename):
        # validate zip file
        if not zipfile.is_zipfile(filename.file):
            raise cherrypy.HTTPError(400, 'Bad Request: Invalid zip file')

        self.wordcount.clear()
        with zipfile.ZipFile(filename.file, "r") as zfile:
            for name in zfile.namelist():
                data = zfile.open(name).read()
                self.q.put(data)

        self.q.join()
        return self.format_response()


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(zipcount(), '/api/v1/zipcount', conf)


