from flask import Flask, render_template, request
#filepath = "static/detail.txt"

app = Flask(__name__)

@app.route("/")
def hello():
    title = "my personal site"
    details = "These are my details"
    detail_text = readDetails()
    return render_template('base.html',infoA=title, infoB = details, detail_text=detail_text)

# Function to read in details for page
def readDetails():
    with open('static/detail.txt', 'r') as file:
        detail_text = file.read()
        return detail_text
        #return [line for line in f]

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    if request.method == 'POST':
        name=request.form['name']
        return render_template('form.html', name=name)
    return render_template('form.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

## When running this file directly...
if __name__ == "__main__":
    app.run(debug=True, port=3000)