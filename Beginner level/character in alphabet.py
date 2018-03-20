x=raw_input()
if x.isdigit():
	print "No"
else:
	if (x>='a' and x<='z') or (x>='A' and x<='Z'):
		print "Alphabet"
	else:
		print "No"
