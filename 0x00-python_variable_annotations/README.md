# 0x00. Python - Variable Annotations

This project focuses on the concept of "Advanced Python" and aims to improve understanding of type annotations in Python 3. It covers topics such as specifying function signatures and variable types using type annotations, duck typing, and code validation with mypy.
The project has several tasks, each with specific requirements and implementation details:

## Tasks

### Task 0: Basic annotations - add

Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float. 
File: [0-add.py](./0-add.py)

### Task 1: Basic annotations - concat 

Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string.
File: [1-concat.py](./1-concat.py)

### Task 2: Basic annotations - floor

Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.
File: [2-floor.py](./2-floor.py)

### Task 3: Basic annotations - to string

Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.
File: [3-to_str.py](./3-to_str.py)

### Task 4: Define variables

Define and annotate the following variables with the specified values:
  - a, an integer with a value of 1
  - pi, a float with a value of 3.14
  - i_understand_annotations, a boolean with a value of True
  - school, a string with a value of “Holberton”
File: [4-define_variables.py](./4-define_variables.py)

### Task 5: Complex types - list of floats

Write a type-annotated function sum_list that takes a list input_list of floats as argument and returns their sum as a float.
File: [5-sum_list.py](./5-sum_list.py)

### Task 6: Complex types - mixed list

Write a type-annotated function sum_mixed_list that takes a list mxd_lst of integers and floats and returns their sum as a float.
File: [6-sum_mixed_list.py](./6-sum_mixed_list.py)

### Task 7: Complex types - string and int/float to tuple

Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.
File: [7-to_kv.py](./7-to_kv.py)

### Task 8: Complex types - functions

Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
File: [8-make_multiplier.py](./8-make_multiplier.py)

### Task 9: Let's duck type an iterable object

Annotate the below function’s parameters and return values with the appropriate types
```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```
File: [9-element_length.py](./9-element_length.py)

### Task 10: Duck typing - first element of a sequence

Augment the following code with the correct duck-typed annotations:
```python
# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
```
File: [100-safe_first_element.py](./100-safe_first_element.py)

### Task 11: More involved type annotations

Given the parameters and the return values, add type annotations to the function
Hint: look into TypeVar
```python
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
```
File: [101-safely_get_value.py](./101-safely_get_value.py)

### Task 12: Type Checking

Use mypy to validate the following piece of code and apply any necessary changes.
```python
def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
```
File: [102-type_checking.py](./102-type_checking.py)

## Resources

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](../LICENSE).
