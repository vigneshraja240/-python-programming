x=raw_input()
y=['a','e','i','o','u','A','E','I','O','U']
if x.isdigit():
	print "enter a valid letter"
else:
	if (x in y):
		print "Vowel"
	else:
		print "Consonant"

