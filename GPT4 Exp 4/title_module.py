from ollama_content import generate_content


def generate_titles(blog):

    prompt = f"""
You are an expert content marketer.

Generate exactly five attractive and engaging blog titles
for the following blog:

BLOG:
{blog}

Requirements:
1. Generate exactly 5 titles.
2. Make them attractive.
3. Make them relevant to the blog.
4. Avoid duplicate titles.
5. Number them from 1 to 5.

Generate only the titles.
"""

    return generate_content(prompt)