# -*- coding: utf-8 -*-
from xml.etree.ElementTree import indent

from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits # +  " " * 10 string.punctuation +
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = ([Contact(firstname="",middlename= "", lastname="", nickname="", title="", company="", address="",
                     home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="")] +
            [Contact(firstname=random_string("firstname", 12),
                     middlename=random_string("middlename", 12),
                     lastname=random_string("lastname", 12),
                     nickname=random_string("nickname", 12),
                     title=random_string("title", 12),
                     company=random_string("company", 12),
                     address=random_string("address", 12),
                     mobile=random_string("mobile", 12),
                     home=random_string("home", 12),
                     work=random_string("work", 12),
                     fax=random_string("fax", 12),
                     email=random_string("email", 12),
                     email2=random_string("email2", 12),
                     email3=random_string("email3", 12),
                     homepage=random_string("homepage", 12))
                    # bday=random_string("bday", 2),
                    # bmonth=random_string("bmonth", 20),
                    # byear=random_string("byear", 20),
                    # aday=random_string("aday", 20),
                    # amonth=random_string("amonth", 20),
                    # ayear=random_string("ayear", 20))
                    for i in range(5)
             ])

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
