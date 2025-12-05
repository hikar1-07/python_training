import pymysql.cursors
from fixture.db import DbFixture


# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     cursor = db.cursor()
#     cursor.execute('select id, firstname, lastname from addressbook')
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     db.destroy()

# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     db.destroy()

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()