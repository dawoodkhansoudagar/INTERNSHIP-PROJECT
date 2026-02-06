from flask import Flask, jsonify, request
from flask_cors import CORS
from voice import listen
from actions import do_action
from assistent import ask_ai

app = Flask(__name__)
CORS(app)



@app.route("/text", methods=["GET"])
def text_query():
    query = request.args.get("query")

    if not query:
        return jsonify({"response": "No input received"})

    action = do_action(query)
    if action:
        return jsonify({"response": action})

    answer = ask_ai(query)
    return jsonify({"response": answer})




@app.route("/voice", methods=["GET"])
def voice_command():
    text = listen()

    if not text:
        return jsonify({"response": "I didn't hear anything"})

    action = do_action(text)
    if action:
        return jsonify({"response": action})

    ai_response = ask_ai(text)
    return jsonify({"response": ai_response})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
