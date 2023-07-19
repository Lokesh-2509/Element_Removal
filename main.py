"""numbers = list(map(int, input().split()))
numbers.sort()
total_cost = 0
for i in range(len(numbers)):
    total_cost += sum(numbers[:i + 1])
    current_sum = sum(numbers[:i + 1])
print(total_cost)"""

"""Elements Removal
Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.
Find the minimum cost to remove all elements from the array.
Example Input
Input 1:
A = [2, 1]
Input 2:
A = [5]
Example Output
Output 1:
4
Output 2:
5"""

def minimum_cost_to_remove(A):
    A.sort()
    total_cost = 0
    for i in range(len(A)):
        total_cost += sum(A[:i + 1])
    return total_cost
A = list(map(int, input("Enter the elements of the array (space-separated): ").split()))

output = minimum_cost_to_remove(A)
print("Output:", output)
