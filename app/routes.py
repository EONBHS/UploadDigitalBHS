from flask import Flask,render_template,redirect,request,jsonify,send_file, url_for, send_from_directory
from flask_cors import CORS
from app import app, db, models
from app.models import user
from app.forms import Form
import os
import zipfile

cors = CORS(app)

@app.route('/', methods=["GET", "POST"])
def home():
    items = user.query.all()
    print(items)


    return render_template("home.html", items=items)

@app.route('/zip', methods=["GET", "POST"])
def read_zip_file():
    file = request.files['file']
    if file.filename.endswith('.zip'):
        with zipfile.ZipFile(file, 'r') as zip_ref: 
            zip_ref.extractall('app/static')
        file_path = os.path.join('app/static', 'index.html')
        with open(file_path, 'r') as f:
            content = f.read()
        all_files = os.listdir('app/static')
        # for f in all_files:
        #     os.remove("app/templates/temp/" + f)
        return jsonify({'content': content})

    else:
        return jsonify({'error': 'file must be a zip file'}), 400
    
@app.route('/play')
def test():

    return render_template("temp/index.html")    
    

