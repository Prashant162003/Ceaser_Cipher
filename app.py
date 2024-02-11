from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift * (1 if encrypt else -1)) % 26 + base)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        operation = request.form['operation']
        if operation == 'encrypt':
            result_text = caesar_cipher(text, shift, encrypt=True)
        else:
            result_text = caesar_cipher(text, shift, encrypt=False)
        return render_template('index.html', text=text, shift=shift, operation=operation, result_text=result_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
