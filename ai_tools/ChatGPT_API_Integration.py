from openai import OpenAI
from pathlib import Path

# Set your OpenAI API key here
API_KEY = "your_default_api_key_here"  # Replace with your actual API key
client = OpenAI(api_key=API_KEY)


def load_answers_from_file(file_path):
    """Load answers from SEF answer file."""
    if not Path(file_path).is_file():
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    with open(file_path, 'r') as file:
        return file.readlines()

def extract_missed_topics(answers):
    """Identify and return questions answered incorrectly from SEF file."""
    return [line for line in answers if line.startswith("[*]") and "-*" not in line]

def create_prompt(missed_topics):
    """Generate a prompt for ChatGPT based on missed topics."""
    missed_summary = "\n".join(missed_topics)
    return (
        f"Using these missed topics, create a new SEF exam with 10 multiple-choice questions:\n\n{missed_summary}"
    )

def generate_sef_exam(file_path):
    """Generate SEF formatted questions based on missed topics from a file."""
    answers = load_answers_from_file(file_path)
    missed_topics = extract_missed_topics(answers)

    # Define messages for ChatCompletion API
    messages = [
        {
            "role": "system",
            "content": (
                "You are generating exam questions using the Smart Exam Format (SEF):\n"
                "1. Each question appears on a new line with answer options following.\n"
                "2. Answers start with '-' for regular and '-*' for correct options.\n"
                "3. Separate questions with a blank line."
            ),
        },
        {"role": "user", "content": create_prompt(missed_topics)},
    ]

    # Make the API call
    chat_completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        max_tokens=1500,
        temperature=0.7
    )

    return chat_completion.choices[0].message.content.strip()

if __name__ == "__main__":
    import sys

    # Check if a file path is provided, otherwise prompt the user to enter one
    if len(sys.argv) < 2:
        file_path = input("Please enter the path to your SEF answer file: ").strip()
    else:
        file_path = sys.argv[1]

    try:
        result = generate_sef_exam(file_path)
        print(result)
    except FileNotFoundError as e:
        print(e)
