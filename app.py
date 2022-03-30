from flask import Flask

# on instancie un objet Flask qui est notre application
app = Flask(__name__)

# On définit notre première vue
@app.route("/")
def home():
    return "Hello"

app.run(host='0.0.0.0:8000')