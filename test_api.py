import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from werkzeug.middleware.shared_data import SharedDataMiddleware
from test import result
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import noisereduce as nr
from scipy.io.wavfile import write, read 


file_name = ""
child_id = 0
Current_Date = datetime.datetime.now().strftime ('%d-%b-%Y-%I-%M')

UPLOAD_FOLDER = 'C:\\Users\\user\\python\\uploads'
UPLOAD_FOLDER2 = 'C:\\Users\\user\\python\\uploads2'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav'}

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def foo():
    allValues = request.values
    child_id = allValues['id']
    return child_id

@app.route('/api/json/upload/result', methods=['POST'])
def final_result():
    if request.method == 'POST':
        # check if the post request has the file part
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # load data
            rate, data = read(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = data/1.0
            # select section of data that is noise
            noisy_part = data[10000:15000]
            # perform noise reduction
            reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=noisy_part, verbose=False)
            emotion = result(foo(),os.path.join(app.config['UPLOAD_FOLDER'] + "\\" + reduced_noise))
            os.rename(UPLOAD_FOLDER + "\\" + reduced_noise,UPLOAD_FOLDER2 + "\\" + emotion + "_" + str(Current_Date) + ".wav")
    return emotion

if __name__ == "__main__":
    app.debug = True
    app.run()

