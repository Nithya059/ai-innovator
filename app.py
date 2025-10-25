from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key (can use Colab secrets or .env if available)
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        problem = request.form.get("problem")
        prompt = f"Generate a complete startup idea including name, description, key features, and a logo concept for this problem: {problem}"
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300
        )
        result = response.choices[0].text.strip()
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
