import numpy as np


def text_decode(text="", template=""):
    result = []
    for t in text:
        before = len(result)
        for i in range(len(template)):
            if t == template[i]:
                result.append(i)
        if len(result) == before:
            result.append(-1)
    return result


def text_encode(value=[], template=""):
    result = ""
    for i in value:
        if 0 <= i < len(template):
            result += template[i]
        else:
            result += "-1"
    return result


def value_encode(value):
    result = [[], []]
    for i in range(0, len(value), 2):
        result[0].append(value[i])
        result[1].append(value[i+1])
    return np.array(result)


def value_decode(value):
    result = []
    for i in range(0, len(value[0])):
        result.append(int(value[0][i]))
        result.append(int(value[1][i]))
    return result


def nshin_decode(text, template):
    result = 0
    for i in range(len(text)):
        for j in range(len(template)):
            if text[i] == template[j]:
                result += (len(template) ** (len(text) - i - 1)) * j
    return result


def nshin_encode(value, template):
    result = ""
    for t in value:
        result += template[int(t, len(template))]
    return result


# def Encorder(text, template):
#     result = 0
#     for i in range(len(text)):
#         for j in range(len(template)):
#             if text[i] == template[j]:
#                 result += (len(template) ** (len(text) - i - 1)) * j
#     return result
#
#
# def Decorder(text, template, Nshin):
#     for t in text:
#         print(f"{template[int(t, Nshin)]}", end='')
