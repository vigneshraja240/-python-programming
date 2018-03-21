a=raw_input()
if a.isdigit():
	if((int(a)%4==0) and ((int(a)%100!=0) or (int(a)%400==0))):
		print"yes"
	else:
		print"no"	
else:
	print"Invalid Input"

