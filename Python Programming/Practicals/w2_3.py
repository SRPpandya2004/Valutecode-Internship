
# List Manipulation – Square Each Number

def square_list(numbers):
    return [x ** 2 for x in numbers]

# Example usage
nums = [1, 2, 3, 4, 5]
squared = square_list(nums)
print("Original list:", nums)
print("Squared list:", squared)
