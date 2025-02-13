from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    feature_flag = os.getenv("SHOW_WELCOME_MESSAGE", "off")  # Default is "off"
    
    if feature_flag.lower() == "on":
        return "🚀 Welcome to the NEW FEATURE!"
    else:
        return "⚡ Default Version - No new feature enabled."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
