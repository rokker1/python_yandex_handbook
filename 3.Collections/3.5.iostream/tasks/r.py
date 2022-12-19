import os
import math


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0Б"
    size_name = ("Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ", "ЭБ", "ЗБ", "ЁБ")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = math.ceil(size_bytes / p)
    return "%s%s" % (s, size_name[i])


filename = input()
statinfo = os.stat(filename)
print(convert_size(statinfo.st_size))