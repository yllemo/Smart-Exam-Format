
import re
import fitz  # PyMuPDF for PDF parsing

def extract_text_from_pdf(file_path):
    """Extract text from PDF file."""
    text = ""
    with fitz.open(file_path) as pdf:
        for page_num in range(pdf.page_count):
            text += pdf[page_num].get_text()
    return text

def parse_questions_answers(text):
    """Parse text to extract questions, answers, and identify the correct answer."""
    questions_answers = []
    question_pattern = (
        r"QUESTION\s*\d+\s*(.*?)\s*A\.\s*(.*?)\s*B\.\s*(.*?)\s*C\.\s*(.*?)\s*D\.\s*(.*?)"
        r"(?:\s*E\.\s*(.*?))?\s*Correct Answer:\s*(\w)"
    )
    matches = re.findall(question_pattern, text, re.DOTALL)

    for match in matches:
        question, option_a, option_b, option_c, option_d, option_e, correct_answer = match

        # Map options to their letters, with E being optional
        options = {
            'A': option_a.strip(),
            'B': option_b.strip(),
            'C': option_c.strip(),
            'D': option_d.strip(),
        }
        
        if option_e:
            options['E'] = option_e.strip()

        # Build the answer list in Smart Exam Format
        formatted_answers = []
        for letter, answer_text in options.items():
            if letter == correct_answer:
                formatted_answers.append(f"-* {answer_text}")
            else:
                formatted_answers.append(f"- {answer_text}")

        questions_answers.append({
            "question": question.strip(),
            "answers": formatted_answers
        })

    return questions_answers

def export_to_smart_exam_format(parsed_data, output_file):
    """Export parsed questions and answers to Smart Exam Format."""
    with open(output_file, 'w') as f:
        for item in parsed_data:
            f.write(f"{item['question']}\n")
            for ans in item['answers']:
                f.write(f"{ans}\n")
            f.write("\n")  # Add blank line between questions

# Usage example
file_path = "path/to/exam.pdf"
output_file = "exam_output.txt"
text = extract_text_from_pdf(file_path)
parsed_data = parse_questions_answers(text)
export_to_smart_exam_format(parsed_data, output_file)
