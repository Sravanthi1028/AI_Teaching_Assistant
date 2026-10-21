import streamlit as st
from ai_services import generate_learning_content
from modules.knowledge import search_knowledge
from modules.lesson import generate_lesson_plan
from modules.reading import (
    transcribe_audio,
    calculate_reading_accuracy,
    get_reading_feedback
)
from modules.games import calculate_score, get_quiz_feedback
from modules.lesson import generate_lesson_plan
from modules.knowledge import search_knowledge

# Page settings
st.set_page_config(
    page_title="AI Teaching Assistant",
    page_icon="🎓",
    layout="wide"
)


# Title
st.title("🎓 AI Teaching Assistant")

st.write(
    "An AI-powered platform designed to support "
    "teachers in personalized and inclusive learning."
)


# Sidebar
st.sidebar.title("📚 Teaching Modules")

module = st.sidebar.selectbox(
    "Select a module",
    [
        "Dashboard",
        "AI Content & Personalized Learning",
        "Knowledge Base",
        "Smart Lesson Planner",
        "Reading Assessment",
        "Educational Games & Quiz"
    ]
)


# Dashboard
if module == "Dashboard":

    st.header("Teacher Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📚 Lessons", "0")

    with col2:
        st.metric("📝 Assessments", "0")

    with col3:
        st.metric("🎮 Activities", "0")

    with col4:
        st.metric("👨‍🎓 Students", "0")

    st.divider()

    st.subheader("Welcome to the AI Teaching Assistant")

    st.write(
        """
        This application helps teachers create educational
        content, personalized learning materials, lesson plans,
        reading assessments and interactive quizzes.
        """
    )


# AI Content Module
elif module == "AI Content & Personalized Learning":

    st.header("🤖 AI Content & Personalized Learning")

    st.write(
        "Create learning material based on the student's "
        "class, subject, topic and learning level."
    )

    subject = st.selectbox(
        "📚 Select Subject",
        [
            "Mathematics",
            "Science",
            "English",
            "Computer Science"
        ]
    )

    grade = st.selectbox(
        "🎓 Select Class",
        [
            "Class 5",
            "Class 6",
            "Class 7",
            "Class 8",
            "Class 9",
            "Class 10"
        ]
    )

    topic = st.text_input(
        "📝 Enter Topic",
        placeholder="Example: Fractions"
    )

    level = st.selectbox(
        "👨‍🎓 Student Learning Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    # Generate learning content
    if st.button("✨ Generate Learning Content"):

        if topic.strip() == "":
            st.warning("Please enter a topic.")

        else:

            result = generate_learning_content(
                subject,
                grade,
                topic,
                level
            )

            st.subheader("📖 Personalized Learning Content")

            st.write(f"**Subject:** {result['subject']}")
            st.write(f"**Class:** {result['grade']}")
            st.write(f"**Topic:** {result['topic']}")
            st.write(f"**Level:** {result['level']}")

            st.divider()

            st.subheader("🎯 Learning Objective")

            st.write(
                result["objective"]
            )

            st.subheader("📚 Explanation")

            st.write(
                result["explanation"]
            )

            st.subheader("💡 Example")

            st.write(
                result["example"]
            )

            st.subheader("📝 Practice Question")

            st.write(
                result["question"]
            )


# Knowledge Base Module
# Knowledge Base Module
# Knowledge Base Module
elif module == "Knowledge Base":

    st.header("📚 Knowledge Base")

    st.write(
        "Search educational information from the "
        "teacher's knowledge base."
    )

    query = st.text_input(
        "🔍 Search Knowledge Base",
        placeholder="Example: fractions"
    )

    if st.button("🔎 Search"):

        if query.strip() == "":

            st.warning(
                "Please enter a topic to search."
            )

        else:

            results = search_knowledge(query)

            if len(results) == 0:

                st.info(
                    "No information found for your search."
                )

            else:

                st.subheader(
                    "📖 Search Results"
                )

                for result in results:

                    st.write(
                        f"• {result}"
                    )


# Smart Lesson Planner Module
# Smart Lesson Planner Module
# Smart Lesson Planner Module
elif module == "Smart Lesson Planner":

    st.header("📅 Smart Lesson Planner")

    st.write(
        "Create a structured lesson plan based on "
        "the subject, class, topic and number of days."
    )

    subject = st.selectbox(
        "📚 Select Subject",
        [
            "Mathematics",
            "Science",
            "English",
            "Computer Science"
        ],
        key="lesson_subject"
    )

    grade = st.selectbox(
        "🎓 Select Class",
        [
            "Class 5",
            "Class 6",
            "Class 7",
            "Class 8",
            "Class 9",
            "Class 10"
        ],
        key="lesson_grade"
    )

    topic = st.text_input(
        "📝 Enter Topic",
        placeholder="Example: Fractions",
        key="lesson_topic"
    )

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=7,
        value=5,
        step=1
    )

    if st.button("📋 Generate Lesson Plan"):

        if topic.strip() == "":

            st.warning(
                "Please enter a topic."
            )

        else:

            lesson_plan = generate_lesson_plan(
                subject,
                grade,
                topic,
                days
            )

            st.subheader(
                "📋 Generated Lesson Plan"
            )

            for lesson in lesson_plan:

                st.write(
                    f"### Day {lesson['day']}"
                )

                st.write(
                    f"**Subject:** {lesson['subject']}"
                )

                st.write(
                    f"**Class:** {lesson['grade']}"
                )

                st.write(
                    f"**Topic:** {lesson['topic']}"
                )

                st.write(
                    f"**Activity:** {lesson['activity']}"
                )

                st.divider()
