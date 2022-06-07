from flask import Flask

app = Flask(__name__)

#API Routes
@app.route("/test")
def test():
    return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
    app.run(debug=True)