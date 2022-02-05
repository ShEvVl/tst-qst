# Сontent viewing service

Задача описана в `test_specs.docx`

Загрузка необходимых библиотек:
```shell
pip install -r requirements.txt
```
Генерация csv файла и изображений:
```shell
img_info_generator.py
```
Запуск сервера :
```shell
python main.py 
```
Пример запроса :
```shell
http://localhost:8080/?category[]=city&category[]=apple
```
Существующие категории :
```shell
'apple', 'banana', 'city', 'drill', 'ear', 'forest', 'gim', 'hill', 'ink', 'juice', 'koala', 'lion', 'mouse', 'notebook', 'octopus', 'panda', 'queen', 'rabbit', 'sun', 'tea'
```

Запуск сервера с пользовательским интерфейсом:
```shell
python main_ui.py 
```
адресс сервера `http://localhost:8080`

Тестовые изображения генерируются и размечаются с помощью исполняемого файла `img_info_generator.py`, их описание указано в файле `info.csv`. `Изображения` сгенерированы при помощи библиотеки `Pillow` и уже хранятся в папке `static` текущего проекта. Файл `csv` лежит в корне проекта. Изображения представляют собой текст категорий по которым они размечены.