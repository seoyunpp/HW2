# get two integer parameters
# return sum

def plus(x, y):
    return x+y
def minus(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus, 2: minus, 3: multiply 4: division")
        check = int(input())
        if check == 1: 
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", plus(x,y))
        elif check == 2:
		print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", minus(x,y))
	  elif check == 3:
		print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", multiply(x,y))
	  elif check == 4:
		print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", division(x,y))
            
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
