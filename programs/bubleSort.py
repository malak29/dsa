from createList import createList

list, listLenqth = createList()

for i in range(listLenqth):
  	for j in range(0, listLenqth-i-1):
  		if list[j] > list[j+1]:
			  list[j], list[j+1] = list[j+1], list[j]

print(list)
print("space complexity: O(1)")
print("Best Case: Time complexity is O(n); occurs when the array is already sorted.")
print("Worst Case: Time complexity is O(n^2) occurs when the array is sorted in reverse order.")

