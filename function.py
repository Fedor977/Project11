# файлы бывают: текстовые, бинарные

# чтение r
# запись w
# дозапись a

# чтение rb
# запись wb

# open(путь_до_файла, режим_работы, кодировка="UTF-8") - открывает файл на указанный режим
# пусть_до_файла
# 1 абсолютный путь
# 2 относительный путь

file = open("byron.txt", mode="r", encoding="utf-8")
# .read() - считывает весь текст из файла
# .readlines() - считает каждую строку сформировав список строк (выдает результат в виде списка)
# .readline() - считывает каждую строку по очереди ()
text = file.read() #получаем текст, что хранится в файле
file.close()
print(text)

file = open("byron.txt", mode="r", encoding="utf-8")
text = file.readlines()
file.close()
print(text)

file = open("byron.txt", mode="r", encoding="utf-8")
text = file.readline()
print(text)
file.close()

#работа с бинарными файлами
img = open('nature.jpg', mode="rb")
contact = img.read()
print()
img.close()

file2 = open('new_file.txt', mode="w", encoding="utf-8")
# .write() - записывает текст в одну строчку
# .writelines(список_строк) - принимает список строк и записывает в файл
file2.write('Hello world')
file2.write('Привет мир')
file2.close()

with open('nature.jpg', mode="rb") as img:
  content = img.read()
  for i in range(1, 11):
    new_img = open(f'{i}.jpg', mode='wb')
    new_img.write(content)
    new_img.close()
  print(img.closed)

print(img.closed)

file2 = open('new_file.txt', mode='a', encoding='utf-8')
lines = [f'{i} строка']

