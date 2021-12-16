from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join("C:\\Users\\user\\python\\uploads", file.filename))
    return jsonify("done")
    
if __name__ == "__main__":
    app.debug = True
    app.run()