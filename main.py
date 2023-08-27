
import random
from flask import Flask

jdm = ["Supra mk4","Silvia S15","RX-7 fd","350z","200sx","R-34","R-32","WRX STI"]


app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<h1>Selam</h1> <a href='/secim'>Rastgele bir araba seç</a>"

@app.route("/secim")
def secim():
    return f"<h1>{random.choice(jdm)}</h1>"


app.run(debug=True)
