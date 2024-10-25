
import json
import argparse
from collections import Counter

def load_completed_exam(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def analyze_performance(answers):
    missed_questions = []
    correct_count = 0
    total_count = 0

    for line in answers:
        if line.startswith("[*]"):
            if "-*" in line:  # Correct answer chosen by user
                correct_count += 1
            else:  # Incorrect answer chosen by user
                missed_questions.append(line)
        total_count += 1 if line.strip() else 0

    missed_counter = Counter(missed_questions)
    return correct_count, total_count, missed_counter

def summarize_results(correct, total, missed_counter):
    accuracy = round((correct / total) * 100, 2) if total > 0 else 0
    summary = {
        "Total Questions": total,
        "Correct Answers": correct,
        "Accuracy (%)": accuracy,
        "Most Missed Questions": missed_counter.most_common(5)
    }
    return summary

def main():
    parser = argparse.ArgumentParser(description="SEF Result Analysis Tool")
    parser.add_argument('file', help="Path to the completed SEF exam file")
    parser.add_argument('-o', '--output', help="Path to save the analysis results", default="analysis_summary.json")
    args = parser.parse_args()

    answers = load_completed_exam(args.file)
    correct_count, total_count, missed_counter = analyze_performance(answers)
    summary = summarize_results(correct_count, total_count, missed_counter)

    with open(args.output, 'w') as f:
        json.dump(summary, f, indent=4)
    
    print(f"Analysis saved to {args.output}")
    print("Analysis Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
