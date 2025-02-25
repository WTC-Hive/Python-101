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
    return {"name": input("Name: "), "age": input("Age: "), "favorite_color": input("Favorite color: ")}

def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) using the formula:
    BMI = weight (kg) / (height (m) ** 2)
    Return the BMI rounded to 2 decimal places.
    """
    return round((weight / height ** 2), 2)

def create_shopping_list(items):
    """
    Given a list of items, create a shopping list.
    Return a dictionary where the keys are the items and the values are the quantities (default to 1).
    Example:
    Input: ["apple", "banana", "apple"]
    Output: {"apple": 2, "banana": 1}
    """
    return {x: items.count(x) for x in items}

def count_word_frequency(text):
    """
    Given a string, count the frequency of each word.
    Return a dictionary where the keys are the words and the values are their frequencies.
    Example:
    Input: "hello world hello"
    Output: {"hello": 2, "world": 1}
    """
    return {x: text.split().count(x) for x in text.split()}

def check_number(num):
    """
    Given a number, return:
    - "Positive" if the number is greater than 0.
    - "Negative" if the number is less than 0.
    - "Zero" if the number is 0.
    """
    return 'Positive' if num > 0 else 'Negative' if num < 0 else 'Zero'

def sum_even_numbers(numbers):
    """
    Given a list of numbers, return the sum of all even numbers.
    """
    return sum([x for x in numbers if x % 2 == 0])

def find_first_negative(numbers):
    """
    Given a list of numbers, use a while loop to find the first negative number.
    Return the first negative number or None if there are no negative numbers.
    """
    return next(iter([number for number in numbers if number < 0]), None)

def analyze_text(text):
    """
    Given a string, perform the following tasks:
    1. Count the number of words.
    2. Count the number of vowels (a, e, i, o, u).
    3. Return a dictionary with the results.
    Example:
    Input: "Hello world"
    Output: {"word_count": 2, "vowel_count": 3}
    """
    return {'word_count': len(text.split()), 'vowel_count': len([char for char in text if char.lower() in ['a', 'e', 'i', 'o', 'u']])}
