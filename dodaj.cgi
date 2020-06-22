#!/usr/bin/env python3

import sqlite3
import cgitb
import cgi
import sys

def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        return 0

print("Content-type: text/html\n")

cgitb.enable()
form = cgi.FieldStorage()
imie = form.getvalue('imie')
nazwisko = form.getvalue('nazwisko')
wartosc_pesel = form.getvalue('pesel')
if (intTryParse(wartosc_pesel) == 0):
    print ("W polu PESEL musisz podac liczbe!")
    print('<br>')
    print('<form action="http://sirius.cs.put.poznan.pl/~inf116457/baza-danych/dodaj.html" />')
    print('<input type="submit" value="Powrot" />')
    print('</form>')
    sys.exit()
else:
    pesel = int(wartosc_pesel)

conn = sqlite3.connect("data/bazadanych.db")
c = conn.cursor()
c.executescript("""
	CREATE TABLE IF NOT EXISTS pacjenci(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nazwisko VARCHAR(30),
		imie VARCHAR(30),
		pesel INT,
        hemoglobina INT,
        hematokryt INT,
        erytrocyty INT,
        leukocyty INT,
        krwinki_plytkowe INT,
        srednia_masa_hemoglobiny INT,
        srednie_stezenie_hemoglobiny INT,
        srednia_objetosc_erytrocytow INT);
""")
empty = 0
c.execute("INSERT INTO pacjenci (nazwisko, imie, pesel, hemoglobina, hematokryt, erytrocyty, leukocyty, krwinki_plytkowe, srednia_masa_hemoglobiny, srednie_stezenie_hemoglobiny, srednia_objetosc_erytrocytow) VALUES ('%s', '%s', %d, %d, %d, %d, %d, %d, %d, %d, %d)" % (nazwisko, imie, pesel, empty, empty, empty, empty, empty, empty, empty, empty))
#print("c.execute("INSERT INTO pacjenci (nazwisko, imie, pesel, hemoglobina, hematokryt, erytrocyty, leukocyty, krwinki_plytkowe, srednia_masa_hemoglobiny, srednie_stezenie_hemoglobiny, srednia_objetosc_erytrocytow) VALUES ('%s', '%s', %d)" % (nazwisko, imie, pesel, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL))")
conn.commit()
c.close()
print("Pacjent zostal pomyslnie dodany\n\r")
print('<br>')
print('<form action="http://sirius.cs.put.poznan.pl/~inf116457/baza-danych/dodaj.html" />')
print('<input type="submit" value="Zarejestruj nowego pacjenta" />')
print('</form>')
print('<br>')
print('<form action="http://sirius.cs.put.poznan.pl/~inf116457/baza-danych/lista.cgi" />')
print('<input type="submit" value="Wyswietl liste zarejestrowanych pacjentow" />')
print('</form>')
