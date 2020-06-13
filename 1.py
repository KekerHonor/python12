def add_list(numbers: list = [], number: int = -999):
    try:
        numbers.append(number)
    except AttributeError:
        numbers = []
        numbers.append(number)
    return numbers
nums = [1,2,3]
new = add_list(nums, 4)
print(new)