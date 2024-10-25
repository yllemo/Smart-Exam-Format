
using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Please provide the path to the SEF formatted exam file.");
            return;
        }

        string filePath = args[0];
        string outputPath = args.Length > 1 ? args[1] : "results.txt";

        var questions = LoadExam(filePath);
        var responses = DisplayExam(questions);
        SaveResults(responses, outputPath);

        Console.WriteLine($"Results saved to {outputPath}");
    }

    static List<string> LoadExam(string filePath)
    {
        return new List<string>(File.ReadAllLines(filePath));
    }

    static List<Tuple<string, string>> DisplayExam(List<string> questions)
    {
        Console.WriteLine("Starting the Exam:");
        var userResponses = new List<Tuple<string, string>>();
        string currentQuestion = string.Empty;
        var answers = new List<string>();

        foreach (string line in questions)
        {
            if (!line.StartsWith("-"))
            {
                if (!string.IsNullOrEmpty(currentQuestion))
                {
                    DisplayQuestion(currentQuestion, answers, userResponses);
                }
                currentQuestion = line.Trim();
                answers.Clear();
            }
            else if (line.StartsWith("-"))
            {
                answers.Add(line.Trim());
            }
        }
        if (!string.IsNullOrEmpty(currentQuestion))
        {
            DisplayQuestion(currentQuestion, answers, userResponses);
        }
        return userResponses;
    }

    static void DisplayQuestion(string question, List<string> answers, List<Tuple<string, string>> userResponses)
    {
        Console.WriteLine($"Question: {question}");
        for (int i = 0; i < answers.Count; i++)
        {
            Console.WriteLine($"  {i + 1}. {answers[i]}");
        }
        Console.Write("Select your answer (number): ");
        string response = Console.ReadLine();
        userResponses.Add(new Tuple<string, string>(question, response));
    }

    static void SaveResults(List<Tuple<string, string>> responses, string outputPath)
    {
        using (StreamWriter writer = new StreamWriter(outputPath))
        {
            foreach (var response in responses)
            {
                writer.WriteLine($"{response.Item1} - Answer: {response.Item2}");
            }
        }
    }
}
