from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(err):
    return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True, port=8089)
