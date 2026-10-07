import os


def save_blog(blog):

    folder = "outputs"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, "generated_blog.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(blog)

    return file_path