import json
import os
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for


BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)


@app.route('/')
def redirect_to_resume():
    return redirect(url_for('resume', lang='en'))


@app.route('/resume')
def resume():
    lang = request.args.get('lang', 'en')
    if lang not in ['en', 'fr']:
        lang = 'en'

    data_file = BASE_DIR / 'data' / f'resume_data_{lang}.json'

    if not data_file.exists():
        return f"Le fichier pour la langue '{lang}' est introuvable.", 404

    with data_file.open('r', encoding='utf-8') as json_file:
        resume_data = json.load(json_file)

    return render_template('resume.html', resume_data=resume_data, lang=lang)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '8080')))
