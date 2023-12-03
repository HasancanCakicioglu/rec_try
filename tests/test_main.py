# test_my_script.py

from src.main import print_hi


def test_print_hi():
    result = print_hi('PyCharm', 10, 20)
    assert result == 200  # Beklenen çıktıya göre bu değeri güncelleyin

