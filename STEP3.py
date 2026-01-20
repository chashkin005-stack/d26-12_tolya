# 1.1
#
# morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}
# operating_mode = int(input("Для режима шифратора нажмите - 1\nДля режима дешифратора нажмите - 0\n"))
# result = []
# if operating_mode:
#     word = list(input("Введите слово\n").lower())
#     for letter in word:
#         if letter in morze:
#             result.append(morze[letter])
#     print(*result)
# else:
#     morze_word = list(input("Введите шифр\n").split())
#     for value in morze_word:
#         for key, morse_value in morze.items():
#             if morse_value == value:
#                 result.append(key)
#                 break
#     print(*result, sep='')

# 1.2

# countries = {"Россия": ["Москва", "Казань", "Новгород"]}
# while True:
#     x = input().split()
#     if len(x)==1 and x[0] in countries:
#         print(countries[x[0]])
#     elif x[0] in countries and x[1] not in countries:
#         countries[x[0]].append(x[1])
#         print(countries)
#     elif x[0] not in countries and x[1] not in countries:
#         countries[x[0]] = x[1:]
#         print(countries)

# 1.3

# word = list(input().replace(" ", ""))
# letter = {}
# for i in word:
#     if i not in letter:
#         letter[i] = 1
#     elif i in letter:
#         letter[i] += 1
# print(letter)

# 2.1
# import math
# def type_trl(coords: list[tuple[int, int]]) -> str:
#     lens = []
#     result = []
#     lens.append(math.sqrt((coords[1][0] - coords[0][0])**2 + (coords[1][1] - coords[0][1])**2))
#     lens.append(math.sqrt((coords[2][0] - coords[1][0])**2 + (coords[2][1] - coords[1][1])**2))
#     lens.append(math.sqrt((coords[0][0] - coords[2][0])**2 + (coords[0][1] - coords[2][1])**2))
#     lens.sort()
#     if lens[0] == lens[1] == lens[2]:
#             result.append('равносторонний')
#     elif lens[2]**2 - (lens[0]**2 + lens[1]**2) < 0.001 :
#             result.append('прямоугольный')
#     if lens[0] == lens[1] or lens[1] == lens[2] or lens[0] == lens[2]:
#             result.append('равнобедренный')
#     if len(result) == 0:
#         result.append('обычный')
#     print(*result)
# type_trl([(0, 0), (4, 2), (3, 1)])

# 2.2
# def is_correct_bracket(text: str) -> bool:
#     replace_text = text.replace('', ' ').split()
#     list_open = []
#     list_close = []
#     bool_result = ()
#     for i in replace_text:
#         if i == "(":
#             list_open.append(i)
#         elif i == ")":
#             list_close.append(i)
#         if len(list_open) < len(list_close):
#             bool_result = False
#             break
#         else:
#             bool_result = True
#     return bool_result
#
#
# print(is_correct_bracket(')(())('))

# 2.3

# def decryption_by_freq(text: str, decode_dict: dict[str, int]) -> str:
#     text_dict = {}
#     decode_dict_inverted = {value: key for key, value in decode_dict.items()}
#     for i in text:
#         if i not in text_dict:
#             text_dict[i] = 1
#         else:
#             text_dict[i] += 1
#     result = []
#     for i in text:
#         values = text_dict[i]
#         if values in decode_dict_inverted:
#             result.append(decode_dict_inverted[values])
#     print(*result, sep="")
#
#
# decryption_by_freq('*!*!*?', {'a': 3, 'н': 2, 'c': 1})
# decryption_by_freq('otonnn', {'с': 3, 'у': 2, 'к': 1})

