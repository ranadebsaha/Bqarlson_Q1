def removeP(Str):
	str = ""
	n = 0
	for i in Str:
		if (i == '(' and n > 0):
			str += i
		if (i == '('):
			n += 1
		if (i == ')' and n > 1):
			str += i	
		if (i == ')'):
		    n -= 1
	return str

if __name__ == '__main__':
	Str =input("Enter a String")
	print(removeP(Str))

