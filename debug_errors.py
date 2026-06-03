def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
   #The error occurs when calling: calculate_average(data3)
    #because data3 is an empty list.
    #This causes len(numbers) to be 0, so the function attempts to divide by zero: total / 0 
    #which results in a ZeroDivisionError.
    try:
        return total / len(numbers)
    except ZeroDivisionError:
        return None  # Return None for empty list to indicate no average can be calculated

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] 
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")


def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")
        return None  # Return None if index is out of range
    except TypeError:
        print(f"Error: Provided {my_list} is not a list.")
        return None  # Return None if the input is not a list


print(get_list_element([10, 20, 30], 0))
print(get_list_element([10, 20, 30], 5))
print(get_list_element(855, 1))