def addnumber(num):
    print("addnumber")
    print("this is a add number funtion")
def totalnum(num1,num2,num3,num4):
    addnumber=num1+num2+num3+num4
    return addnumber
result=totalnum(2,3,2,2)
print(result)

def subtractnumber(num):
    print("subtarctnumber")
    print("this is a subtract number funtion")
def totalnum(num1,num2,num3,num4):
    subtractnumber=num1-num2-num3-num4
    return subtractnumber
result=totalnum(2,3,2,2)
print(result)

def multiplenumber(num):
    print("multiplenumber")
    print("this is a multiple number funtion")
def totalnum(num1,num2,num3,num4):
    multiplenumber=num1*num2*num3*num4
    return multiplenumber
result=totalnum(2,3,2,2)
print(result)

def dividenumber(num):
    print("dividenumber")
    print("this is a divide number funtion")
def totalnum(num1,num2,num3,num4):
    dividenumber=num1/num2/num3/num4
    return dividenumber
result=totalnum(2,3,2,2)
print(result)


def is_perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n


print(is_perfect(28))
print(is_perfect(6))
print(is_perfect(10))

def prime_factors(n):
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors
print(prime_factors(60))




