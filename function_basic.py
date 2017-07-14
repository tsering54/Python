def odd_even(n):
    for i in range(1, n+1):
        if i%2==0:
            print i, ' This is an even number.'
        else:
            print i, ' This is an odd number.'

y=odd_even(2000)
print y


#Create a function called odd_even that counts from 1 to 2000.
#As your loop executes have your program print the number of that iteration and
#specify whether it's an odd or even number.

def multiply(arr,num):
    for i in range(len(arr)):
        arr[i] = arr[i]* num
    return arr

a = [2,4,10,16]
b = multiply(a,5)
print b

def layered_multiples(arr):
    print arr
    new_array = []
    for i in arr:
        val_arr = []
        for j in range(0,i):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
