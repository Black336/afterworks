print("Привет! Как тебя зовут?")
name = input()
print("Очень приятно,", name)

print("Сколько тебе лет?")
age = int(input())

if age>10:
  print("Добро пожаловать в игру!")
  print("Я тебе один вопрос задам, какой моб взрывается в игре Minecraft?")
  print("1. Зомби")
  print("2. Скелет")
  print("3. Крипер")
  exmo = input()
  if exmo=="3":
    print("Правильный ответ!")

  if exmo!="3":
    print("Неправильный ответ!")
  
if 10>age:
  print("Ты ещё не дорос для этой игры!")
