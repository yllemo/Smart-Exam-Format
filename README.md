
# Smart Exam Format

The **Smart Exam Format** is a structured plain text format for representing multiple-choice questions and their answers. This format is designed to handle both questions and user responses in a simple, readable format. It supports both single and multiple correct answers, user selections, and the inclusion of images in the question sections.

## Format Overview

### Questions:
- Each question starts with the question text.
- Any line that does not start with a hyphen (`-`) or a bracket (`[]`) and is not blank is considered a new question.
- Images can be embedded into questions using Markdown-style image syntax: `[]()` or `![]()` with generic links, such as `[Image](https://example.com/image.png)`.

### Answers:
- Each answer option begins with a hyphen (`-`).
- Correct answers are marked with a hyphen followed by an asterisk (`-*`).
- After the exam is completed, user-selected answers will be marked with `[ * ]` (with no spaces inside the brackets) before the hyphen, and unselected answers will be marked with `[]`. There can be a space after the brackets before the hyphen (`[] -` or `[*] -*`).

### Two States of the Smart Exam Format:
There are two distinct states for the **Smart Exam Format**:
1. **Input State (Exam File)**: This is the original exam format used as input, containing questions and answers. In this state, there are no brackets (`[]`) around the answers, and only correct answers are marked with `-*`.
2. **Executed State (User Responses)**: After the exam is completed and user answers are submitted for analysis, the user's selections are marked with brackets (`[]` or `[*]`). The correct answers remain marked with `-*`.

### Input State (Exam File):
This is what the exam file looks like before user execution:

```
What is 2 + 2? [Image here](https://example.com/image.png)
- 4
- 3
-* 5

What is the capital of France? [See Image 1.1](https://example.com/image2.png)
-* Paris
- Berlin
- Madrid

What is 5 + 5?
- 9
-* 10
-* 11
```

### Executed State (User Responses):
After the exam has been completed and submitted, the user's selections are reflected as shown:

```
What is 2 + 2? [Image here](https://example.com/image.png)
[*] - 4
[] - 3
[] -* 5

What is the capital of France? [See Image 1.1](https://example.com/image2.png)
[*] -* Paris
[] - Berlin
[] - Madrid

What is 5 + 5?
[] - 9
[*] -* 10
[*] -* 11
```

## Features

- **Correct Answers**: Correct answers are marked with `-*` after the answer option, making it easy to differentiate correct answers from incorrect ones.
- **User Selections**: After the exam, user-selected answers are marked with `[*]`, and unselected answers are marked with `[]`.
- **Support for Images**: You can include images within the question section using Markdown-style syntax with generic links, such as `[Image](https://example.com/image.png)`.

  Example with image:
  ```
  What is 2 + 2? [Image here](https://example.com/image.png)
  - 4
  - 3
  -* 5
  ```

- **Multiple Correct Answers**: The format supports questions with either single or multiple correct answers.
  
## Notes

- **Flexibility**: The Smart Exam Format is designed to be flexible, allowing for both human and machine readability. It can be easily parsed by a program while still being understandable to a person reading the file.
- **Blank Line Separation**: Each question is separated by a blank line for clarity, making it easier to distinguish between questions.
- **Customizable**: This format can be customized to include additional information, such as metadata or detailed explanations after each question, as needed.

## Use Cases

The **Smart Exam Format** is ideal for:
- Storing and sharing multiple-choice questions in a lightweight, portable format.
- Processing exam results where both correct answers and user selections need to be represented.
- Importing/exporting questions and answers between systems.
- Creating quizzes with images embedded in the questions to provide visual context or references.

## AI Integration

The **Smart Exam Format** is enhanced through AI integration, enabling:
- **Question Generation**: AI can generate new questions based on past exam results, aiding in continuous learning.
- **Result Analysis**: AI can suggest new questions focusing on topics where users frequently make mistakes, implementing a "diminishing returns" strategy.
- **Prompts for AI Models**: Example prompts and guidance are provided for various AI models, including ChatGPT, Copilot, Google Gemini, and local models (e.g., LM Studio, Ollama).

Refer to the `docs/ai_integration/` folder for prompt examples and guidance on using APIs and local models.

## Folder Structure

- **`src/parsers/`**: Parsing scripts for Smart Exam Format files.
- **`src/exam_simulators/`**: Web and desktop simulators with a focus feature for incorrect answers.
- **`src/cli_tools/`**: Command-line tools for interacting with the format.
- **`samples/sample_exams/`**: Sample exams demonstrating both Input and Executed states.
- **`samples/ai_generated_questions/`**: Example AI-generated questions based on previous exam results.
- **`analysis/export_formats/`**: Templates for result exports formatted for AI input.
- **`analysis/result_analysis/`**: Scripts and notebooks for analyzing exam results.
- **`docs/ai_integration/`**: AI prompt examples, API integration instructions, and local model usage.
- **`tests/`**: Unit tests to validate functionality.

## How to Use

1. Create a new `.txt` file or use any text editor to define your questions and answers in the **Smart Exam Format**.
2. Include images if needed by adding the appropriate Markdown-style image syntax in the question section.
3. Use a program (such as a parser or web application) that can process the format and handle user selections to track responses.

## Example Repository

This repository includes example implementations for parsing the **Smart Exam Format**, AI-enhanced question generation, and analysis of exam results. Clone, experiment, and contribute improvements!

---

Feel free to reach out if you have any questions or suggestions!
