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
flag = False
for row in c:
    print('<tr>')
    print('<th>',row[1],'</th>')
    print('<th>',row[2],'</th>')
    print('<th>',row[3],'</th>')

    if (row[4] > 13 or row[4] is 0) and row[4] < 18:
        print('<th>',row[4],'</th>')
    else:
        print('<th><font color="red">',row[4],'</font></th>')
        flag = True
        
    if (row[5] > 40 or row[5] is 0) and row[5] < 54:
        print('<th>',row[5],'</th>')
    else:
        print('<th><font color="red">',row[5],'</font></th>')
        flag = True
        
    if (row[6] > 4 or row[6] is 0) and row[6] < 6:
        print('<th>',row[6],'</th>')
    else:
        print('<th><font color="red">',row[6],'</font></th>')
        flag = True
        
    if (row[7] > 4 or row[7] is 0) and row[7] < 10:
        print('<th>',row[7],'</th>')
    else:
        print('<th><font color="red">',row[7],'</font></th>')
        flag = True
        
    if (row[8] > 150 or row[8] is 0) and row[8] < 450:
        print('<th>',row[8],'</th>')
    else:
        print('<th><font color="red">',row[8],'</font></th>')
        flag = True
        
    if (row[9] > 27 or row[9] is 0) and row[9] < 34:
        print('<th>',row[9],'</th>')
    else:
        print('<th><font color="red">',row[9],'</font></th>')
        flag = True
        
    if (row[10] > 32 or row[10] is 0) and row[10] < 34:
        print('<th>',row[10],'</th>')
    else:
        print('<th><font color="red">',row[10],'</font></th>')
        flag = True
        
    if (row[11] > 80 or row[11] is 0) and row[11] < 100:
        print('<th>',row[11],'</th>')
    else:
        print('<th><font color="red">',row[11],'</font></th>')
        flag = True

    print('</tr>')
c.close()
print('</table>')
print('<br>')
if flag:
    print('<font color="red">Nieprawidlowy wynik, prosze poinformowac zainteresowanego pacjenta</font>')
print('<br>')
print('<form action="http://sirius.cs.put.poznan.pl/~inf116457/baza-danych/dodaj.html" />')
print('<input type="submit" value="Dodaj nowego pracownika" />')
print('</form>')
print('<br>')
print('<form action="/~inf116457/baza-danych/usun.cgi" target="_self" method="POST">')
print('<input type="text" name="nazwisko" placeholder="Podaj nazwisko" minlength="1" required><br><br>')
print('<input type="text" name="imie" placeholder="Podaj imie" minlength="1" required><br><br>')
print('<input type="text" name="pesel" placeholder="Podaj pesel" minlength="1" required><br><br>')
print('<input type="submit" value="Aby odwolac wizyte, wypelnij powyzsze pola">')
print('</form>')

