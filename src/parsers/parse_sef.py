
import re
import json

def parse_sef_file(file_path):
    """
    Parses a Smart Exam Format (SEF) file and returns a structured dictionary of questions, answers, and user selections.
    
    Parameters:
        file_path (str): The path to the SEF .txt file.

    Returns:
        dict: A dictionary with parsed questions, answers, correct answers, and user selections.
    """

    # Initialize lists for storing parsed content
    questions = []
    current_question = None

    # Regex patterns for identifying SEF structure
    question_pattern = re.compile(r"^[^-\[\]]")  # Matches a line that doesn't start with '-' or '['
    answer_pattern = re.compile(r"^(-|\[\*\] -|\[\] -)")  # Matches lines with answer options
    correct_answer_marker = "-*"
    user_selected_marker = "[*]"
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()

                # Start of a new question
                if question_pattern.match(line):
                    if current_question:
                        # Append current question data to questions list before starting a new question
                        questions.append(current_question)
                    # Initialize a new question structure
                    current_question = {
                        "question_text": line,
                        "answers": [],
                        "correct_answers": [],
                        "user_selections": []
                    }

                # Answer option handling
                elif answer_pattern.match(line):
                    answer_text = line.split("-", 1)[1].strip()  # Extract answer text after the hyphen
                    current_question["answers"].append(answer_text)

                    # Check if it's a correct answer
                    if correct_answer_marker in line:
                        current_question["correct_answers"].append(answer_text)

                    # Check if it's a user-selected answer
                    if user_selected_marker in line:
                        current_question["user_selections"].append(answer_text)

            # Add the last question to the list (if file ends without blank line)
            if current_question:
                questions.append(current_question)

    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None

    return {
        "exam_title": file_path.split("/")[-1],
        "questions": questions
    }

# Example usage
file_path = "path/to/your/SEF_Exam.txt"
parsed_data = parse_sef_file(file_path)
if parsed_data:
    # Save parsed data as JSON for easier visualization and debugging
    with open("parsed_exam_output.json", "w") as json_file:
        json.dump(parsed_data, json_file, indent=4)
    print("Parsing complete. Results saved to parsed_exam_output.json.")
