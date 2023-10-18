from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def resume():
    with open('data/resume_data.json', 'r') as json_file:
        resume_data = json.load(json_file)

    return render_template('resume.html', resume_data=resume_data)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
