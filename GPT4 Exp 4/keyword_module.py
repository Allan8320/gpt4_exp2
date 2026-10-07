from ollama_content import generate_content


def generate_keywords(blog):

    prompt = f"""
You are an SEO specialist.

Generate SEO-friendly keywords for the following blog:

BLOG:
{blog}

Requirements:
1. Generate 8 to 12 relevant keywords.
2. Include important short keywords.
3. Include useful long-tail keywords.
4. Put each keyword on a separate line.
5. Do not add explanations.

Generate only the keywords.
"""

    return generate_content(prompt)