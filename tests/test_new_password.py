import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test1():
    password = generate_password(1111)
    assert len(password) == 15
    
def test():
    password = generate_password(15)
    assert len(password) == 15


def test2():
    password = generate_password(1000)
    assert len(password) != 0
