from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/', methods=['POST'])
def home_post():

  length = float(request.form['length'])
  height = float(request.form['height'])
  width = float(request.form['width'])
  output = length * height * width

  return render_template('index.html',
                         output_=output,
                         length_=length,
                         height_=height,
                         width_=width)


app.run(host="0.0.0.0")
