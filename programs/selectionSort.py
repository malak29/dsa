from createList import createList

list, listLenqth = createList()


for i in range(listLenqth):
  	for j in range(i+1, listLenqth):
		  if (list[j] < list[i]):
			  list[i], list[j] = list[j], list [i]

print(list)
print("space complexity: O(1)")
print("Worst Case and Best case: Time complexity is O(n^2) occurs we swap for every innner loop")

		  