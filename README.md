# Phishing Website Detection Tool (Streamlit)

## Overview
A simple Streamlit app that performs lightweight, rule-based checks on a URL to flag common phishing indicators (missing HTTPS, suspicious characters, use of IP address in domain, suspicious keywords, etc.).

This project is meant as a portfolio/demo project for cybersecurity roles and can be deployed quickly on Streamlit Community Cloud.

## Project structure
```
phishing-detector/
├── app.py
├── requirements.txt
├── utils/
│   ├── feature_extractor.py
│   └── url_checker.py
├── dataset/
│   └── phishing.csv
├── tests/
│   └── test_url_checker.py
└── README.md
```

## Run locally
1. Create and activate a Python environment (Python 3.8+ recommended).
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run app.py
   ```

## Deploying on Streamlit Community Cloud
1. Push this repository to GitHub.
2. Go to https://streamlit.io/cloud and log in with GitHub.
3. Create a new app and point it to this repo and `app.py`.
4. Click deploy — Streamlit will install dependencies and provide a live URL.

## Notes
- This implementation uses **rule-based heuristics**, not a trained ML model. For higher accuracy, integrate a trained model and/or third-party reputation services.
- Do not use this tool as the sole protection — it is educational/demo-grade.
