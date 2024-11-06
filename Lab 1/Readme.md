# 🎓 Viva Selection Script

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)<img src="https://img.icons8.com/?size=100&id=hGdCwhSHUe6L&format=png&color=000000"/> 
This Python script randomly selects students for viva sessions from a list of student IDs. Once all students have been selected, the list resets, allowing the process to repeat indefinitely. The script demonstrates file I/O, list manipulation, and random selection, along with error handling.

## 📑 Table of Contents
- [Objective](#objective)
- [File Structure](#file-structure)
- [Requirements](#requirements)
- [Setup and Usage](#setup-and-usage)
- [Error Handling](#error-handling)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [Requirements Checklist](#requirements-checklist)

---

## 🎯 Objective
The purpose of this script is to:
1. Familiarize users with file I/O, list manipulation, and basic iteration in Python.
2. Practice error handling and producing structured output with counters.
3. Randomly select students for viva sessions and reset the list when all students have been chosen.

## 🗂️ File Structure

```
├── README.md          # Project documentation
├── student_ids.txt    # Text file containing student IDs (one per line)
└── viva_selection.py  # Python script for viva selection
```

## 📋 Requirements
- **Python 3.x** is required to run this script.

## ⚙️ Setup and Usage

1. **Prepare the student list**: 
    - Create a file named `student_ids.txt` in the same directory as the script.
    - List each student ID on a new line in the format `YYYY-N-MM-xxx`, for example:
      ```
      2022-1-60-145
      2021-3-60-173
      2022-1-60-130
      2022-1-60-135
      ```

2. **Run the script**:
    - Open a terminal or command prompt in the script's directory.
    - Run the script using:
      ```bash
      python viva_selection.py
      ```

3. **Observe the Output**:
    - The script will display each randomly selected student with a "Viva #" counter.
    - When all students have been selected, the list will reset, and selection will start again.

## ⚠️ Error Handling
- If `student_ids.txt` is missing, the script will display an error message: 
  ```
  Error: The file 'student_ids.txt' was not found.
  ```
- If the file is empty, the script will notify you that there are no students to select from.

## 📊 Example Output

Below is an example output from running the script:

```
Viva #1: 2022-1-60-145
Viva #2: 2021-3-60-173
Viva #3: 2022-1-60-130
Viva #4: 2022-1-60-135

All students have been selected. Resetting list...

Viva #1: 2022-1-60-130
Viva #2: 2021-3-60-135
Viva #3: 2022-1-60-145
Viva #4: 2022-1-60-173

All students have been selected. Resetting list...
```

Each "Viva #" line shows the viva number and the selected student ID. After all students have been picked, the list resets, and the process repeats.

## 🤝 Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your improvements.

---

**Note**: This script is designed for demonstration purposes in an educational setting. If you have a large number of students, consider modifying the script to limit the number of resets or allow user input to control the number of rounds.

## ✅ Requirements Checklist

### 📂 File I/O:
- The `load_student_ids` function reads student IDs from a file and handles `FileNotFoundError`.
  - ✅ Works as intended if the file `student_ids.txt` is in the same directory as the script.

### 📋 List Manipulation:
- The function initializes a list of students and then removes each selected student from the list until it's empty.
  - ✅ Works as intended.

### 🎲 Random Selection:
- The code uses `random.choice(student_ids)` to select a random student.
  - ✅ Works as intended.

### 🔄 Iteration and Reset:
- The loop continues until all students are selected, then resets by reloading the list from the file.
  - ✅ Works as intended.

### 🧮 Output Format with Counter:
- The code outputs each selection with a "Viva #" counter.
  - ✅ Works as intended.

### ⚠️ Error Handling:
- Handles `FileNotFoundError` if the file does not exist and prints a meaningful error message.
  - ✅ Works as intended.

## 🧪 Additional Testing Considerations
You may want to verify:
- The script resets properly after all students have been selected.
- The output displays as expected, even with multiple resets.

## 💡 Improvement Suggestions
- **Loop Control**: Currently, the script runs indefinitely. If you want it to stop after a certain number of rounds, you could add a limit.
- **Student ID Validation**: To ensure each ID follows the format `YYYY-N-MM-xxx`, you could add validation when reading from the file.

In summary, yes, the code should work as intended, fulfilling all assignment requirements. It is functional, readable, and appropriately handles errors.