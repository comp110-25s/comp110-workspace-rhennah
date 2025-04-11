"""Exercise 03"""

__author__: str = "730470881"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values in a given dictionary"""
    output_dict: dict[str, str] = {}

    for key in input_dict:  # Looping through the original dictionary one by one
        value = input_dict[key]

        if (
            value in output_dict
        ):  # Checking to see if the value is already a key in the output dictionary
            raise KeyError("Duplicate values detected. Cannot invert dictionary.")

        output_dict[value] = key  # Swapping the values

    return output_dict


def count(my_list: list[str]) -> dict[str, int]:
    """Counting the number of each item in a list"""
    count_dict: dict[str, int] = {}

    for item in my_list:  # Looping through list items
        if item in count_dict:  # If it's already in the dictionary, add 1
            count_dict[item] += 1
        else:  # If it's the first time we see it, initialize with 1
            count_dict[item] = 1

    return count_dict


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Finding the most frequent favorite color out of everyone"""
    color_count = count(list(names_and_colors.values()))

    most_frequent_color = ""
    max_count = 0

    for color in names_and_colors.values():  # Assigns the values to "color"
        if color_count[color] > max_count:  # If the color is greater than max_count
            most_frequent_color = color  # Udpdate most frequent color
            max_count = color_count[color]  # And update max count

    return most_frequent_color


def bin_len(words_list: list[str]) -> dict[int, set[str]]:
    result: dict[int, set[str]] = {}

    for word in words_list:  # Looping through each word
        length: int = len(word)  # Gathering its length

        if length in result:
            result[length].add(word)  # Adding word to existing set if number exists
        else:
            result[length] = {word}  # Creating a new set otherwise

    return result
