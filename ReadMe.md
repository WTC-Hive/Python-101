# Python Basics Project

Welcome to the Python Basics Project! In this project, you will practice working with **user inputs, variables, data types, data structures, if/else statements, and for/while loops**.

## Instructions

1. **Fork the Repository**:  
   - Click the "Fork" button on the top right of this repository to create your own copy.

2. **Clone Your Fork**:  
   - Clone your forked repository to your local machine:  
     ```bash
     git clone https://github.com/YOUR_USERNAME/Python-101.git
     ```

3. **Create a Branch**:  
   - Create a branch with your name (e.g., `Monwabisi`):  
     ```bash
     git checkout -b YOUR_NAME
     ```

4. **Complete the Tasks**:  
   - Open `tasks.py` and implement the functions as described in the docstrings.  
   - Test your implementation using the provided unit tests.

5. **Run the Tests**:  
   - Install `pytest` if you don't have it:  
     ```bash
     pip install pytest
     ```
   - Run the tests:  
     ```bash
     pytest test_tasks.py
     ```

6. **Commit and Push Your Changes**:  
   - Add your changes:  
     ```bash
     git add tasks.py
     ```
   - Commit your changes:  
     ```bash
     git commit -m "Completed tasks"
     ```
   - Push your changes to your branch:  
     ```bash
     git push origin YOUR_NAME
     ```

7. **Submit a Pull Request**:  
   - Go to your forked repository on GitHub and click "New Pull Request".  
   - Select your branch (`YOUR_NAME`) and submit the pull request to the main repository.

## Tasks Overview

### Task 1: User Input and Variables
- Ask the user for their name, age, and favorite color.  
- Return a dictionary with the collected information.

### Task 2: Data Types and Variables
- Calculate the Body Mass Index (BMI) using weight and height.  
- Return the BMI rounded to 2 decimal places.

### Task 3: Data Structures (Lists)
- Create a shopping list from a list of items.  
- Return a dictionary with items as keys and quantities as values.

### Task 4: Data Structures (Dictionaries)
- Count the frequency of each word in a string.  
- Return a dictionary with words as keys and frequencies as values.

### Task 5: If/Else Statements
- Check if a number is positive, negative, or zero.  
- Return the appropriate string.

### Task 6: For Loops
- Sum all even numbers in a list.  
- Return the sum.

### Task 7: While Loops
- Find the first negative number in a list.  
- Return the first negative number or `None` if there are no negative numbers.

### Task 8: Combined Concepts
- Analyze a string to count the number of words and vowels.  
- Return a dictionary with the results.

## Running Tests

To run the tests, use the following command:  
```bash
pytest test_tasks.py
