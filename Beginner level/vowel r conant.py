x=raw_input()
y=['a','e','i','o','u','A','E','I','O','U']
if x.isdigit():
	print "Invalid Input"
else:
	if (x in y):
		print "Vowel"
	else:
		print "Consonant"

