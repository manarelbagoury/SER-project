import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from werkzeug.middleware.shared_data import SharedDataMiddleware
from test import result
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Ser

engine = create_engine('mysql:///ser_db.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

child_id = 0

UPLOAD_FOLDER = 'C:\\Users\\user\\python\\uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav'}

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/json/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return jsonify (status= "Error", 
            message= "Please Upload the file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return jsonify (
	status= "Success",
	message= "File uploaded successfully"
)

@app.route('/api/json/upload/id', methods=['POST']) 
def foo():
    allValues = request.values
    child_id = allValues['id']
    return child_id

@app.route('/api/json/upload/result', methods=['POST'])
def final_result():
    if request.method == 'POST':
        # check if the post request has the file part
        #if 'file' not in request.files:
            #print('No file part')
            #return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        #if file.filename == '':
            #return jsonify (status= "Error", 
            #message= "Please Upload the file")
            #return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            newSer = Ser(child_id = foo(), emotion_detected = result(foo(),os.path.join(app.config['UPLOAD_FOLDER'] + "\\" + filename))
            session.add(newSer)
            session.commit()
    return "added to database!"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == "__main__":
    app.debug = True
    app.run()