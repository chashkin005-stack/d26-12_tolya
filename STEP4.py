# # 1.1
#
# i = [x **2 for x in range(20) if x % 2 != 0]
# print(i)

# 1.2

# list_i = ['-2', '0', '4', '1', '-5', '7', '2', '1']
# print(set([x for x in sorted([abs(int(x)) for x in list_i]) if x % 2 != 0]))

# 1.3

# row = input()
# row_dict = {}
# for i in row[:15]:
#     row = row[:15]
#     if i not in row_dict:
#         row_dict[i] = len(row) - 1 - row[::-1].index(i)
# print(row_dict)

# 2.1
# import pytest
# def equation(i: int) -> int:
#     if i < 0:
#         return False
#     else:
#         return i**0.5 + 16/i
#
#
# def test_equation_true():
#     assert equation(2)
#     assert equation(3)
#
# def test_equation_false():
#     assert not equation(-2)
#     assert not equation(-5)


# 2.2
# from unittest.mock import Mock, patch
# import requests
#
#
# def get_currency_rate(currency_code):
#     """Получение курса валюты к USD из API"""
#     url = "https://open.er-api.com/v6/latest/USD"
#     response = requests.get(url)
#     data = response.json()
#     return data['rates'][currency_code]
#
#
# def convert_to_usd(amount, currency_code):
#     """Конвертация суммы в USD"""
#     rate = get_currency_rate(currency_code)
#     return round(amount / rate, 2)
#
#
# def test_convert():
#     mock_response = Mock()
#     mock_response.json.return_value = {'rates': {'EUR': 0.85}}
#
#     with patch('requests.get') as mock_get:
#         mock_get.return_value = mock_response
#         url = "https://open.er-api.com/v6/latest/USD"
#         response = requests.get(url)
#         data = response.json()
#         result = data['rates']['EUR']
#
#         assert result == 0.85
#         print("✓ Простейший тест пройден!")
#
#
# if __name__ == "__main__":
#     test_convert()

