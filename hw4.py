# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.


n=(int(input("Введите кол-во элементов первого множества N: ")))
num_list_1=[]
for i in range(n):
    num = int(input("Введите num "))
    num_list_1.append(num)


m=(int(input("Введите кол-во элементов первого множества M: ")))
num_list_2 = []
for i in range(m):
    num = int(input("Введите num "))
    num_list_2.append(num)


num_list3 = num_list_1+num_list_2

for i in set(num_list3):
    if num_list3.count(i) > 1:
        print(i)