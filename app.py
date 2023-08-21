import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

def generate_prompt(question):
    return f"You are a helpful assistant that answers questions.\n\nQ: {question}\nA:"

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
        )
        answer = response.choices[0].message["content"]
        return render_template("index.html", question=question, answer=answer)

    return render_template("index.html")

# Uncomment the below if you want to use a development server to test your application.

# if __name__ == '__main__':
#     app.run(debug=True)

# Uncomment the below if you want to use Waitress as your production server to test your application.

# if __name__ == '__main__':
#     # Run the application using Waitress
#     from waitress import serve
#     serve(app, host='0.0.0.0', port=8000)

# Gunicorn below is the default production server. Simply run `gunicorn app:application` to fire off the Gunicorn prod server.

# Export the Flask application object as 'application'
application = app
