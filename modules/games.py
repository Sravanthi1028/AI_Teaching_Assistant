def calculate_score(correct_answers, total_questions):

    if total_questions == 0:
        return 0

    score = (correct_answers / total_questions) * 100

    return round(score, 2)


def get_quiz_feedback(score):

    if score >= 90:
        return "Excellent! 🌟"

    elif score >= 75:
        return "Great job! Keep it up! 👍"

    elif score >= 50:
        return "Good attempt. Keep practicing! 📚"

    else:
        return "Keep practicing. You can improve! 💪"
