#Определить, сколько раз в тексте встречается заданное слово.

#По методичке

text = input("Введите текст: ")
word = input("Введите слово: ")

current = ""    
count = 0       

for ch in text:
    if ch != ' ':
        current += ch
    else:
        if current == word:
            count += 1
        current = ""

if current == word:
    count += 1

print("Слово встречается", count, "раз(а)")

#Более комфортный вариант 
text = input("Введите текст: ")
word = input("Введите слово: ")

words = text.split()
count = words.count(word)

print("Слово встречается", count, "раз(а)")
