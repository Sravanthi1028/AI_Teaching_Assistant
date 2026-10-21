from faster_whisper import WhisperModel
import tempfile
import os
import re


# Load Whisper model
model = WhisperModel(
    "base.en",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_file):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as temp_file:

        temp_file.write(audio_file.getvalue())

        audio_path = temp_file.name

    try:

        segments, info = model.transcribe(audio_path)

        text = ""

        for segment in segments:
            text += segment.text + " "

        return text.strip()

    finally:

        os.remove(audio_path)


def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        "",
        text
    )

    text = " ".join(text.split())

    return text


def calculate_reading_accuracy(
    expected_text,
    student_text
):

    expected = clean_text(expected_text)

    student = clean_text(student_text)

    if expected == "":
        return 0

    expected_words = expected.split()
    student_words = student.split()

    correct_words = 0

    for i in range(
        min(
            len(expected_words),
            len(student_words)
        )
    ):

        if expected_words[i] == student_words[i]:
            correct_words += 1

    accuracy = (
        correct_words /
        len(expected_words)
    ) * 100

    return round(accuracy, 2)


def get_reading_feedback(accuracy):

    if accuracy >= 90:

        return "Excellent reading! 🌟"

    elif accuracy >= 75:

        return "Good reading. Keep practicing! 👍"

    elif accuracy >= 50:

        return "Good attempt. Practice the sentence again. 📖"

    else:

        return "Keep practicing your reading. You can improve! 💪"
