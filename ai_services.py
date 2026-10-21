def generate_learning_content(subject, grade, topic, level):

    if level == "Beginner":

        explanation = (
            f"{topic} is a basic concept in {subject}. "
            f"We will learn it step by step using simple words "
            f"so that a {grade} student can understand it easily."
        )

        example = (
            f"Imagine a simple real-life situation related to "
            f"{topic}. We can use this example to understand "
            f"the concept more easily."
        )

        question = (
            f"What is {topic}? Explain it in your own words."
        )

    elif level == "Intermediate":

        explanation = (
            f"{topic} is an important concept in {subject}. "
            f"It can be understood by connecting the basic idea "
            f"with practical examples and applications."
        )

        example = (
            f"Consider a real-world example where {topic} "
            f"is used. Identify the important steps and explain "
            f"how they work."
        )

        question = (
            f"Explain {topic} and give one real-world example."
        )

    else:

        explanation = (
            f"{topic} is an advanced concept in {subject}. "
            f"Students should understand its working, applications "
            f"and important concepts related to it."
        )

        example = (
            f"Consider a practical problem involving {topic}. "
            f"Analyze the problem and explain how {topic} "
            f"can be applied to solve it."
        )

        question = (
            f"Explain {topic} in detail and discuss its applications."
        )

    return {
        "subject": subject,
        "grade": grade,
        "topic": topic,
        "level": level,
        "objective": f"Understand the basic concepts of {topic} and apply them.",
        "explanation": explanation,
        "example": example,
        "question": question
    }