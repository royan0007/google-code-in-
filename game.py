board = [ [],
	['A', 'F', 'K', 'P', 'U', 'Z'],
	['B', 'G', 'L', 'Q', 'V'],
	['C', 'H', 'M', 'R', 'W'],
	['D', 'I', 'N', 'S', 'X'],
	['E', 'J', 'O', 'T', 'Y']]


for i in range(1, 6):
	print(i, end=' ')
	temp = ' '.join(board[i])
	print(temp)

n = input("Enter the numbers: ")

print("1 2 3 4 5 6")
for letter in n:
	temp = int(letter)
	print(' '.join(board[temp]))


m = input("Enter the numbers: ")

i = 0

final = ""

for letter in m:
	final += board[int(n[i])][int(letter)-1]
	i += 1

print(final)