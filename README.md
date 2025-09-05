# Brutus
**Phishing**.....

A **cybersecurity educational project** that demonstrates how phishing techniques can be simulated in a controlled environment for awareness training, penetration testing, and defensive research.

> ⚠️ **Disclaimer:** This project is intended **strictly for educational and research purposes**.  
> Do **not** use this code for malicious purposes. The author is not responsible for misuse.

---

## Requirements
- Python 3.x  
- Flask (for web interface)  
- Localtonet (for exposing the app to external devices)

## Usage

1. Replace the content of `server_url.txt` with your **Localtonet URL**.  
   This simulates how an attacker might configure a public-facing address for a fake page.  

2. Run the Flask app locally:
   ```bash``
   python app.py

## Features
- Credentials will be saved in the credentials.txt