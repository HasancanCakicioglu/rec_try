# test_my_script.py
import os
import sys

# Test dosyasının bulunduğu dizinden bir adım geri gidin
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))

# sys.path'e ekleyin
sys.path.append(project_root)

from src.main import print_hi


def test_print_hi():
    result = print_hi('PyCharm', 10, 20)
    assert result == 200  # Beklenen çıktıya göre bu değeri güncelleyin

