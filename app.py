from flask import Flask, render_template, request

from utils.predict import predict_url


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        url = request.form.get("url", "").strip()

        # Check if URL is empty
        if not url:

            error = "Please enter a URL."

        # Check URL length
        elif len(url) > 2048:

            error = "URL is too long. Please enter a valid URL."

        else:

            try:

                result = predict_url(url)

            except Exception:

                error = (
                    "Unable to analyze this URL. "
                    "Please check the URL and try again."
                )

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":

    app.run(debug=True)