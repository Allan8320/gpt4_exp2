def get_blog_input():

    print("\n========================================")
    print("        AI BLOG CONTENT GENERATOR")
    print("========================================")

    topic = input("Enter Blog Topic : ")
    style = input("Writing Style : ")
    tone = input("Tone : ")
    word_count = input("Word Count : ")

    print("\n----------------------------------------")
    print("Collected Information")
    print("----------------------------------------")

    print("Blog Topic :", topic)
    print("Style      :", style)
    print("Tone       :", tone)
    print("Words      :", word_count)

    return topic, style, tone, word_count