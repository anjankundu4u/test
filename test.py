from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Handle the JSON data here
    # For example, you can print it to the console
    print("Received JSON data:")
    print(json.dumps(data, indent=2))

    # You can also perform actions based on the received data
    # For example, send a response back to the sender
    response_data = {"message": "Webhook received successfully"}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
