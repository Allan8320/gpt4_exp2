from flask import Flask, render_template, request, jsonify

from blog_module import generate_blog
from title_module import generate_titles
from keyword_module import generate_keywords
from summary_module import generate_summary
from meta_module import generate_meta_description
from intent_module import detect_intent
from utils import save_blog


app = Flask(__name__)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# BLOG GENERATION
# ============================================================

@app.route("/generate-blog", methods=["POST"])
def generate_blog_api():

    try:
        data = request.get_json()

        topic = data.get("topic", "").strip()
        style = data.get("style", "Professional")
        tone = data.get("tone", "Formal")
        word_count = data.get("word_count", 500)

        if not topic:
            return jsonify({
                "error": "Please enter a blog topic."
            }), 400

        blog = generate_blog(
            topic,
            style,
            tone,
            word_count
        )

        save_blog(blog)

        return jsonify({
            "success": True,
            "blog": blog
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ============================================================
# TITLE GENERATION
# ============================================================

@app.route("/generate-titles", methods=["POST"])
def generate_titles_api():

    try:

        data = request.get_json()

        blog = data.get("blog", "").strip()

        if not blog:
            return jsonify({
                "error": "Please generate a blog first."
            }), 400

        titles = generate_titles(blog)

        return jsonify({
            "success": True,
            "titles": titles
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ============================================================
# KEYWORD GENERATION
# ============================================================

@app.route("/generate-keywords", methods=["POST"])
def generate_keywords_api():

    try:

        data = request.get_json()

        blog = data.get("blog", "").strip()

        if not blog:
            return jsonify({
                "error": "Please generate a blog first."
            }), 400

        keywords = generate_keywords(blog)

        return jsonify({
            "success": True,
            "keywords": keywords
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ============================================================
# SUMMARY GENERATION
# ============================================================

@app.route("/generate-summary", methods=["POST"])
def generate_summary_api():

    try:

        data = request.get_json()

        blog = data.get("blog", "").strip()

        if not blog:
            return jsonify({
                "error": "Please generate a blog first."
            }), 400

        summary = generate_summary(blog)

        return jsonify({
            "success": True,
            "summary": summary
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ============================================================
# META DESCRIPTION
# ============================================================

@app.route("/generate-meta", methods=["POST"])
def generate_meta_api():

    try:

        data = request.get_json()

        blog = data.get("blog", "").strip()

        if not blog:
            return jsonify({
                "error": "Please generate a blog first."
            }), 400

        meta = generate_meta_description(blog)

        return jsonify({
            "success": True,
            "meta": meta
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ============================================================
# INTENT DETECTION
# ============================================================

@app.route("/detect-intent", methods=["POST"])
def detect_intent_api():

    try:

        data = request.get_json()

        message = data.get("message", "").strip()

        if not message:
            return jsonify({
                "error": "Please enter a message."
            }), 400

        intent = detect_intent(message)

        return jsonify({
            "success": True,
            "intent": intent
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ============================================================
# AI CHATBOT
# ============================================================

@app.route("/chat", methods=["POST"])
def chat_api():

    try:

        data = request.get_json()

        message = data.get("message", "").strip()

        # Existing blog from frontend
        blog = data.get("blog", "").strip()

        if not message:
            return jsonify({
                "error": "Please enter a message."
            }), 400

        # ----------------------------------------------------
        # Detect user intent using Ollama
        # ----------------------------------------------------

        intent = detect_intent(message)

        # ----------------------------------------------------
        # BLOG GENERATION
        # ----------------------------------------------------

        if intent == "BLOG_GENERATION":

            # Use simple defaults for chatbot-generated blogs
            generated_blog = generate_blog(
                message,
                "Professional",
                "Informative",
                500
            )

            save_blog(generated_blog)

            return jsonify({
                "success": True,
                "intent": intent,
                "response": generated_blog,
                "blog": generated_blog
            })

        # ----------------------------------------------------
        # SUMMARY
        # ----------------------------------------------------

        elif intent == "SUMMARY":

            if not blog:

                return jsonify({
                    "success": True,
                    "intent": intent,
                    "response":
                        "Please generate a blog first so I can summarize it."
                })

            summary = generate_summary(blog)

            return jsonify({
                "success": True,
                "intent": intent,
                "response": summary
            })

        # ----------------------------------------------------
        # KEYWORDS
        # ----------------------------------------------------

        elif intent == "KEYWORD_GENERATION":

            if not blog:

                return jsonify({
                    "success": True,
                    "intent": intent,
                    "response":
                        "Please generate a blog first so I can create SEO keywords."
                })

            keywords = generate_keywords(blog)

            return jsonify({
                "success": True,
                "intent": intent,
                "response": keywords
            })

        # ----------------------------------------------------
        # META DESCRIPTION
        # ----------------------------------------------------

        elif intent == "META_DESCRIPTION":

            if not blog:

                return jsonify({
                    "success": True,
                    "intent": intent,
                    "response":
                        "Please generate a blog first so I can create a meta description."
                })

            meta = generate_meta_description(blog)

            return jsonify({
                "success": True,
                "intent": intent,
                "response": meta
            })

        # ----------------------------------------------------
        # UNKNOWN
        # ----------------------------------------------------

        else:

            return jsonify({
                "success": True,
                "intent": "UNKNOWN",
                "response":
                    "I can help you generate blogs, summaries, SEO keywords, and meta descriptions."
            })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ============================================================
# APPLICATION START
# ============================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )