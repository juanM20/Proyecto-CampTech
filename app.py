from flask import Flask, render_template, url_for, request, redirect

from preprocessing import preprocessing
from speech_to_text import speech_to_text

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/form', methods = ['GET','POST'])
def form():

    resp = []

    if request.method == 'POST':
        text_news = request.form['text']
        audio = request.form['audio']

        print(text_news)
        print(audio)

        if text_news == '':
            text_news = speech_to_text(audio)
            resp = preprocessing(text_news)
        else:
            resp = preprocessing(text_news)


    return render_template('result.html', respuesta = resp)

if __name__ == "__main__":
    app.run()