# Reading Assessment Module
# Reading Assessment Module
# Reading Assessment Module
# Reading Assessment Module
elif module == "Reading Assessment":

    st.header("🎤 Reading Assessment")

    st.write(
        "Evaluate a student's reading by recording "
        "their voice."
    )

    expected_text = st.text_area(
        "📖 Expected Reading Text",
        value="The sun rises in the east."
    )

    audio_value = st.audio_input(
        "🎤 Record Student Reading",
        sample_rate=16000
    )

    if audio_value:

        st.audio(
            audio_value,
            format="audio/wav"
        )

        if st.button("📊 Evaluate Reading"):

            with st.spinner(
                "🎧 Converting speech to text..."
            ):

                student_text = transcribe_audio(
                    audio_value
                )

            if student_text == "":

                st.error(
                    "We could not detect your voice. "
                    "Please record again."
                )

            else:

                st.subheader("🗣️ Detected Reading")

                st.write(student_text)

                accuracy = calculate_reading_accuracy(
                    expected_text,
                    student_text
                )

                feedback = get_reading_feedback(
                    accuracy
                )

                st.subheader(
                    "📊 Reading Assessment Result"
                )

                st.metric(
                    "Reading Accuracy",
                    f"{accuracy}%"
                )

                st.write(
                    f"### {feedback}"
                )
# Educational Games and Quiz Module
# Educational Games and Quiz Module
# Educational Games and Quiz Module
# Educational Games and Quiz Module
elif module == "Educational Games & Quiz":

    st.header("🎮 Educational Games & Quiz")

    st.write(
        "Test your knowledge with a short educational quiz."
    )

    questions = [
        {
            "question": "What is 5 + 3?",
            "options": ["6", "7", "8", "9"],
            "answer": "8"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": [
                "Earth",
                "Mars",
                "Jupiter",
                "Venus"
            ],
            "answer": "Mars"
        },
        {
            "question": "Which language is used to create web pages?",
            "options": [
                "HTML",
                "Python",
                "SQL",
                "Java"
            ],
            "answer": "HTML"
        },
        {
            "question": "What is the largest ocean?",
            "options": [
                "Indian Ocean",
                "Atlantic Ocean",
                "Pacific Ocean",
                "Arctic Ocean"
            ],
            "answer": "Pacific Ocean"
        },
        {
            "question": "How many sides does a triangle have?",
            "options": [
                "2",
                "3",
                "4",
                "5"
            ],
            "answer": "3"
        }
    ]

    st.subheader("📝 Answer the Questions")

    answers = []

    for i, question in enumerate(questions):

        st.write(f"### Question {i + 1}")

        st.write(question["question"])

        selected_answer = st.selectbox(
            "Choose your answer:",
            question["options"],
            index=None,
            placeholder="-- Select an answer --",
            key=f"quiz_select_{i}"
        )

        if selected_answer is None:
            answers.append(None)
        else:
            answers.append(selected_answer)

    st.divider()

    if st.button("🎯 Submit Quiz"):

        if None in answers:

            st.warning(
                "Please answer all questions before submitting the quiz."
            )

        else:

            correct_answers = 0

            for i in range(len(questions)):

                if answers[i] == questions[i]["answer"]:

                    correct_answers += 1

            total_questions = len(questions)

            score = calculate_score(
                correct_answers,
                total_questions
            )

            feedback = get_quiz_feedback(score)

            st.subheader(
                "📊 Quiz Result"
            )

            st.metric(
                "Your Score",
                f"{score}%"
            )

            st.write(
                f"**Correct Answers:** "
                f"{correct_answers}/{total_questions}"
            )

            st.write(
                f"### {feedback}"
            )