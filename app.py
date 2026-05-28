from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)

# Secret key for session management
app.secret_key = "quiz_secret_key"


# Quiz Questions
questions = [

    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyper Transfer Markup Language",
            "Home Tool Markup Language"
        ],
        "answer": "Hyper Text Markup Language"
    },

    {
        "question": "Which language is used for web styling?",
        "options": [
            "Python",
            "HTML",
            "CSS",
            "Java"
        ],
        "answer": "CSS"
    },

    {
        "question": "Which of these is a Python framework?",
        "options": [
            "React",
            "Flask",
            "Bootstrap",
            "Node.js"
        ],
        "answer": "Flask"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": [
            "//",
            "#",
            "/* */",
            "<!-- -->"
        ],
        "answer": "#"
    },

    {
        "question": "Which company developed Python?",
        "options": [
            "Google",
            "Microsoft",
            "Apple",
            "Python Software Foundation"
        ],
        "answer": "Python Software Foundation"
    }

]


# Home Page
@app.route("/")
def home():

    # Reset quiz session
    session["score"] = 0
    session["question_index"] = 0

    # Shuffle questions each time
    random.shuffle(questions)

    return render_template("index.html")


# Quiz Page
@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    question_index = session.get("question_index", 0)

    score = session.get("score", 0)

    # Handle Answer Submission
    if request.method == "POST":

        selected_option = request.form.get("answer")

        current_question = questions[question_index]

        # Check if answer is correct
        if selected_option == current_question["answer"]:

            score += 1

            session["score"] = score

        # Move to next question
        question_index += 1

        session["question_index"] = question_index

    # Quiz Finished
    if question_index >= len(questions):

        return redirect(url_for("result"))

    current_question = questions[question_index]

    # Progress Bar Percentage
    progress = int(

        ((question_index + 1) / len(questions)) * 100

    )

    return render_template(

        "quiz.html",

        question=current_question,

        question_number=question_index + 1,

        total_questions=len(questions),

        progress=progress
    )


# Result Page
@app.route("/result")
def result():

    score = session.get("score", 0)

    total_questions = len(questions)

    percentage = int(

        (score / total_questions) * 100

    )

    # Performance Messages
    if percentage >= 80:

        message = "Excellent Performance 🚀"

    elif percentage >= 50:

        message = "Good Job 👍"

    else:

        message = "Keep Practicing 💪"

    return render_template(

        "result.html",

        score=score,

        total_questions=total_questions,

        percentage=percentage,

        message=message
    )


# Restart Quiz
@app.route("/restart")
def restart():

    session.clear()

    return redirect(url_for("home"))


# Run Flask App
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)