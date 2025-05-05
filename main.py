from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

@app.route('/')
def redirect_to_resume():
    return redirect(url_for('resume', lang='en'))

@app.route('/resume')
def resume():
    lang = request.args.get('lang', 'en')
    if lang not in ['en', 'fr']:
        lang = 'en'

    data_file = f'data/resume_data_{lang}.json'

    if not os.path.exists(data_file):
        return f"Le fichier pour la langue '{lang}' est introuvable.", 404

    with open(data_file, 'r', encoding='utf-8') as json_file:
        resume_data = json.load(json_file)

    return render_template('resume.html', resume_data=resume_data, lang=lang)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
