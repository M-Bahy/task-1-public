List = [90, 100, 20, 270, 0, 50, 650]
maxIndex = 7
n = maxIndex - 1
Index = 0

while True:
	Flag = False
	Index += 1
	for j in range(n):
		if (List[j] > List[j+1]):
			List[j],List[j+1] = List[j+1],List[j]
			Flag = True
	n -= 1
	if (Flag == False or Index >= maxIndex):
		break

for i in range(7):
	print(List[i])

List = [90, 100, 20, 270, 0, 50, 650]
maxIndex = 7
n = maxIndex - 1
Index = 0

while True:
	Flag = False
	Index += 1
	for j in range(n):
		if (List[j] > List[j+1]):
			List[j],List[j+1] = List[j+1],List[j]
			Flag = True
	n -= 1
	if (Flag == False or Index >= maxIndex):
		break

for i in range(7):
	print(List[i])



print("hello world")