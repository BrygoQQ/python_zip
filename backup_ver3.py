import os
import time

# 1. Файлы и каталоги, который необходимо скопировать, собираются в список.
source = ["/Users/aleksandrkirusin/Documents/STUDY/python/books", "/Users/aleksandrkirusin/Documents/STUDY/python/study/lessons"]
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = "/Users/aleksandrkirusin/Documents/STUDY/python/резерв" # Подставьте тот путь, который вы будете использовать

# 3. Файлы помещатся в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime("%Y-%m-%d")

# Именем для zip-архива служит текущая дата и время.
now = time.strftime("%H-%M-%S")

# Запрашиваем комментарий пользователя для имени файла
comment = input("Введите комментарий --> ")
if len(comment) == 0: # Проверяем, введен ли комментарий
    taget = target = today + os.sep + now + ".zip"
else:
    target = today + os.sep + now + "_" +\
    comment.replace(" ", "_") + ".zip"

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # Создание каталога
print("Каталог успешно создан", today)

# Имя zip-файла


# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, " ".join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print("Резервная копия успешно создана в", target)
else:
    print("Создание резервной копии НЕ УДАЛОСЬ")