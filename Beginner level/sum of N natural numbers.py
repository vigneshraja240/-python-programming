a=raw_input()
sum=0
if a.isdigit():
	for i in range(1,int(a)+1):
		sum+=i
	print sum
else:
	print"invalid input"
