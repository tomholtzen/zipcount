# zipcount
CherryPy REST API for uploading a zip file and returning the top 10 word count

* **URL**

  /localhost:8080/api/zipcount

* **Method:**

  POST - Uploads the zip file, and returns top 10 word count

*  **URL Params**
  
  None

* **Data Params**

  "filename=@/Users/myname/Documents/sampletext_all.zip"

* **Success Response:**

  JSON returns with top 10 words with counts

  Code: 200
  
  POST Resposne: {"results": [{"count": 56, "word": "and"}, {"count": 56, "word": "in"}, {"count": 56, "word": "of"}, 
  {"count": 60, "word": "should"}, {"count": 60, "word": "we"}, {"count": 64, "word": "principle"}, {"count": 68, "word": "classes"}, 
  {"count": 84, "word": "a"}, {"count": 128, "word": "to"}, {"count": 156, "word": "the"}]}

* **Error Response:**
  
  Code: 400, Bad Request: Invalid zip file

* **Sample Call:**

  curl -X POST http://localhost:8080/api/v1/zipcount -F "filename=@/Users/myname/Documents/sampletext_all.zip"

**Docker Configuration**
----

*  **Image Creation from Dockerfile**

  docker build -t restapp/zipcount .

  Execute the following command from the same directory as the Dockerfile to create image called restapp/zipcount

*  **Run the docker image**

  docker run -d -p 32768:8080 restapp/zipcount

  This command starts the container and maps port 32769 on host to port 8080 in the container.

*  **Execute REST API on container**

  My local test scenario was to deploy docker on my mac. In this case, after the container was running, I needed to find the IP address of the container in order send the commands via curl. The docker-machine ls command returns the IP address.

  docker-machine ls
  
  default     *         virtualbox    Running     tcp://192.168.99.100:2376               v1.12.2   

*  **Example REST API's**

  curl -X POST http://192.168.99.100:32768/api/v1/zipcount -F "filename=@/Users/myname/Documents/sampletext_all.zip"
