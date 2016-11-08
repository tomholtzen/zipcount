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

  curl -X POST http://localhost:8080/api/v1/zipcount -F "filename=@/Users/myname/Documents/solidfire/sampletext_all.zip"
