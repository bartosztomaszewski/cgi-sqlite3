#!/usr/bin/env python3

import sqlite3
import cgitb
import cgi

print("Content-type: text/html\n")

cgitb.enable()
form = cgi.FieldStorage()
imie = form.getvalue('imie')
nazwisko = form.getvalue('nazwisko')
pesel = form.getvalue('pesel')

conn = sqlite3.connect("data/bazadanych.db")
c = conn.cursor()
c.execute("DELETE FROM pacjenci WHERE nazwisko = '%s' AND imie = '%s' AND pesel = %d" % (nazwisko, imie, int(pesel)))
conn.commit()
c.close()
print("Wizyta zostala odwolana")
print("Za chwile wrocisz do poprzedniej strony")
print('<meta http-equiv="refresh" content="3;url=http://sirius.cs.put.poznan.pl/~inf116457/baza-danych/lista.cgi" />')
