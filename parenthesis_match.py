# Python3 program for the above approach

# Function to check if 
# parenthesis are balanced
def isBalanced(exp):

	# Initialising Variables
	flag = True
	count = 0

	# Traversing the Expression
	for i in range(len(exp)):
		if (exp[i] == '('):
			count += 1
		else:
			
			# It is a closing parenthesis
			count -= 1

		if (count < 0):

			# This means there are 
			# more closing parenthesis 
			# than opening
			flag = False
			break

	# If count is not zero , 
	# it means there are more 
	# opening parenthesis
	if (count != 0):
		flag = False

	return flag

# Driver code
if __name__ == '__main__':
	

	exp1 = "((()))()()"

	if (isBalanced(exp1)):
		print("Balanced")
	else:
		print("Not Balanced")

	exp2 = "())((())"

	if (isBalanced(exp2)):
		print("Balanced")
	else:
		print("Not Balanced")

# This code is contributed by himanshu77
