def filter_and_sort_evens(list):
    """Given a list of integers, return a new list containing only the even integers, sorted in ascending order."""
    evens = [number for number in list if number % 2 == 0]
    return sorted(evens)

numbers = [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
result = filter_and_sort_evens(numbers)
print(result)

def count_character_frequency(text):
    """Given a string, return a dictionary where the keys are characters and the values are the number of times each character appears in the string."""
    text = text.lower()
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

text = "This my task for Basic Data Structures & Algorithms"
result = count_character_frequency(text)
print(result)
