def sum(a,b):
    print(a+b)
print('hello')
a=input("enter first digit \n")
b=input("enter second digit \n")
print("Total sum is :")
sum(a,b)
print("hello")
#Passing value to positional function

def pos_fun(a,b):
    print(a+b)
pos_fun(b=3,a=22)

#function having default values

def def_val(a=2,b=2):
    print(a+b)

def_val(3)
def_val(b=22)

#arbitary argument
def pizza(types,size,*toping):
    print(f"hello {types}")
    #print(f"your pizza of {types}, type of size {size} is ready with toping of {toping} is ready")

pizza("chicken","XL","extra cheese","Olives")
print("I dont know the version of python I am using")