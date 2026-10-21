def generate_lesson_plan(subject, grade, topic, days):

    lesson_plan = []

    for day in range(1, days + 1):

        if day == 1:
            activity = "Introduction and basic concepts"

        elif day == days:
            activity = "Revision and assessment"

        else:
            activity = "Explanation, examples and practice"

        lesson_plan.append({
            "day": day,
            "subject": subject,
            "grade": grade,
            "topic": topic,
            "activity": activity
        })

    return lesson_plan
