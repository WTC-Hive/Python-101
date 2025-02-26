# Task 1
def get_user_info():
    """
    Ask the user for their name, age, and favorite color.
    Return a dictionary with the following structure:
    {
        "name": <user's name>,
        "age": <user's age>,
        "favorite_color": <user's favorite color>
    }
    """
    return {
        "name": input("Enter your name: "),
        "age": input("Enter your age: "),
        "favorite_color": input("Enter your favorite color: ")
    }

# Task 2
def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) using the formula:
    BMI = weight (kg) / (height (m) ** 2)
    Return the BMI rounded to 2 decimal places.
    """
    return round(weight / (height ** 2), 2)

# Task 3
def create_shopping_list(items:list):
    """
    Given a list of items, create a shopping list.
    Return a dictionary where the keys are the items and the values are the quantities (default to 1).
    Example:
    Input: ["apple", "banana", "apple"]
    Output: {"apple": 2, "banana": 1}
    """
    return {item: items.count(item) for item in items}

# Task 4
def count_word_frequency(text:str):
    """
    Given a string, count the frequency of each word.
    Return a dictionary where the keys are the words and the values are their frequencies.
    Example:
    Input: "hello world hello"
    Output: {"hello": 2, "world": 1}
    """
    return {word: text.split().count(word) for word in text.split()}


# Task 5
def check_number(num):
    """
    Given a number, return:
    - "Positive" if the number is greater than 0.
    - "Negative" if the number is less than 0.
    - "Zero" if the number is 0.
    """
    return "Positive" if num > 0 else "Negative" if num < 0 else "Zero"

# Task 6
def sum_even_numbers(numbers):
    """
    Given a list of numbers, return the sum of all even numbers.
    """
    return sum(num for num in numbers if num % 2 == 0)

# Task 7
def find_first_negative(numbers):
    """
    Given a list of numbers, use a while loop to find the first negative number.
    Return the first negative number or None if there are no negative numbers.
    """
    n = 0
    while n < len(numbers):
        if numbers[n] < 0:
            return numbers[n]
        n += 1
    return None

# Task 8
def analyze_text(text:str):
    """
    Given a string, perform the following tasks:
    1. Count the number of words.
    2. Count the number of vowels (a, e, i, o, u).
    3. Return a dictionary with the results.
    Example:
    Input: "Hello world"
    Output: {"word_count": 2, "vowel_count": 3}
    """
    return {"word_count": len(text.split()),
            "vowel_count": sum(text.count(vowel) for vowel in ("a", "e", "i", "o", "u"))}
