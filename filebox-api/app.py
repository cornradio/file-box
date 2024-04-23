import os
from flask import Flask,request
from flask_cors import CORS
from werkzeug.utils import secure_filename
# flask run -p3000 --debug
app = Flask(__name__)
CORS(app)

@app.route("/<boxname>/filelist")
def get_filelist(boxname):
    return {
        "files": [
            "./box1/file1.txt",
            "./box1/file2.txt",
            "./box1/file3.txt"
        ]
    }

@app.route("/<boxname>/upload", methods=['POST','GET'])
def uploadfile(boxname):
        #if not exist boxname create box floder:
        if not os.path.exists('./'+boxname): 
            os.makedirs('./'+boxname)

        if request.method == 'POST':
            f = request.files['the_file']
            f.save('./'+boxname+'/'+secure_filename(f.filename))
            return{
                 "info": "uploaded "+ secure_filename(f.filename)
            }
        else:
            return {
                "info": "use post method with file "
            }