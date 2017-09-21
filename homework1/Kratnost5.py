# 5. Кратные пяти
# Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами.
Numbs = input('Введите два числа через пробел:').split(' ')
# Следующий иф не требуется, если числа записаны в порядке возрастания
if int(Numbs[0]) > int(Numbs[1]):
	maxnumb = int(Numbs[0])
	minnumb = int(Numbs[1])
else:
	maxnumb = int(Numbs[1])
	minnumb = int(Numbs[0])
i = minnumb
while i % 5 != 0:
    i= i - 1
list = []
for j in range(i+5,maxnumb,5):
    list.append(j)
#Тоже самое можно было сделать через while
#while i<(maxnumb-5):
#    i= i+5
#    list.append(i)
print ('Числа кратные 5 в заданном диапоне: ',list)

# А так же вариант тупого перебора:
#Numbs = input('Введите два числа через пробел:').split(' ')
#list = []
#for i in range(int(Numbs[0]), int(Numbs[1])):
#    if i%5==0:
#        list.append(i)
#print(list)

# Да, мне было скучно)