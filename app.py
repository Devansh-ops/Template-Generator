from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

def create_prompt(recipient_name, email_subject, key_points, tone, additional_instructions):
    return {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant asked to generate an email template based on specific instructions."
            },
            {
                "role": "user",
                "content": f"Create an email template addressing {recipient_name} with the subject '{email_subject}'. The key points to include are: {key_points}. The tone should be {tone}. Additional instructions: {additional_instructions}. The email should be professional and suitable for a business context."
            }
        ]
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_template', methods=['POST'])
def generate_template():
    data = request.get_json()
    prompt = create_prompt(
        data['recipientName'],
        data['emailSubject'],
        data['keyPoints'],
        data['tone'],
        data['additionalInstructions']
    )

    response = client.chat.completions.create(**prompt)

    email_template = response.choices[0].message.content.strip()
    return jsonify({'generatedTemplate': email_template})

if __name__ == '__main__':
    app.run(debug=True)
