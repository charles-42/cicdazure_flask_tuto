from flask import Flask,render_template

# on instancie un objet Flask qui est notre application
app = Flask(__name__)

# On définit notre première vue
@app.route("/")
def home():
    return render_template('index.html')

app.run()