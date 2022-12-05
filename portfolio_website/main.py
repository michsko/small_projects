from flask import Flask, render_template
app = Flask("__name__")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/program")
def program():
    return render_template("program.html")


@app.route("/repertoire")
def repertoire():
    return render_template("repertoire.html")

@app.route("/bio")
def bio():
    return render_template("bio.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)


