
# AI Generated Questions Examples

This guide explains how to use a manual prompt generation process to create AI-generated questions without relying on API calls. 
This is useful for users who want to manually generate prompts for input into generic AI tools like ChatGPT, Copilot, or Google Gemini.

## Process Overview

1. **Prepare Your SEF Exam Result**:
   Start with the output of a completed exam in the Smart Exam Format (SEF), highlighting user responses to each question.

2. **Generate Instructions for the AI Tool**:
   Use a manual instruction generation process to format the SEF results as a prompt. Follow the format provided below for a ready-to-use prompt that can be copied and pasted into a generic AI tool.

3. **Structure Your Prompt for AI Input**:
   The AI will generate new questions based on missed topics or areas that need reinforcement, as specified in the prompt.

## Example Prompt Template

Here is an example of a prompt template based on the SEF exam output, which you can adapt for your AI tool.

---

**Prompt Template for Generating New Smart Exam Questions**:

Create a new exam based on the Smart Exam Format, using the information provided below.

### Smart Exam Format:
The Smart Exam Format is a structured way to represent multiple-choice questions and answers in plain text. The format is designed to handle both questions and user responses, following these rules:

**Questions**:
- Each question starts with the question text.
- Any line that does not start with a hyphen (-) or bracket ([ ]) and is not blank is considered a new question.

**Answers**:
- Each answer option starts with a hyphen (-), indicating it is an answer.
- Correct answers are marked with a hyphen followed by an asterisk (-*).
- If the exam has been executed by a user, the user-selected answers will be marked with [ * ] before the hyphen (- or -*), while unselected answers are marked with [ ].

**Answer Markings**:
- Correct answers are always marked with -*.
- The format supports both single and multiple correct answers.
- User selections are marked as follows:
  - Selected Correct Answer: [ * ] -* 
  - Unselected Correct Answer: [ ] -* 
  - Selected Incorrect Answer: [ * ] - 
  - Unselected Incorrect Answer: [ ] - 

**Separation**:
- Blank lines are used to separate different questions.

**Example**:
\```
What is 2 + 2?
[ * ] -* 4
[ ] - 3
[ ] - 5

What is the capital of France?
[ * ] -* Paris
[ ] - Berlin
[ ] - Madrid
\```

### Previous Exam:
Below is the previous exam to use as input for creating a new exam:

\```
What is 2 + 2?
[ * ] -* 4
[ ] - 3
[ ] - 5

What is the capital of France?
[ * ] -* Paris
[ ] - Berlin
[ ] - Madrid

What is 5 + 5?
[ * ] - 9
[ ] -* 10
[ ] - 11
\```

### Instructions:
- Please create a new Smart Exam without any other output in text format.
- Ensure that the output exam follows the Smart Exam Format, with each answer on its own line starting with a "- " and the correct answer marked with "-* ".
- Do not include brackets [] in this new exam, as they are only used to reference user selections.

Format the output as markdown.

---

## Notes
- This prompt template is designed to be copied directly into an AI tool for creating a new set of questions.
- The process uses plain text without API calls, making it suitable for manual operations.

---
