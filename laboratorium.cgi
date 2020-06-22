#!/usr/bin/env python3

import sqlite3
import cgitb

print("Content-type: text/html\n")

cgitb.enable()

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
c.execute("select * from pacjenci")
print('<table border="1" cellspacing="0" cellpadding="3">')
print('<tr>')
print('<th>Nazwisko</th>')
print('<th>Imie</th>')
print('<th>pesel</th>')
print('<th>hemoglobina</th>')
print('<th>hematokryt</th>')
print('<th>erytrocyty</th>')
print('<th>leukocyty</th>')
print('<th>krwinki plytkowe</th>')
print('<th>srednia masa hemoglobiny</th>')
print('<th>srednie stezenie hemoglobiny</th>')
print('<th>srednia objetosc erytrocytow</th>');
for row in c:
    print('<tr>')
    print('<th>',row[1],'</th>')
#    print(row[1],row[2])
    print('<th>',row[2],'</th>')
    print('<th>',row[3],'</th>')
    print('<th>',row[4],'</th>')
    print('<th>',row[5],'</th>')
    print('<th>',row[6],'</th>')
    print('<th>',row[7],'</th>')
    print('<th>',row[8],'</th>')
    print('<th>',row[9],'</th>')
    print('<th>',row[10],'</th>')
    print('<th>',row[11],'</th>')
    print('</tr>')
c.close()
print('</table>')
print('<br>')
#print('<form action="/~inf116457/baza-danych/usun.cgi" target="_self" method="POST">')
print('<form action="/~inf116457/baza-danych/edycja.cgi" target="_self" method="POST">')
print('<input type="text" name="nazwisko" placeholder="Podaj nazwisko" minlength="1" required><br><br>')
print('<input type="text" name="imie" placeholder="Podaj imie" minlength="1" required><br><br>')
print('<input type="text" name="pesel" placeholder="Podaj pesel" minlength="1" required><br><br>')
print('<input type="text" name="hemoglobina" placeholder="Podaj hemoglobinie" minlength="1" required><br><br>')
print('<input type="text" name="hematokryt" placeholder="Podaj hematokryt" minlength="1" required><br><br>')
print('<input type="text" name="erytrocyty" placeholder="Podaj erytrocyty" minlength="1" required><br><br>')
print('<input type="text" name="leukocyty" placeholder="Podaj leukocyty" minlength="1" required><br><br>')
print('<input type="text" name="krwinki_plytkowe" placeholder="Podaj krwinki plytkowe" minlength="1" required><br><br>')
print('<input type="text" name="srednia_masa_hemoglobiny" placeholder="Podaj srednia mase hemoglobiny" minlength="1" required><br><br>')
print('<input type="text" name="srednie_stezenie_hemoglobiny" placeholder="Podaj srednie stezenie hemoglobiny" minlength="1" required><br><br>')
print('<input type="text" name="srednia_objetosc_erytrocytow" placeholder="Podaj srednia objetosc erytrocytow" minlength="1" required><br><br>')
print('<form action="/~inf116457/baza-danych/edycja.cgi" target="_self" method="POST">')
print('<input type="submit" value="Dodaj wyniki">')
print('</form>')

