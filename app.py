from flask import Flask, render_template, request
from flask_restful import Api
import os
import translator
from generated_text import SentenceGenerator

app = Flask(__name__)
api = Api(app)
port = 5100

# Path to the folder containing ISL videos
VIDEO_FOLDER = "static/videos"

EXAMPLE_SENTENCES = [
    "I am alone.",
    "He is nervous.",
    "She is special.",
    "We go to school.",
    "They are different.",
    "You are special.",
    "The light is yellow.",
    "The road is narrow.",
    "He and I are the same.",
    "We saw a fresh chart.",
]

@app.route("/", methods=["GET", "POST"])
def index():
    sentence = None
    isl_sentence = None
    matched_videos = None
    generated_sentences = None

    if request.method == "POST":
        # Get the input sentence
        sentence = request.form["sentence"]
        generate_flag = "generate" in request.form  # Check if generation is enabled
        
        print(f"Input sentence: {sentence}")
        
        # Get ISL Translation and matched videos
        translation_result = translator.main3(sentence)
        isl_sentence = translation_result.get("isl_sentence", "")
        matched_videos = translation_result.get("matched_videos", [])

        # Generate similar sentences only if the checkbox is selected
        if generate_flag:
            generator = SentenceGenerator()
            generator.__init__()  # Initialize the generator
            generated_sentences = generator.generate_sentences(sentence)

    # Pass data to the template
    return render_template(
        "index.html",
        sentence=sentence,
        isl_sentence=isl_sentence,
        matched_videos=matched_videos,
        generated_sentences=generated_sentences,
        example_sentences=EXAMPLE_SENTENCES
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
