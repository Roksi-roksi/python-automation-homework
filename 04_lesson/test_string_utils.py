import pytest

from string_utils import StringUtils

string_utils = StringUtils()

@pytest.fixture
def utils():
    return StringUtils()

class TestCapitalize:
    @pytest.mark.parametrize("string, expected", [
        ("skypro", "Skypro"),
        ("Тест", "Тест"),
        ("123", "123"),
        ("04 апреля 2023", "04 апреля 2023"),
        ("sky pro", "Sky pro"),
    ])
    def test_capitalize_positive(self, utils, string, expected):
        assert utils.capitalize(string) == expected

    @pytest.mark.parametrize("string, expected", [
        ("", ""),
        (" ", " "),
    ])
    def test_capitalize_negative(self, utils, string, expected):
        assert utils.capitalize(string) == expected

    def test_capitalize_none(self, utils):
        with pytest.raises(AttributeError):
            utils.capitalize(None)


class TestTrim:
    @pytest.mark.parametrize("string, expected", [
        ("   skypro", "skypro"),
        ("  04 апреля 2023", "04 апреля 2023"),
        ("без_пробелов", "без_пробелов"),
        ("  текст с пробелами сзади  ", "текст с пробелами сзади  "),
    ])
    def test_trim_positive(self, utils, string, expected):
        assert utils.trim(string) == expected

    @pytest.mark.parametrize("string, expected", [
        ("", ""),
        (" ", ""),
        ("   ", ""),
    ])
    def test_trim_negative(self, utils, string, expected):
        assert utils.trim(string) == expected

    def test_trim_none(self, utils):
        with pytest.raises(AttributeError):
            utils.trim(None)


class TestContains:
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "U", False),
        ("04 апреля 2023", "4", True),
        ("Тест", "е", True),
    ])
    def test_contains_positive(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol, expected", [
        ("", "A", False),
        (" ", " ", True),
    ])
    def test_contains_negative(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

    def test_contains_empty_symbol_bug(self, utils):
        # Падающий тест (Критический дефект): пустая строка содержит в себе пустой символ,
        # однако из-за дефекта в логике index() возвращает 0, а проверка > -1 не срабатывает для первой позиции при баге.
        # Метод возвращает False вместо True.
        assert utils.contains("SkyPro", "") is True

    def test_contains_none(self, utils):
        with pytest.raises(AttributeError):
            utils.contains(None, "A")


class TestDeleteSymbol:
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("04 апреля 2023", "2023", "04 апреля "),
        ("Тест", "а", "Тест"), # Символа нет — строка не изменилась
    ])
    def test_delete_symbol_positive(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol, expected", [
        ("", "A", ""),
        (" ", " ", ""),
    ])
    def test_delete_symbol_negative(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    def test_delete_empty_symbol_bug(self, utils):
        # Дефект: из-за бага в методе contains, попытка удалить пустой символ ""
        # вернет исходную строку без изменений, вместо удаления пустых мест (или вызова ошибки)
        # Ожидаем, что метод отработает корректно или упадет, но он застревает на ложном False от contains()
        assert utils.delete_symbol("SkyPro", "") == "SkyPro"