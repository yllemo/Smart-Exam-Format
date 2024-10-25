
import argparse
import datetime

def load_exam(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def display_exam(questions):
    print("Starting the Exam:")
    user_responses = []
    for question in questions:
        if not question.startswith('-'):
            print(f"Question: {question.strip()}")
            answers = []
        elif question.startswith('-'):
            answers.append(question.strip())
            for idx, answer in enumerate(answers):
                print(f"  {idx + 1}. {answer}")
            response = input("Select your answer (number): ")
            user_responses.append((question.strip(), response))
    return user_responses

def save_results(responses, output_path):
    with open(output_path, 'w') as file:
        for question, response in responses:
            file.write(f"{question} - Answer: {response}\n")

def main():
    parser = argparse.ArgumentParser(description="SEF Exam CLI Tool")
    parser.add_argument('file', help="Path to the SEF formatted exam file")
    parser.add_argument('-o', '--output', help="Path to save the exam results", default="results.txt")
    args = parser.parse_args()

    questions = load_exam(args.file)
    responses = display_exam(questions)
    save_results(responses, args.output)
    print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()
