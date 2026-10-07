from ollama_content import generate_content


def generate_blog(topic, style, tone, word_count):

    prompt = f"""
You are a professional blog writer.

Write a complete blog on the following topic:

Topic: {topic}

Writing Style: {style}

Tone: {tone}

Approximate Word Count: {word_count} words

Requirements:
1. Give the blog a suitable heading.
2. Include an introduction.
3. Include multiple meaningful sections.
4. Use clear paragraphs.
5. Include a conclusion.
6. Follow the requested writing style and tone.
7. Keep the blog close to the requested word count.

Generate only the blog.
"""

    return generate_content(prompt)