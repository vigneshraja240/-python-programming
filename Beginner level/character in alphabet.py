x=raw_input()
if x.isdigit():
	print "No"
else:
	if (x>'a' and x<'z') and (x>'A' and x<'z'):
		print "character is in alphabet"
	else:
		print "No"
