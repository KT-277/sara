from flask import Flask, request, jsonify, redirect, render_template
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import validators
from flask_cors import CORS
import random, string, json, os

app = Flask(__name__, template_folder='templates')
CORS(app) # Allows React frontend to call this API

# Applies basic security headers using Flask-Talisman
Talisman(app, content_security_policy=None)

# Simple rate limiting - 10 requests per minute per IP
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

# File to store shortened URLs
DATA_FILE = 'urls.json'

# Load existing data if file exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        url_store = json.load(f)
else:
    url_store = {}

# Helper: generates random short code
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Helper: detects potentially unsafe URLs
def looks_malicious(url):
    # The basic heuristic, just to simulate threat detection
    blocked_keywords = ['phish', 'malware', '.exe', '@', '://http']
    return any(keyword in url.lower() for keyword in blocked_keywords)

@app.route('/shorten', methods=['POST'])
@limiter.limit("5 per minute")
def shorten_url():
    data = request.get_json()

    if not data or 'url' not in data:
        return jsonify({'error': 'URL is missing'}), 400

    original_url = data['url']

    # Validate the URL format
    if not validators.url(original_url):
        return jsonify({'error': 'Invalid URL format'}), 400

    # Check for malicious patterns
    if looks_malicious(original_url):
        app.logger.warning(f"Blocked suspicious URL: {original_url}")
        return jsonify({'error': 'URL appears unsafe and was blocked'}), 403

    # Generate unique short code
    code = generate_code()
    url_store[code] = original_url

    # Save to JSON file (simple storage)
    with open(DATA_FILE, 'w') as f:
        json.dump(url_store, f, indent=4)

    return jsonify({'short_url': f"http://localhost:5000/{code}"}), 200

@app.route('/<code>')
def redirect_to_original(code):
    # Redirects to the original URL if code exists
    if code in url_store:
        return redirect(url_store[code])
    else:
        return jsonify({'error': 'Invalid or expired short code'}), 404

if __name__ == '__main__':
    app.run(debug=True)