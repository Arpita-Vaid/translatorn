from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def translate_text(text, src, dest):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={src}&tl={dest}&dt=t&q={requests.utils.quote(text)}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0][0][0]
    else:
        return "Translation failed"

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = None
    if request.method == 'POST':
        text = request.form['text']
        src = request.form['src']
        dest = request.form['dest']
        translated_text = translate_text(text, src, dest)
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)