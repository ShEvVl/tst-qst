# Сontent viewing service

Задача описана в `test_specs.docx`

## Для запуска выполнить:

- загрузить необходимые библиотеки;
- сгенерировать csv файл и изображения;
- запустить сервер.

```shell
    pip install -r requirements.txt
    python img_info_generator.py
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