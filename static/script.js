// Timer Functionality

const timerElement =
    document.getElementById("timer");

const quizForm =
    document.getElementById("quiz-form");

let timeLeft = 15;

if (timerElement) {

    const countdown = setInterval(() => {

        timerElement.innerText = timeLeft;

        // Timer color warning
        if (timeLeft <= 5) {

            timerElement.style.color = "#ff4d4d";
        }

        timeLeft--;

        // Auto submit when timer ends
        if (timeLeft < 0) {

            clearInterval(countdown);

            quizForm.submit();
        }

    }, 1000);
}

// Button Animation

const buttons =
    document.querySelectorAll("button");

buttons.forEach(button => {

    button.addEventListener("mouseenter", () => {

        button.style.transform =
            "scale(1.05)";
    });

    button.addEventListener("mouseleave", () => {

        button.style.transform =
            "scale(1)";
    });
});

// Option Card Selection Effect

const optionCards =
    document.querySelectorAll(".option-card");

optionCards.forEach(card => {

    card.addEventListener("click", () => {

        optionCards.forEach(c => {

            c.style.background =
                "rgba(255,255,255,0.12)";
        });

        card.style.background =
            "rgba(0,198,255,0.3)";
    });
});