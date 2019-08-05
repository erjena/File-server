# Python File Server

A simple file server operates via REST API. Supports list, upload and delete operations.

## Installation

Step 1: Clone the repo
```
$ git clone https://github.com/erjena/py-file-server.git
```

Step 2: Install dependencies
```
$ cd py-file-server
$ pip install flask
$ python3 -m venv venv
$ virtualenv venv
$ source venv/bin/activate
```
Step 3: To start server:
```
$ python3 <full_path_to_directory_to_serve_files>
```

## Testing
Get list of files
```
$ curl -X GET http://localhost:5000/list
```
Upload file
```
$ curl -X POST \
    http://localhost:5000/upload \
    -H 'Content-Type: application/json' \
    -H 'content-type: multipart/form-data' \
    -F filename=@<full_path_to_file>
```
Delete file 
```
$ curl -X DELETE \
    http://localhost:5000/delete \
    -H 'Content-Type: application/json' \
    -d '{ "filename": "<file_name>" }'
```

## Future Improvements
* Support download
* React client
* Support recursive directories
