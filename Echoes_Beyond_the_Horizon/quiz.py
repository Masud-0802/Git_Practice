import streamlit as st

QUESTIONS = [
    {
        "question": "Which NASA mission successfully landed on the Moon in 1967?",
        "options": [
            "Lunar Prospector",
            "Surveyor 3",
            "Spirit",
            "Opportunity"
        ],
        "answer": "Surveyor 3",
        "explanation": "Surveyor 3 landed on the Moon on April 20, 1967."
    },
    {
        "question": "What type of spacecraft was Lunar Prospector?",
        "options": [
            "Lunar rover",
            "Mars orbiter",
            "Lunar orbiter",
            "Lunar lander"
        ],
        "answer": "Lunar orbiter",
        "explanation": "Lunar Prospector orbited the Moon to study its composition, gravity and magnetic fields."
    },
    {
        "question": "Which two spacecraft were NASA's Mars Exploration Rovers?",
        "options": [
            "Surveyor 3 and Spirit",
            "Spirit and Opportunity",
            "Lunar Prospector and Opportunity",
            "Spirit and Lunar Prospector"
        ],
        "answer": "Spirit and Opportunity",
        "explanation": "Spirit and Opportunity were twin robotic rovers sent to explore Mars."
    },
    {
        "question": "In which year did Spirit and Opportunity land on Mars?",
        "options": [
            "1997",
            "2001",
            "2004",
            "2012"
        ],
        "answer": "2004",
        "explanation": "Spirit landed on January 4, 2004, and Opportunity landed on January 25, 2004."
    },
    {
        "question": "What caused the final loss of communication with Opportunity?",
        "options": [
            "A collision with a meteorite",
            "A global dust storm",
            "A software update failure",
            "A solar eclipse"
        ],
        "answer": "A global dust storm",
        "explanation": "A massive dust storm in 2018 blocked sunlight from Opportunity's solar panels, and communication was never restored."
    }
]


def show_quiz():

    # Initialize quiz variables
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0

    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0

    if "quiz_answered" not in st.session_state:
        st.session_state.quiz_answered = False

    total_questions = len(QUESTIONS)
    index = st.session_state.quiz_index

    # Quiz completion screen
    if index >= total_questions:

        st.subheader("Quiz Completed!")

        score = st.session_state.quiz_score

        st.metric("Your Score", f"{score}/{total_questions}")

        percentage = (score / total_questions) * 100

        st.progress(percentage / 100)

        if percentage == 100:
            st.success("Outstanding! You answered every question correctly.")
        elif percentage >= 60:
            st.success("Good work! You have a solid understanding of these missions.")
        else:
            st.info("Keep exploring the missions and try again.")

        if st.button("Restart Quiz"):
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answered = False

            for i in range(total_questions):
                key = f"quiz_option_{i}"
                if key in st.session_state:
                    del st.session_state[key]

            st.rerun()

        return

    # Current question
    question_data = QUESTIONS[index]

    st.progress((index + 1) / total_questions)

    st.caption(f"QUESTION {index + 1} OF {total_questions}")

    st.subheader(question_data["question"])

    selected_option = st.radio(
        "Choose your answer:",
        question_data["options"],
        key=f"quiz_option_{index}",
        disabled=st.session_state.quiz_answered
    )

    # Submit answer
    if not st.session_state.quiz_answered:

        if st.button("Submit Answer"):

            st.session_state.quiz_answered = True

            if selected_option == question_data["answer"]:
                st.session_state.quiz_score += 1

            st.rerun()

    # Display feedback
    if st.session_state.quiz_answered:

        if selected_option == question_data["answer"]:
            st.success("Correct answer!")
        else:
            st.error(
                f"Incorrect. The correct answer is: "
                f"{question_data['answer']}"
            )

        st.info(question_data["explanation"])

        if st.button("Next Question"):

            st.session_state.quiz_index += 1
            st.session_state.quiz_answered = False

            st.rerun()