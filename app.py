from flask import Flask, render_template

app = Flask(__name__)

# Sua mensagem personalizada
MENSAGEM = "Feliz aniversário atrasado!!" \
""

@app.route('/')
def home():
    return render_template('index.html', mensagem=MENSAGEM)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)