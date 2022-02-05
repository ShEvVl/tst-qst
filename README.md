# Сontent viewing service

Задача описана в `test_specs.docx`

## Для запуска выполнить:
```shell
Загрузить необходимые библиотеки:

    pip install -r requirements.txt

Сгенерировать csv файл и изображения:

    img_info_generator.py

Запустить сервер:

    python main.py 
```

## Пример запроса :
```shell
http://localhost:8080/?category[]=city&category[]=apple
```
Существующие категории :
```shell
'apple', 'banana', 'city', 'drill', 'ear', 'forest', 'gim', 'hill', 'ink', 'juice', 'koala', 'lion', 'mouse', 'notebook', 'octopus', 'panda', 'queen', 'rabbit', 'sun', 'tea'
```

Для запуска сервера с пользовательским интерфейсом:
```shell
python main_ui.py 
```
адрес сервера `http://localhost:8080`

## Примечание
Тестовые изображения генерируются и размечаются с помощью исполняемого файла `img_info_generator.py`, их описания указаны в файле `info.csv`. `Изображения` генерируются при помощи библиотеки `Pillow` и помещаются в папку `static` текущего проекта. Файл `csv` генерируется в корень проекта. Изображения представляют собой текст категорий от 1 до 10 на нейтральном фоне по которым они размечены.