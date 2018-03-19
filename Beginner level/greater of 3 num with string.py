a=raw_input()
b=raw_input()
c=raw_input()
if a.isdigit() and b.isdigit() and c.isdigit():
	if(a>b and a>c):
		print a
	elif(b>c and b>c):
		print b
	elif(c>a and c>a):
		print c
else:
	print"invalid"
