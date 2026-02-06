from flask import Flask
import subprocess
import os

app = Flask(__name__)

@app.route("/start-mask")
def start_mask():
    script_path = os.path.join(os.getcwd(), "mask.py")
    subprocess.Popen(["python", script_path])
    return "Mask detection started!"

if __name__ == "__main__":
    app.run(port=5001, debug=True)
