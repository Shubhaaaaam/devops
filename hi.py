from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Newbgit"
print("HiiII")
app.run()