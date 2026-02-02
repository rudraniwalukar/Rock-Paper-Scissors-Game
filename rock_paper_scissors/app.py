from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "rps_secret_key"

choices = ["rock", "paper", "scissors"]

@app.route("/", methods=["GET", "POST"])
def index():
    if "user_score" not in session:
        session["user_score"] = 0
        session["computer_score"] = 0

    user_choice = None
    computer_choice = None
    result = None

    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You Win!"
            session["user_score"] += 1
        else:
            result = "Computer Wins!"
            session["computer_score"] += 1

    return render_template(
        "index.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result,
        user_score=session["user_score"],
        computer_score=session["computer_score"]
    )

@app.route("/reset")
def reset():
    session.clear()
    return render_template("index.html", user_score=0, computer_score=0)

if __name__ == "__main__":
    app.run(debug=True)
