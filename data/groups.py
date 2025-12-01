# -*- coding: utf-8 -*-
from model.group import Group

# -n 10 -f data/test.json

testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits +  " " * 1 #string.punctuation +
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# testdata = [Group(name="",header= "", footer="")] + [
#              Group(name=random_string("group name", 5),
#                    header=random_string("group header", 10),
#                    footer=random_string("group footer", 10)) for i in range(5)
# ]

