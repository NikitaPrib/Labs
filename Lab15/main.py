import sqlite3

con = sqlite3.connect('Avto_garage.db')
cursorObj = con.cursor()


def create():
    cursorObj.execute(
        'CREATE TABLE if not exists listOfPatient(id integer primary key,patient text, decease text)')

    con.commit()
create()
def sql_insert(con,entities):
    cursorObj.execute('INSERT INTO listOfPatient(id, patient, decease) VALUES(?,?,?)', entities)
    con.commit()
# def sql_fetch(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('DROP table if exists listOfPatient')
#     con.commit()
#
# sql_fetch(con)
entities = (6, "Анатолия", "Анемия")
sql_insert(con, entities)

# def sql_fetch(con):
# cursorObj = con.cursor()
# cursorObj.execute('DROP table if exists listOfDecease')
# con.commit()
# sql_fetch(con)
# con.close()

# CREATE TABLE listOfDecease
# (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# age INTEGER,
# company_id INTEGER,
# FOREIGN KEY (decease) REFERENCES decease (id) ON DELETE CASCADE
# );