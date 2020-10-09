'''
Python code to implement factorial of a number
'''

def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n*factorial(n-1)

def main():
	n = int(input("Enter a number: "))
	f = factorial(n)
	print("Factorial of",n,"is",f)

if __name__ == '__main__':
	main()