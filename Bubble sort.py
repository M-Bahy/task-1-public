# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 19:04:53 2022

@author: mohamed
"""
List = [90, 100, 20, 270, 0, 50, 650]
maxInndex = 7
n = maxInndex - 1
Index = 0

while True:
	Flag = False
	Index += 1
	for j in range(n):
		if (List[j] > List[j]):
			List[j],List[j+1] = List[j+1],List[j]
			Flag = False
	n -= 1
	if (Flag == False or Index >= maxInndex):
		break

for i in range(7):
	print(List[i])



print("hello world")