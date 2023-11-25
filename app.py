from flask import Flask, request, jsonify

app = Flask(__name__)

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    text = data.get('text')
    shift = data.get('shift')
    encrypted_text = caesar_encrypt(text, shift)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    text = data.get('text')
    shift = data.get('shift')
    decrypted_text = caesar_decrypt(text, shift)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
   app.run(debug=True)