from ollama_content import generate_content


def generate_meta_description(blog):

    prompt = f"""
You are an SEO expert.

Create an SEO-friendly meta description for the following blog:

BLOG:
{blog}

Requirements:
1. Maximum 160 characters.
2. Make it attractive.
3. Include the main topic.
4. Encourage users to read the blog.
5. Generate only the meta description.

Do not provide explanations.
"""

    result = generate_content(prompt)

    # Keep only the first 160 characters
    return result.strip()[:160]