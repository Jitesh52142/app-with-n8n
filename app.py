from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Your n8n webhook URL
WEBHOOK_URL = "https://n8n-render-a5pm.onrender.com/webhook/A_CHAT_GURU"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get("message")

    try:
        # Send message to the webhook
        response = requests.post(WEBHOOK_URL, json={"message": user_message}, timeout=10)

        # Try to parse JSON
        data = response.json()
        bot_reply = data.get("reply") or data.get("output")

        if bot_reply:
            return jsonify({"reply": bot_reply.strip()})
        else:
            return jsonify({"reply": "Guru: Trying to connect..."})

    except:
        # Hide errors, show generic message
        return jsonify({"reply": "Guru: Trying to connect..."})

if __name__ == '__main__':
    app.run(debug=True)
