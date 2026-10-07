from input_module import get_blog_input
from blog_module import generate_blog
from title_module import generate_titles
from keyword_module import generate_keywords
from summary_module import generate_summary
from meta_module import generate_meta_description
from utils import save_blog


def main():

    topic, style, tone, word_count = get_blog_input()

    print("\nGenerating Blog...")
    print("----------------------------------------")

    blog = generate_blog(
        topic,
        style,
        tone,
        word_count
    )

    print(blog)

    print("\n========================================")
    print("SUGGESTED TITLES")
    print("========================================")

    titles = generate_titles(blog)
    print(titles)

    print("\n========================================")
    print("SEO KEYWORDS")
    print("========================================")

    keywords = generate_keywords(blog)
    print(keywords)

    print("\n========================================")
    print("SUMMARY")
    print("========================================")

    summary = generate_summary(blog)
    print(summary)

    print("\n========================================")
    print("META DESCRIPTION")
    print("========================================")

    meta = generate_meta_description(blog)
    print(meta)

    file_path = save_blog(blog)

    print("\n========================================")
    print("Blog saved successfully!")
    print("File:", file_path)
    print("========================================")


if __name__ == "__main__":
    main()