
# Smart Exam Format

The **Smart Exam Format (SEF)** is a uniquely structured format designed to revolutionize digital learning. Built for versatility and simplicity, SEF leverages plain text files, making it extremely portable and easy to manage across various platforms and applications. SEF is specifically engineered to harness the power of **reinforcement learning with AI**, delivering a dynamic and adaptive learning experience.

## Why Choose Smart Exam Format?

- **Simplicity and Flexibility**: SEF uses a straightforward, text-based format. This makes it easy to read, edit, and share, requiring only a simple `.txt` file. The clean, structured format of SEF is intuitive to work with, making it accessible to educators, learners, and AI tools alike.
  
- **Two-State Design**: SEF includes two unique states: an **Input State** and an **Executed State**. This two-state design enables precise tracking of user responses, especially weaker or commonly missed questions. This structure allows for seamless identification of areas for improvement, which can then be reinforced with tailored questions.

- **Cycle of Learning and Reinforcement**: SEF transforms static exams into a powerful cycle of learning. By tracking incorrect answers, SEF enables the creation of customized follow-up questions. With AI integration, these new questions can address gaps in understanding from different perspectives, making SEF an ideal tool for ongoing, targeted learning.

- **Optimized for AI-Driven Reinforcement Learning**: SEF is designed to work seamlessly with AI systems like ChatGPT, Copilot, and Google Gemini. With AI-generated new questions based on user performance, SEF enables a unique reinforcement cycle that continuously adapts to the learner’s needs. The result? Enhanced retention, deeper understanding, and a highly engaging learning process.

## How Smart Exam Format Works

1. **Start with an Exam in the Input State**: Create a set of questions using the SEF structure, where correct answers are clearly marked, and user responses are tracked in the Executed State.

2. **AI-Driven Feedback and Reinforcement**: With incorrect answers identified in the Executed State, use AI to generate follow-up questions focusing on weak areas. This prompts students to review and re-engage with material from new angles, reinforcing understanding through targeted practice.

3. **Track Progress and Improve**: By cycling through exams that adapt to user responses, SEF creates a continuous loop of assessment and improvement. Learners not only see where they need improvement but can actively work to strengthen those areas with tailored support from AI.

## The Power of Plain Text

Using `.txt` files ensures maximum compatibility and ease of use, as these files can be read, modified, and processed across virtually any device or platform. The lightweight nature of plain text ensures SEF exams are easy to store, share, and integrate with other digital tools, making SEF an ideal choice for digital learning.

## Get Started with SEF Today!

Harness the simplicity and intelligence of the Smart Exam Format to elevate your learning experience. SEF's clean format, AI compatibility, and reinforcement learning capabilities make it the ultimate choice for educators, learners, and anyone aiming to maximize learning outcomes with minimal complexity.

---

This repository contains all the resources you need to implement the Smart Exam Format, including examples, scripts for parsing and analysis, and integrations with AI tools to help you build a powerful, adaptive learning system. Dive in and experience the next generation of digital learning!

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
