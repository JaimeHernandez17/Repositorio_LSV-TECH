# The framework flask is installed to facilitate the task of creating a web application with python and
# The libraries "Flask" and "render_template" are imported
from flask import Flask, render_template

# The app Flask is created
app = Flask(__name__)


# The first route is added to app to redirect to "index.html" archive in the templates directory
@app.route("/")
def index():
    return render_template("index.html")


# In case of not finding a page, the application will redirect to a file "error.html"
@app.errorhandler(404)
def page_not_found(err):
    return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True, port=8089)
