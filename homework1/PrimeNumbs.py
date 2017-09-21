# 4. Простые числа
# Напишите программу, которая находит все простые числа между 0 и пользовательским числом.
end = int(input('Введите число, до которого считать простые числа:'))
if end>0 :
	list = []
	for i in range(2,end):
		for j in list:
			if j > int(i**0.5 + 1):
				list.append(i)
				break
			if (i % j == 0):
				break
		else:
			list.append(i)
	print('Список всех простых чисел до заданного числа: ', list)
else:
	print('Введи положительно число!')