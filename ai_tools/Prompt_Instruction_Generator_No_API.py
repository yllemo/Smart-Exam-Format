
from pathlib import Path

def load_answers_from_file(file_path):
    """Load answers from SEF answer file."""
    if not Path(file_path).is_file():
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    with open(file_path, 'r') as file:
        return file.readlines()

def extract_exam_text(answers):
    """Format the answers text as a single string for AI input."""
    return "".join(answers).strip()

def generate_instruction_text(file_path):
    """Generate instructions for a new exam based on missed topics from a file."""
    answers = load_answers_from_file(file_path)
    exam_text = extract_exam_text(answers)

    instructions = f"""
Create a new exam based on the Smart Exam Format, using the information provided below.

### Smart Exam Format:
The Smart Exam Format is a structured way to represent multiple-choice questions and answers in plain text. The format is designed to handle both questions and user responses, following these rules:

**Questions**:
- Each question starts with the question text.
- Any line that does not start with a hyphen (-) or bracket ([ ]) and is not blank is considered a new question.

**Answers**:
- Each answer option starts with a hyphen (-), indicating it is an answer.
- Correct answers are marked with a hyphen followed by an asterisk (-*).
- If the exam has been executed by a user, the user-selected answers will be marked with [ * ] before the hyphen (- or -*), while unselected answers are marked with [ ].

**Answer Markings**:
- Correct answers are always marked with -*.
- The format supports both single and multiple correct answers.
- User selections are marked as follows:
  - Selected Correct Answer: [ * ] -* 
  - Unselected Correct Answer: [ ] -* 
  - Selected Incorrect Answer: [ * ] - 
  - Unselected Incorrect Answer: [ ] - 

**Separation**:
- Blank lines are used to separate different questions.

**Example**:
\```
What is 2 + 2?
[ * ] -* 4
[ ] - 3
[ ] - 5

What is the capital of France?
[ * ] -* Paris
[ ] - Berlin
[ ] - Madrid
\```

Additional Notes:
- Correct Answers: Correct answers are marked with -* after the answer option.
- User Selections: After the exam is executed, user-selected answers will be marked with [ * ], and unselected answers will be marked with [ ].
- Question Separation: Blank lines separate each question to maintain clarity.
- Format Flexibility: The format supports both single and multiple correct answers for each question.

### Previous Exam:
Below is the previous exam to use as input. Create a new exam based on this structure:

\```
{exam_text}
\```

### Instructions:
- Please create a new Smart Exam without any other output in text format.
- Ensure that the output exam follows the Smart Exam Format, with each answer on its own line starting with a "- " and the correct answer marked with "-* ".
- Do not include brackets [] in this new exam, as they are only used to reference user selections.

Format the output as markdown.
"""
    return instructions.strip()

if __name__ == "__main__":
    import sys

    # Check if a file path is provided, otherwise prompt the user to enter one
    if len(sys.argv) < 2:
        file_path = input("Please enter the path to your SEF answer file: ").strip()
    else:
        file_path = sys.argv[1]

    try:
        result = generate_instruction_text(file_path)
        print("Copy this prompt into any AI tool:")
        print(result)
    except FileNotFoundError as e:
        print(e)
