from ollama_content import generate_content


def generate_summary(blog):

    prompt = f"""
You are an expert summarizer.

Summarize the following blog in approximately 100 words.

BLOG:
{blog}

Requirements:
1. Keep the important points.
2. Make the summary easy to understand.
3. Do not add information that is not present in the blog.
4. Keep the summary around 100 words.

Generate only the summary.
"""

    return generate_content(prompt)