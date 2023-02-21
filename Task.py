numbers_div_5=[]
for i in range (0,100):
    if i%5==0 and i>0:
        numbers_div_5.append(i)
        i=i+1
print(numbers_div_5)
numbers_exp_3=[number**3 for number in numbers_div_5]
print(numbers_exp_3)