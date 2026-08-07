# DevResume

A bilingual, ATS-friendly resume website built with Flask, HTML, and CSS.

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Open `http://localhost:8080`.

## Vercel deployment

Vercel detects the root `main.py` Flask application automatically. No build
command, output directory, `package.json`, or Node.js dependency is required.

Before deploying, open the Vercel project's **Settings > Build and Deployment**
page and set **Node.js Version** to `24.x`. Vercel validates this platform-level
setting before detecting the Python application, even though the application
does not use Node.js.

The application runtime is pinned to Python 3.14 in `.python-version` and its
only direct production dependency is declared in `requirements.txt`.
