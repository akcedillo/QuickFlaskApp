app = Flask(__name__)

@app.route("/")
def homeInfo():
    title = "my personal site"
    details = "These are my details"
    return render_template("base.html",infoA=title, infoB = details)