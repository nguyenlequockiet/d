from flask import Flask, render_template, request
# Import các class mật mã từ thư mục cipher
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.rail_fence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)

# --- 1. TRANG CHỦ ---
@app.route("/")
def home():
    return render_template('index.html')

# --- 2. CAESAR CIPHER ---
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = CaesarCipher()
    result = cipher.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {result}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = CaesarCipher()
    result = cipher.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {result}"

# --- 3. VIGENERE CIPHER ---
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt_vigenere", methods=['POST'])
def vigen_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    cipher = VigenereCipher()
    result = cipher.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {result}"

@app.route("/decrypt_vigenere", methods=['POST'])
def vigen_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    cipher = VigenereCipher()
    result = cipher.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {result}"

# --- 4. RAIL FENCE CIPHER ---
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/encrypt_railfence", methods=['POST'])
def rail_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    cipher = RailFenceCipher()
    result = cipher.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {result}"

@app.route("/decrypt_railfence", methods=['POST'])
def rail_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    cipher = RailFenceCipher()
    result = cipher.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {result}"

# --- 5. PLAYFAIR CIPHER ---
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/encrypt_playfair", methods=['POST'])
def pf_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    pf = PlayFairCipher()
    matrix = pf.create_playfair_matrix(key)
    result = pf.playfair_encrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {result}"

@app.route("/decrypt_playfair", methods=['POST'])
def pf_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    pf = PlayFairCipher()
    matrix = pf.create_playfair_matrix(key)
    result = pf.playfair_decrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {result}"

# --- 6. TRANSPOSITION CIPHER ---
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/encrypt_transposition", methods=['POST'])
def trans_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    cipher = TranspositionCipher()
    result = cipher.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {result}"

@app.route("/decrypt_transposition", methods=['POST'])
def trans_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    cipher = TranspositionCipher()
    result = cipher.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {result}"

# Khởi chạy server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
