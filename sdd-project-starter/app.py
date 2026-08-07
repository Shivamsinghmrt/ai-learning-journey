from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt', '')

    reply = f"You asked: {prompt}\nThis is your starter backend response."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
