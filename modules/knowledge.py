def search_knowledge(query):

    query = query.lower().strip()

    if query == "":
        return []

    try:
        with open(
            "data/knowledge.txt",
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

    except FileNotFoundError:

        return []

    paragraphs = content.split("\n")

    results = []

    for paragraph in paragraphs:

        if query in paragraph.lower():

            results.append(paragraph.strip())

    return results
