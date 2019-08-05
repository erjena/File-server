import os
import sys
from flask import Flask, abort, request
from os import listdir
from os.path import isfile, join
from werkzeug.utils import secure_filename

app = Flask(__name__)
work_dir = sys.argv[1]
app.config['UPLOAD_FOLDER'] = work_dir
allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@app.route('/list', methods=['GET'])
def get_list():
  onlyfiles = [f for f in listdir(work_dir) if isfile(join(work_dir, f))]
  return str(onlyfiles)

@app.route('/upload', methods=['POST'])
def upload_file():
  if 'filename' not in request.files:
    print ('No file part')
    abort(400)
  file = request.files['filename']
  if file.filename == '':
    print ('No selected file')
    abort(400)
  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(join(app.config['UPLOAD_FOLDER'], filename))
    return "File added"
  abort(500)

@app.route('/delete', methods=['DELETE'])
def delete_file():
  if 'filename' not in request.json:
    print('Filename not provided')
    abort(400)
  filename = work_dir + request.json['filename']
  os.remove(filename)
  return "File deleted"

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in allowed_extensions

def main():
  if len(sys.argv) != 2:
    print ("Please enter correct directory name.")
    return
  if os.path.isdir(work_dir) == False:
    print ("Such directory does not exist.")
    return
  app.run(debug=True)

main()
