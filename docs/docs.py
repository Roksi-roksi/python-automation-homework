def do_it(param_1: int, param_2: str, param_3: float) -> float:
    """
    Эта функция берет первые два параметра, складывает их и делит на третий.
    Результат печатается в консоль.
    Параметры должны быть в консоли.
    """
    # int — 19;
    # float — 2.6;
    # bool — True/False;
    # str — “Test”;
    # dict — {};
    # list — [].
    result = (param_1 + param_2) * param_3
    return [param_1 + param_2, param_3, result]


do_it(1, 2, 3)

# Команда ниже запускает Allure и конвертирует результаты теста в отчет: -
# allure serve "allure-result"

# Запустите тесты и укажите путь к каталогу результатов тестирования: -
# python -m pytest --alluredir "allure-result" <- название папки

# attach - вложения
# принимает на вход три параметра:
# content — содержимое вложения. Например, SQL-запрос к БД.
# title — название вложения. Например, SQL.
# type — тип вложения. Например, текст — TEXT.

# вызов результатов - allure serve allure-results
# вызов определенной папки и сохранение в нее результатов
#
# - python -m pytest Api/test_x_cleints.py --alluredir= "results"

# выгрузить отчет в папку - allure generate название папки (allure-result)
# результаты в index.html можно запускать с помощью команды: allure open allure-report

# создать папку и туда поместить отчет - allure generate из папки "results" в папку -o "finish"

# запуск готового цикла аллюр - powershell -ExecutionPolicy Bypass -File .\"run.ps1"
