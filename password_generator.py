#1st type:

"""import string
import random
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
passw = []
n = int(input("please enter the length of your password:"))
passw.extend(list(s1))
passw.extend(list(s2))
passw.extend(list(s3))
passw.extend(list(s4))

print("Your password is:")
print("".join(random.sample(passw, n)))"""






"""import random
s = 'asd463fghOPIUYQWEj40512klpoiuyCV!@#$%^&*()_+~<>?/\|{]{[BNM789ZXASDFGHJKLtrewqzRTxcvbnm'
n = int(input("please enter the length of your password:"))
pssw=[]
pssw.extend(s)
print("Your password is:")
print("".join(random.sample(pssw, n)))"""


#2nd type


import random
lst1 = 'UIOPHJKLYTREWQGFDSAZXCVBNM'
lst2 = 'lkjhgfdsapoiuytrewqzxcvbnm'
lst3 = '4569871230'
lst4 = '&^%$#@!*()}{:"|?><]['
list1= []
list2= []
list3= []
list4= []

list1.extend(list(lst1))
list2.extend(list(lst2))
list3.extend(list(lst3))
list4.extend(list(lst4))


n1= int(input("How many upper_case letter do you want in your password:"))
n2= int(input("how many lower_case letter do you want in your password:"))
n3= int(input("how many digits do you want in your password:"))
n4= int(input("how many symbols do you want in your password:"))


n_1 = random.sample(list1, n1)
n_2  = random.sample(list2, n2)
n_3 = random.sample(list3, n3)
n_4  = random.sample(list4, n4)
n = n1+n2+n3+n4
passw =[]
passw.extend(list(n_1))
passw.extend(list(n_2))
passw.extend(list(n_3))
passw.extend(list(n_4))
print("Your password is:")
print("".join(random.sample(passw ,n)))









