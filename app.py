from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store complaints in a simple list (resets when server restarts)
complaints = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        room = request.form["room"]
        complaint = request.form["complaint"]
        complaints.append({
            "name": name,
            "room": room,
            "complaint": complaint,
            "status": "Pending"
        })
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", complaints=complaints)

if __name__ == "__main__":
    app.run(debug=True)
