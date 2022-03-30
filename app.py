from flask import Flask,render_template

# on instancie un objet Flask qui est notre application
app = Flask(__name__)

# On définit notre première vue
@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)