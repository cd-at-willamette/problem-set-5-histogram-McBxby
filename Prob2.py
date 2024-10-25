##################################################
# Name: Myles Crandall
# Collaborators: n/a
# Estimate of time spent (hr): 2.5
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    n = len(array)
    if not array or n != len(array[0]):
        return False
    
    # Calculate the expected sum (sum of first row)
    expected_sum = sum(array[0])
    
    # Check rows
    for row in array:
        if sum(row) != expected_sum:
            return False
    
    # Check columns
    for col in range(n):
        if sum(array[row][col] for row in range(n)) != expected_sum:
            return False
    
    # Check diagonals
    if sum(array[i][i] for i in range(n)) != expected_sum or sum(array[i][n-1-i] for i in range(n)) != expected_sum:
        return False
    
    # Create a list of all numbers in the array
    array_list = []
    for row in array:
        for num in row:
            array_list.append(num)
    
    # Check if all numbers are unique
    unique_numbers = []
    for num in array_list:
        if num not in unique_numbers:
            unique_numbers.append(num)
    if len(unique_numbers) != n * n:       
        return False
    
    # Check if all numbers are between 1 and n * n
    for num in array_list:
        if num < 1 or num > n * n:
            return False
    
    return True

small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))
