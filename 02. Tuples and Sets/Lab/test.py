import json

my_dict = {"Name": [], "Address": [], "Age": []}

n = 30.00
print(type(n))
my_dict["Name"].append("Gabi")
my_dict["Address"].append("Blanton 12")
my_dict["Age"].append(n)
print(my_dict)

from math import ceil
items
y = {'a': 80.0, 'b': 0.0786235, 'c': 10.0, 'd': 10.6742903}


class TwoDec(float):
    def __repr__(self):
        return "%.2f" % self


def rounding_values(y, ceil=ceil, TwoDec=TwoDec):
    for d in y:
        for k, v in d.():
            d[k] = TwoDec(ceil(v * 100) / 100)


rounding_values(y)
for el in y:
    print(el)
