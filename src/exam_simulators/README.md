
# Smart Exam Format - Exam Simulator

This `exam_simulator` folder contains an interactive HTML-based simulator for the **Smart Exam Format (SEF)**. This simulator provides a basic interface for loading and taking exams formatted in SEF, allowing users to view results, focus on incorrect answers, and save or copy the exam output in the specified format.

## About the Smart Exam Format

The **Smart Exam Format** is a structured, plain-text format for creating multiple-choice exams. It supports questions, correct answers, user selections, and embedded images, all using a simple syntax for readability and machine processing.

For full details on the SEF syntax and format, visit the main repository [here](https://github.com/yllemo/Smart-Exam-Format).

## Features

- **Load SEF Exams:** Upload `.txt` files formatted in SEF to take exams interactively.
- **Track Progress and Score:** Users can navigate between questions, track correct answers, and view final results.
- **Result Output:** Generate exam results with correct answers and user selections clearly marked in brackets.
- **Save or Copy Results:** Easily save the result output as a `.txt` file or copy it to the clipboard.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yllemo/Smart-Exam-Format
   ```
   
2. **Open the Simulator**:
   - Navigate to `exam_simulator/SEF_Basic_Exam_Simulator.html`.
   - Open the HTML file in a modern browser to access the simulator interface.

3. **Using the Simulator**:
   - Click **"Choose File"** to upload an SEF-formatted `.txt` exam file.
   - Navigate through questions with **Previous** and **Next** buttons.
   - Once completed, click **End Exam** to view your score and generate the result output.
   - Use **Copy to Clipboard** or **Save Result** to export your results.

## Example SEF File Format

Below is an example SEF file for reference:

```plaintext
What is 2 + 2?
- 3
-* 4
- 5

What is the capital of France?
-* Paris
- Rome
- Madrid
```

## Feedback and Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve the simulator and expand functionality for the SEF.

