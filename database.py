import sqlite3
import database_prep

def creatingTables():
    con = sqlite3.connect('countryDatabase.sqlite')

    c = con.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Country(
              id INTEGER PRIMARY KEY,
              country_code TEXT UNIQUE,
              country_name TEXt)''')
    con.commit()
    con.close()


def insertData():
    con = sqlite3.connect('countryDatabase.sqlite')
    c = con.cursor()

    for currency in database_prep.currencies:
        country_code = currency['code']
        country_name = currency['name']
        c.execute('INSERT INTO Country(country_code, country_name) VALUES(?,?)',(country_code, country_name))
    con.commit()
    con.close()


        
if __name__ == "__main__":
    #creatingTables()
    #insertData()