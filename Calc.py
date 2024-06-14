import math

def remove_spaces(string):
    string = string.replace(" ","")
    return string
def check_trigonometry(string):
    for i in range(0,len(string)-3,3):
        a = string[i] + string[i+1] + string[i+2]
        if  a == 'sin':
            string = string.replace("sin","math.sin")
        if  a == 'cos':
            string = string.replace("cos","math.cos")
        if  a == 'tan':
            string = string.replace("tan","math.tan")
        if  a == 'ctg':
            string = string.replace("ctg","math.ctg")
    return string

def check_factorial(string):
    for i in range(0,len(string)-3,3):
        a = string[i] + string[i+1] + string[i+2]
        if a == "fac":
            string = string.replace("fac","math.factorial")
    return string
def parse(string):
    string = remove_spaces(string)
    string = check_trigonometry(string)
    string = check_factorial(string)
    return string

def help():
    print("fac() for factorial \n sin() for sin \n cos() for cos \n tan() for tan \n ctg() for ctg \n for module abs() \n for factorial fac()")
def main():
    print("For help type HELP \n For exit type QUIT")
    while True:
        n = input()
        if n == "HELP":
            help()
        elif n == "QUIT":
            break
        else:
            calc = parse(n)
            try:
                res = eval(calc)
                print(res)
            except:
                print("ERROR:Invalid expression")

main()
#MADE BY YURIY ZAYDOVIY
