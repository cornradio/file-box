import os
from flask import Flask,request,send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
# flask run -p3000 --debug
app = Flask(__name__)
CORS(app)

@app.route("/<boxname>/filelist")
def get_filelist(boxname):
    # get file list from boxname floder
    if not os.path.exists('./'+boxname): 
        os.makedirs('./'+boxname)
    filelist = os.listdir('./'+boxname)
    print(filelist)

    return filelist

@app.route("/<boxname>/upload", methods=['POST','GET'])
def uploadfile(boxname):
        #if not exist boxname create box floder:
        if not os.path.exists('./'+boxname): 
            os.makedirs('./'+boxname)

        if request.method == 'POST':
            if 'the_file' not in request.files:
                return {
                    "info": "No file part"
                }
            f = request.files['the_file']
            f.save('./'+boxname+'/'+secure_filename(f.filename))
            return{
                 "info": "uploaded "+ secure_filename(f.filename)
            }
        else:
            return {
                "info": "use post method with file "
            }

import os

@app.route("/<boxname>/delete/<filename>", methods=['GET'])
def delete_file(boxname, filename):
    file_path = './{}/{}'.format(boxname, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        return {
            "info": "File {} deleted.".format(filename)
        }
    else:
        return {
            "info": "File {} does not exist.".format(filename)
        }
    

@app.route("/<boxname>/download/<filename>", methods=['GET'])
def download_file(boxname, filename):
    file_path = './{}/{}'.format(boxname, filename)

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return {
            "info": "File {} does not exist.".format(filename)
        }
    
@app.route("/<boxname>/deleteall/", methods=['GET'])
def delete_all_files(boxname):
    directory = os.path.join('.',boxname)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
    return {
        "info": "All files in {} deleted.".format(directory)
    }