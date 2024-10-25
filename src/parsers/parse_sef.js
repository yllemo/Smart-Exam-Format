
const fs = require('fs');

function parseSEFFile(filePath) {
    // Read the file content
    const content = fs.readFileSync(filePath, 'utf-8').split('\n');
    const questions = [];
    let currentQuestion = null;

    // Regular expressions for identifying SEF structure
    const questionPattern = /^[^\-\[\]]/;  // Lines that don't start with '-' or '['
    const answerPattern = /^(-|\[\*\] -|\[\] -)/;  // Lines that start with '-' or '[*] -' or '[] -'
    const correctAnswerMarker = "-*";
    const userSelectedMarker = "[*]";

    content.forEach(line => {
        line = line.trim();

        // Start of a new question
        if (questionPattern.test(line)) {
            if (currentQuestion) {
                questions.push(currentQuestion);
            }
            currentQuestion = {
                question_text: line,
                answers: [],
                correct_answers: [],
                user_selections: []
            };
        } else if (answerPattern.test(line)) {
            const answerText = line.split("-", 2)[1].trim();
            currentQuestion.answers.push(answerText);

            // Check if it's a correct answer
            if (line.includes(correctAnswerMarker)) {
                currentQuestion.correct_answers.push(answerText);
            }

            // Check if it's a user-selected answer
            if (line.includes(userSelectedMarker)) {
                currentQuestion.user_selections.push(answerText);
            }
        }
    });

    // Add the last question to the list
    if (currentQuestion) {
        questions.push(currentQuestion);
    }

    return {
        exam_title: filePath.split('/').pop(),
        questions: questions
    };
}

// Example usage
const filePath = "path/to/your/SEF_Exam.txt";
const parsedData = parseSEFFile(filePath);
fs.writeFileSync("parsed_exam_output.json", JSON.stringify(parsedData, null, 4));
console.log("Parsing complete. Results saved to parsed_exam_output.json.");
