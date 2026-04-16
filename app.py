from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # O Flask procura automaticamente o index dentro da pasta /templates
    return render_template('index.html')

if __name__ == '__main__':
    # Roda o servidor local na porta 5000
    app.run(debug=True)