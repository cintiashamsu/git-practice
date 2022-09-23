# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    sum = 0
    num = 1
    while sum < 1000 and num != 0:
        num = input_int("Enter a number: ")
        sum += num
    return sum
        





if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
