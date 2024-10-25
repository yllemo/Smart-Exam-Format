
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Newtonsoft.Json; // Requires Newtonsoft.Json for JSON serialization

class SEFResultAnalysis
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Please provide the path to the completed SEF exam file.");
            return;
        }

        string filePath = args[0];
        string outputPath = args.Length > 1 ? args[1] : "analysis_summary.json";

        var lines = File.ReadAllLines(filePath);
        var (correctCount, totalCount, missedQuestions) = AnalyzePerformance(lines);
        var summary = SummarizeResults(correctCount, totalCount, missedQuestions);

        string jsonSummary = JsonConvert.SerializeObject(summary, Formatting.Indented);
        File.WriteAllText(outputPath, jsonSummary);

        Console.WriteLine($"Analysis saved to {outputPath}");
        DisplaySummary(summary);
    }

    static (int correctCount, int totalCount, Dictionary<string, int> missedQuestions) AnalyzePerformance(string[] lines)
    {
        var missedQuestions = new Dictionary<string, int>();
        int correctCount = 0, totalCount = 0;

        foreach (var line in lines)
        {
            if (line.StartsWith("[*]"))
            {
                if (line.Contains("-*")) // Correct answer chosen
                    correctCount++;
                else // Incorrect answer chosen
                {
                    if (missedQuestions.ContainsKey(line))
                        missedQuestions[line]++;
                    else
                        missedQuestions[line] = 1;
                }
            }
            if (!string.IsNullOrWhiteSpace(line)) totalCount++;
        }
        return (correctCount, totalCount, missedQuestions);
    }

    static Dictionary<string, object> SummarizeResults(int correct, int total, Dictionary<string, int> missedQuestions)
    {
        double accuracy = total > 0 ? Math.Round((correct / (double)total) * 100, 2) : 0;
        var summary = new Dictionary<string, object>
        {
            { "Total Questions", total },
            { "Correct Answers", correct },
            { "Accuracy (%)", accuracy },
            { "Most Missed Questions", missedQuestions.OrderByDescending(kvp => kvp.Value).Take(5).ToList() }
        };
        return summary;
    }

    static void DisplaySummary(Dictionary<string, object> summary)
    {
        Console.WriteLine("Analysis Summary:");
        foreach (var item in summary)
        {
            Console.WriteLine($"{item.Key}: {item.Value}");
        }
    }
}
