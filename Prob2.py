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
    
    return True

small = [[8,1,6],[3,5,7],[4,9,2]]
medium = [[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]]
large = [[35,1,6,26,19,24],[3,32,7,21,23,25],[31,9,2,22,27,20],[8,28,33,17,10,15],[30,5,34,12,14,16],[4,36,29,13,18,11]]
error = [[1,2],[3,4,5]]
print(is_magic_square(small))
print(is_magic_square(medium))
print(is_magic_square(large))
print(is_magic_square(error))
