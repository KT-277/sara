# Secure URL Shortener

## Project Overview

The Secure URL Shortener is a web application that allows users to shorten URLs securely. The application is built with **React.js** for the frontend and **Flask** for the backend, with JSON file-based storage for URL data. It includes multiple security layers such as input validation, phishing/malware detection, rate limiting, and secure headers.

**Key Features:**

* Shorten long URLs quickly and easily
* Input validation for safe URL submission
* Detection and blocking of malicious URLs
* Rate limiting to prevent abuse
* Secure frontend-backend communication (CORS and HTTPS headers)
* User-friendly frontend with smooth transitions and Poppins font

## Project Structure

```
D:/Sara/project
├── app.py                 # Flask backend
├── urls.json              # Stores original and shortened URLs
├── frontend/              # React frontend
│   ├── package.json
│   ├── public/
│   └── src/
├── README.md
└── venv/                  # Python virtual environment
```

## Setup Instructions

### Backend (Flask)

1. Navigate to the project folder:

```bash
cd D:/Sara/project
```

2. Create and activate a Python virtual environment:

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the backend server:

```bash
python app.py
```

5. Backend will run on:

```
http://127.0.0.1:5000/
```

### Frontend (React)

1. Open a new terminal and navigate to the frontend folder:

```bash
cd D:/Sara/project/frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the React development server:

```bash
npm start
```

4. Frontend will run on:

```
http://localhost:3000/
```

## Usage

* Open the frontend in a browser.
* Enter a valid URL and click **Shorten URL**.
* If valid, the shortened URL will appear.
* Invalid or malicious URLs will be blocked with an error message.

## Security Features

* Input validation using regex and URL validators
* Malicious URL detection (phishing/malware)
* Rate limiting (10 requests per minute per IP)
* Secure headers via Flask-Talisman
* CORS enabled for frontend-backend communication
* Logging of suspicious URL submissions in `security.log`

## Demo Screenshots

1. Frontend homepage
2. Successful URL shortening
3. Invalid URL input blocked
4. Malicious URL blocked
5. Network requests in browser DevTools
6. Backend logging of suspicious attempts

## Repository Link

[GitHub Repository](https://github.com/KT-277/sara)
