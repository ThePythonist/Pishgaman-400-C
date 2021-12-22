lst = ["Sorena", 12, 3.14, True, (), 61, {} ]

def filter(data):

	print(data)

	numbers = []

	for i in data :
		if type(i) == int or type(i) == float :
			numbers.append(i)

	return numbers

print(filter(lst))
input("Press any key to exit : ")
