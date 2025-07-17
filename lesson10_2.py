with open("example.txt", "r") as file:
    content = file.readlines()
    for line in content:
        print(line)
    # Робота з файлом у межах блоку "with"

print(content)
# Автоматичне закриття файлу поза блоком "with"
