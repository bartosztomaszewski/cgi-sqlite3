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
temp_pesel = form.getvalue('pesel')
pesel = int(temp_pesel)
hemoglobina = int(form.getvalue('hemoglobina'))
hematokryt = int(form.getvalue('hematokryt'))
erytrocyty = int(form.getvalue('erytrocyty'))
leukocyty = int(form.getvalue('leukocyty'))
krwinki_plytkowe = int(form.getvalue('krwinki_plytkowe'))
srednia_masa_hemoglobiny = int(form.getvalue('srednia_masa_hemoglobiny'))
srednie_stezenie_hemoglobiny = int(form.getvalue('srednie_stezenie_hemoglobiny'))
srednia_objetosc_erytrocytow = int(form.getvalue('srednia_objetosc_erytrocytow'))


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
c.execute("UPDATE pacjenci SET hemoglobina = ? , hematokryt = ? , erytrocyty = ? , leukocyty = ? , krwinki_plytkowe = ? , srednia_masa_hemoglobiny = ? , srednie_Stezenie_hemoglobiny = ? , srednia_objetosc_erytrocytow = ? WHERE pesel = ?", (hemoglobina, hematokryt, erytrocyty, leukocyty, krwinki_plytkowe, srednia_masa_hemoglobiny, srednie_stezenie_hemoglobiny, srednia_objetosc_erytrocytow, pesel))
#print("c.execute("INSERT INTO pacjenci (nazwisko, imie, pesel, hemoglobina, hematokryt, erytrocyty, leukocyty, krwinki_plytkowe, srednia_masa_hemoglobiny, srednie_stezenie_hemoglobiny, srednia_objetosc_erytrocytow) VALUES ('%s', '%s', %d)" % (nazwisko, imie, pesel, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL))")
conn.commit()
c.close()
print("Wynik badan zostal zaktualizowany\n\r")
print('<br>')
print('<br>')
flag = True
if (hemoglobina > 13 or hemoglobina is 0) and hemoglobina < 18:
    print("Hemoglobina jest w normie\r\n")
    print('<br>')
else:
    #print("Hemoglobina jest nieprawidlowa")
    print('<font color="red">Hemoglobina jest nieprawidlowa</font>')
    flag = False
    print('<br>')

if (hematokryt > 40 or hematokryt is 0) and hematokryt < 54:
    print("hematokryt jest w normie\r\n")
    print('<br>')
else:
    #print("hematokryt jest nieprawidlowy")
    print('<font color="red">hematokryt jest nieprawidlowy</font>')
    flag = False
    print('<br>')

if (erytrocyty > 4 or erytrocyty is 0) and erytrocyty < 6:
    print("erytrocyty sa w normie\r\n")
    print('<br>')
else:
    #print("erytrocyty sa nieprawidlowe")
    print('<font color="red">erytrocyty sa nieprawidlowe</font>')
    flag = False
    print('<br>')

if (leukocyty > 4 or leukocyty is 0) and leukocyty < 10:
    print("leukocyty sa w normie\r\n")
    print('<br>')
else:
    #print("leukocyty sa nieprawidlowe")
    print('<font color="red">leukocyty sa nieprawidlowe</font>')
    flag = False
    print('<br>')

if (krwinki_plytkowe > 150 or krwinki_plytkowe is 0) and krwinki_plytkowe < 450:
    print("krwinki plytkowe sa w normie\r\n")
    print('<br>')
else:
    #print("krwinki plytkowe sa nieprawidlowa")
    print('<font color="red">krwinki plytkowe sa nieprawidlowa</font>')
    flag = False
    print('<br>')

if (srednia_masa_hemoglobiny > 27 or srednia_masa_hemoglobiny is 0) and srednia_masa_hemoglobiny < 34:
    print("srednia masa hemoglobiny jest w normie\r\n")
    print('<br>')
else:
    #print("srednia masa hemoglobiny jest nieprawidlowa")
    print('<font color="red">srednia masa hemoglobiny jest nieprawidlowa</font>')
    flag = False
    print('<br>')

if (srednie_stezenie_hemoglobiny > 32 or srednie_stezenie_hemoglobiny is 0) and srednie_stezenie_hemoglobiny < 36:
    print("srednie stezenie hemoglobiny jest w normie\r\n")
    print('<br>')
else:
    #print("srednie stezenie hemoglobiny jest nieprawidlowe")
    print('<font color="red">srednie stezenie hemoglobiny jest nieprawidlowe</font>')
    flag = False
    print('<br>')

if (srednia_objetosc_erytrocytow > 80 or srednia_objetosc_erytrocytow is 0) and srednia_objetosc_erytrocytow < 100:
    print("srednia objetosc erytrocytow jest w normie\r\n")
    print('<br>')
else:
    #print("srednia objetosc erytrocytow jest nieprawidlowa")
    print('<font color="red">srednia objetosc erytrocytow jest nieprawidlowa</font>')
    flag = False
    print('<br>')

if flag:
    print('<font color="green">Wszystkie wyniki sa OK</font>')
print('<br>')
print('<br>')
print('<form action="http://sirius.cs.put.poznan.pl/~inf116457/baza-danych/laboratorium.cgi" />')
print('<input type="submit" value="Dodaj kolejny wynik laboratoryjny" />')
print('</form>')
