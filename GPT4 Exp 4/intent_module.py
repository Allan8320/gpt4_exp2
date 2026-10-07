from ollama_content import generate_content


def detect_intent(user_message):

    prompt = f"""
You are an intent classification system.

Classify the user's request into exactly ONE of these categories:

BLOG_GENERATION
SUMMARY
KEYWORD_GENERATION
META_DESCRIPTION
UNKNOWN

User request:
{user_message}

Rules:

BLOG_GENERATION:
The user wants to write, create, generate, or produce a blog.

SUMMARY:
The user wants to summarize or shorten existing content.

KEYWORD_GENERATION:
The user wants SEO keywords or keywords for a blog.

META_DESCRIPTION:
The user wants an SEO meta description.

UNKNOWN:
The request does not match any of the above.

Return ONLY the category name.
"""

    result = generate_content(prompt)

    result = result.strip().upper()

    if "BLOG_GENERATION" in result:
        return "BLOG_GENERATION"

    if "SUMMARY" in result:
        return "SUMMARY"

    if "KEYWORD_GENERATION" in result:
        return "KEYWORD_GENERATION"

    if "META_DESCRIPTION" in result:
        return "META_DESCRIPTION"

    return "UNKNOWN"