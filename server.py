from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
  return '<h1 style="color: blue">welcome to ITIL</h1> prn = 230344223003 name = Aniket Bhole phone_no ="75825" '
  

app.run(port=4000, host="0.0.0.0", debug=True)
