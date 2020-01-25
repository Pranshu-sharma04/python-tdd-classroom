def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    return input_list[::-1]

def count_digits(number):
    """
    Return count of digits
    """
    s = str(number)
    count = 0 
    for i in s:
        count+=1
    return count