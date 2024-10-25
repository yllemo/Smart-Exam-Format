
using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;

class SEFParser
{
    public class Question
    {
        public string QuestionText { get; set; }
        public List<string> Answers { get; set; } = new List<string>();
        public List<string> CorrectAnswers { get; set; } = new List<string>();
        public List<string> UserSelections { get; set; } = new List<string>();
    }

    public static List<Question> ParseSEFFile(string filePath)
    {
        var questions = new List<Question>();
        Question currentQuestion = null;

        var questionPattern = new Regex(@"^[^-\[\]]");  // Matches lines that don't start with '-' or '['
        var answerPattern = new Regex(@"^(-|\[\*\] -|\[\] -)");  // Matches lines with answer options
        string correctAnswerMarker = "-*";
        string userSelectedMarker = "[*]";

        foreach (var line in File.ReadLines(filePath))
        {
            var trimmedLine = line.Trim();

            // Start of a new question
            if (questionPattern.IsMatch(trimmedLine))
            {
                if (currentQuestion != null)
                {
                    questions.Add(currentQuestion);
                }
                currentQuestion = new Question { QuestionText = trimmedLine };
            }
            else if (answerPattern.IsMatch(trimmedLine))
            {
                var answerText = trimmedLine.Split(new[] { '-' }, 2)[1].Trim();
                currentQuestion.Answers.Add(answerText);

                // Check if it's a correct answer
                if (trimmedLine.Contains(correctAnswerMarker))
                {
                    currentQuestion.CorrectAnswers.Add(answerText);
                }

                // Check if it's a user-selected answer
                if (trimmedLine.Contains(userSelectedMarker))
                {
                    currentQuestion.UserSelections.Add(answerText);
                }
            }
        }

        // Add the last question to the list
        if (currentQuestion != null)
        {
            questions.Add(currentQuestion);
        }

        return questions;
    }

    // Example usage
    static void Main()
    {
        string filePath = "path/to/your/SEF_Exam.txt";
        var parsedQuestions = ParseSEFFile(filePath);

        foreach (var question in parsedQuestions)
        {
            Console.WriteLine($"Question: {question.QuestionText}");
            Console.WriteLine("Answers:");
            foreach (var answer in question.Answers)
            {
                Console.WriteLine($"- {answer}");
            }
            Console.WriteLine("Correct Answers:");
            foreach (var correct in question.CorrectAnswers)
            {
                Console.WriteLine($"- {correct}");
            }
            Console.WriteLine("User Selections:");
            foreach (var selected in question.UserSelections)
            {
                Console.WriteLine($"- {selected}");
            }
            Console.WriteLine();
        }
    }
}
