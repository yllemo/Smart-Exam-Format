
# Smart Exam Format

The **Smart Exam Format** is a structured plain text format for representing multiple-choice questions and their answers. This format is designed to handle both questions and user responses in a simple, readable format. It supports both single and multiple correct answers, user selections, and the inclusion of images in the question sections.

## Format Overview

### Questions:
- Each question starts with the question text.
- Any line that does not start with a hyphen (`-`) or a bracket (`[ ]`) and is not blank is considered a new question.
- Images can be embedded into questions using Markdown-style image syntax: `[]()` or `![]()`.

### Answers:
- Each answer option begins with a hyphen (`-`).
- Correct answers are marked with a hyphen followed by an asterisk (`-*`).
- After the exam is completed, user-selected answers will be marked with `[ * ]` before the hyphen, while unselected answers will be marked with `[ ]`.

### Answer Markings:
- **Correct answers** are always marked with `-*` after the answer option.
- **User selections** are marked as follows:
  - Selected Correct Answer: `[ * ] -*`
  - Unselected Correct Answer: `[ ] -*`
  - Selected Incorrect Answer: `[ * ] -`
  - Unselected Incorrect Answer: `[ ] -`

### Separation:
- Blank lines are used to separate different questions for clarity and readability.

## Example

### Input Example

Below is an example of the **Smart Exam Format** in plain text:

```
What is 2 + 2? [Image here](https://marinegeo.github.io/assets/img/MarineGEO_logo.png)
[ * ] -* 4
[ ] - 3
[ ] - 5

What is the capital of France? [See Image 1.1](https://assets.digitalocean.com/articles/alligator/boo.svg)
[ * ] -* Paris
[ ] - Berlin
[ ] - Madrid

What is 5 + 5?
[ ] - 9
[ * ] -* 10
[ * ] -* 10
```

### After User Completion Example

If a user completes the exam, their selections would appear like this:

```
What is 2 + 2? [Image here](https://marinegeo.github.io/assets/img/MarineGEO_logo.png)
[ * ] -* 4
[ ] - 3
[ ] - 5

What is the capital of France? [See Image 1.1](https://assets.digitalocean.com/articles/alligator/boo.svg)
[ * ] -* Paris
[ ] - Berlin
[ ] - Madrid

What is 5 + 5?
[ ] - 9
[ * ] -* 10
[ * ] -* 10
```

## Features

- **Correct Answers**: Correct answers are marked with `-*` after the answer option, making it easy to differentiate correct answers from incorrect ones.
- **User Selections**: After the exam, user-selected answers are marked with `[ * ]`, and unselected answers are marked with `[ ]`.
- **Support for Images**: You can include images within the question section using Markdown-style syntax. This allows for richer questions with visual aids or references.
  - Example: `![Alt Text](image-url)` or `[Alt Text](image-url)`
  
  Example with image:
  ```
  What is 2 + 2? [Image here](https://marinegeo.github.io/assets/img/MarineGEO_logo.png)
  [ * ] -* 4
  [ ] - 3
  [ ] - 5
  ```

- **Multiple Correct Answers**: The format supports questions with either single or multiple correct answers.
  
## Notes:

- **Flexibility**: The Smart Exam Format is designed to be flexible, allowing for both human and machine readability. It can be easily parsed by a program while still being understandable to a person reading the file.
- **Blank Line Separation**: Each question is separated by a blank line for clarity, making it easier to distinguish between questions.
- **Customizable**: This format can be customized to include additional information, such as metadata or detailed explanations after each question, as needed.

## Use Cases

The **Smart Exam Format** is ideal for:
- Storing and sharing multiple-choice questions in a lightweight, portable format.
- Processing exam results where both correct answers and user selections need to be represented.
- Importing/exporting questions and answers between systems.
- Creating quizzes with images embedded in the questions to provide visual context or references.

## How to Use

1. Create a new `.txt` file or use any text editor to define your questions and answers in the **Smart Exam Format**.
2. Include images if needed by adding the appropriate Markdown-style image syntax in the question section.
3. Use a program (such as a parser or web application) that can process the format and handle user selections to track responses.

## Example Repository

You can find an example implementation for parsing the **Smart Exam Format** and processing user responses in the provided code within this repository. Feel free to clone this repository, experiment, and contribute improvements!

---

Feel free to reach out if you have any questions or suggestions!
