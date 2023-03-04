from flask import Flask, render_template, jsonify

app = Flask(__name__)

BLOGS = [
    {
        "id":1,
        "title":"A Comprehensive guide to being a rebellious teen"
    },
    {
        "id":2,
        "title":"How to be an ideal Chief Justice"
    },
    {
        "id":3,
        "title":"Craziest things I've done so far..."
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", posts = BLOGS)

@app.route("/api/posts")
def get_blogs():
    return jsonify(BLOGS)

if __name__ == "__main__":
    app.run(debug = True)