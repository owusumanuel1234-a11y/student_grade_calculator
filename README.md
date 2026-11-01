# Student Grade Calculator

A simple Python application that collects a student's name and subject scores, validates the scores, calculates academic results, and assigns a grade based on the student's average.

## Features

- Accepts a student's name.
- Prevents the user from submitting an empty name.
- Accepts Mathematics, Science, and English scores.
- Converts scores into numeric values.
- Validates that each score is between 0 and 100.
- Calculates the student's total score.
- Calculates the average score.
- Assigns a letter grade based on the average.
- Handles non-numeric score input using exception handling.
- Displays a formatted student result report.

## Technologies Used

- **Python 3**
- Python built-in functions
- Conditional statements
- While loops
- Exception handling
- Input validation

## Grading System

The current grading conditions in the program are:

| Average score | Grade | Status |
|---|---|---|
| Above 80 | A |Excellent|
| Above 70 | B |Very Good|
| Above 60 | C |  Good   |   
| Above 50 | D |  Poor   | 
| 50 or below | F | fail |

*Note: The current conditions use strict greater-than comparisons. Exact boundary scores should be reviewed before treating this as a final grading policy.*

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Clone this repository:

   ```bash
   git clone https://github.com/owusumanuel1234-a11y/student_grade_calculator.git
   ```

3. Navigate into the project folder:

   ```bash
   cd student_grade_calculator
   ```

4. Run the application:

   ```bash
   python grade_calculator.py
   ```

## Example Output

```text
Welcome to Student Grade Calculator.

Enter name: Emmanuel
Enter Mathematics score: 85
Enter Science score: 78
Enter english score: 90

=== student information ===
Student name: Emmanuel
Mathematics score: 85.00
Science score: 78.00
English score: 90.00
Total score: 253.00
Average score: 84.33
Grade: A
Status: Excellent
```

## Project Structure

```text
student_grade_calculator/
│
├── grade_calculator.py
├── README.md
└── .gitignore
```

## Future Improvements

- Allow users to enter more subjects.
- Improve validation by allowing incorrect scores to be re-entered.
- Add a pass/fail result.
- Improve the grading system and its boundary conditions.
- Support calculating results for multiple students.
- Organise the program using functions and classes.

## Author

**Owusu Emmanuel Kuffor**

Computer Science Student | Python Learner

## Project Purpose

This project is part of my practical Python programming journey. It helps me strengthen my understanding of input handling, conditional statements, loops, arithmetic operations, validation, and exception handling.

