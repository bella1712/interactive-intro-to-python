# Interaktive Einführung in Python :snake:
Dieses Repository soll dir eine kurze Einführung in das Programmieren mit Python geben. Du wirst lernen, welche Datentypen und Operatoren es gibt und wofür sie da sind. Ausserdem werdet wirst du lernen, was Variablen, Kontrollstrukturen und Schleifen sind. 

## Lernziele :mortar_board:
- Du lernst Python kennen und weisst wofür man diese Programmiersprache braucht
- Du kennst verschiedene Datentypen und weisst wofür man welchen Datentyp verwendet
- Du kannst Variablen Deklarieren und weisst wie man mit ihnen arbeitet
- Du kennst die verschiedenen Operatoren und ihren Anwendungszweck
- Du kennst Kontrollstrukturen und könnt diese anwenden
- Du kennst die verschiedenen Schleifentypen und weisst, wann du welchen verwendest.
- Du weisst wie man eine Klasse und eine Funktion macht und kannst dies anwenden.
- Du kannst mittels dem neu erlenten Wissen dein erstes Python-Programm selbst schreiben.

## Python und seine Geschichte :book:
Python ist eine vielseitige, interpretierte Programmiersprache, die Anfang der 1990er Jahre von Guido van Rossum entwickelt wurde. Sie zeichnet sich durch eine klare, lesbare Syntax aus und unterstützt verschiedene Programmierparadigmen wie objektorientierte, funktionale und prozedurale Programmierung. Python wurde ursprünglich als Nachfolger der ABC-Sprache, welche nur 5 Grunddatentypen hatte und keine Variablendeklaration benötigte, konzipiert und hat sich seitdem zu einer der beliebtesten Programmiersprachen weltweit entwickelt. 

## Variablen
Variablen kannst du dir wie kleine Boxen oder Container vorstellen, die einen Inhalt speichern können. Sie werden beim Programmieren verwendet, damit du nicht immer explizite Werte angeben musst und variabel programmieren kannst. 
Wenn du beispielsweise zu Hause ein Glas hast, aus dem du trinkst, dann musst du auch nicht vorher bestimmen, ob da nur Wasser herein kommt, sondern du kannst auch andere Getränke wie Saft hineinfüllen. Ähnlich ist das mit Variablen. 
Das oben genannte Beispiel sieht in Pyhton so aus:
```
glas = "Wasser"
print(glas)
# Ausgabe: Wasser

glas = "Saft"
print(glas)
# Ausgabe: Saft
```
Varibalen können aber auch für Berechnungen verwendet werden. Angenommen ich möchte auf 5 Zählen, dann kann das in Python Code so aussehen:
```
zahl_init= 0
zahl_1=1
zahl_2=2
zahl_3=3
zahl_4=4
zahl_5=5

print(zahl_init, zahl_1, zahl_2 zahl_3, zahl_4, zahl_5)
# Ausgabe: 0 1 2 3 4 5 
```
Das ist allerding sehr umständlich, vorallem, wenn du später mit Schleifen arbeitest. Daher wird oft folgende Vorgehensweise verwendet:
```
zahl = 0
print(zahl)
# Ausgabe: 0

zahl = zahl + 1
print(zahl)
# Ausgabe: 1

zahl = zahl + 1
print(zahl)
# Ausgabe: 2

zahl = zahl + 1
print(zahl)
# Ausgabe: 3

zahl = zahl + 1
print(zahl)
# Ausgabe: 4

zahl = zahl + 1
print(zahl)
# Ausgabe: 5
```
Du kannst also den Wert ein Variable mit dem Wert der Variable verändern. 

## Datentypen :page_facing_up:
Du kannst dir Datentpyen wie eine Unterteilung verschiedener Kategorien vorstellen. Stell dir deinen Alltag vor:
- Du redest &rarr; dafür verwendest du **Wörter**
- Du rechnest &rarr; dafür verwendest du **Zahlen**
- Du musst dich für etwas entscheiden &rarr; dafür verwendetst du **Affirmation und Negation**
- Du musst Wörter bustabieren &rarr; dafür verwendest du **Buchstaben**
- Du putzt dir deine Zähne &rarr; dafür verwendest du einen **Routine**
Wenn du programmierst, musst du deinem Programm sagen, was es machen soll. Da Programme keine Intuition haben, so wie du es tust, musst du ihm helfen und ihm sagen, was du von ihm möchtest. Ein Beispiel: Du möchtest, dass dein Programm einen Text ausgibt. Damit das funktioniert muss das Programm wissen, dass es sich um einen **Text** und nicht um eine **Zahl** oder gar eine **Handlung** handelt. Um diese Unterscheidung machen zu können gibt es in Python Datentypen.

### Primitive Datentypen :sunglasses:
| Datentyp  |  Beschreibung |Deklaration in Python|
|:---:|:---|:---|
|  Boolean | Hat die Werte *True* oder *False* und wird oft für Entscheidungen verwendet. Mehr dazu findest du im Kapitel Kontrollstrukturen und Schleifen| bool_1 = True <br>bool_2 = False|
| Integer  | Repräsentiert eine ganze Zahl. |integer = 2|
|Float| Repräsentiert eine Fliesskommazahl  |float_1 = 2.0 <br> float_2 = 2f |
|String | Repräsentiert ein Zeichen oder eine Zeichenkette und muss immer in Anführungszeichen gesetzt werden |string_1 = 'Hello' <br> string_2 ="World!"|

### Nicht primitive Datentypen :bowtie:
| Datentyp  | Beschreibung  |Deklaration in Python|
|:---:|:---|:---|
|  List |Ein Liste die Elemente aus verschiedenen Datentypen enthalten kann   |list = []|
|  Tuple | Funktioniert ähnlich wie eine Liste, ist aber unveränderlich  |tuple = ()|
| Dictionary | Ein Datentyp in dem Key-Value Paare gespeichert werden. Beispiel: "Name": "Max Muster"  |dict = {key : value}|
| Set  |Ähnlich wie die Liste. Allerdings ist ein Set ungeordnet, unveränderlich und hat keinen Index |set = {}|
|Array   | Funktioniert wie eine Liste, da Python eigentlich keinen Array support hat. Daher werden prinzipiell Listen verwendet  |arr = []|

## Operatoren :thought_balloon:
Operatoren werden verwendet um Zuweisungen zu machen oder Mathematische oder vergeleichende Operationen auszuführen.

### Zuweisende Operatoren :arrow_right:
|Operator|	Beispiel|	Das Gleiche wie	| Beschreibung der Zuweisung|Rechenbeispiel mit x = 5 |
|:---:|:---|:---|:---|:---|
|=|	x = 5|	x = 5	|x hat den Wert 5| keine Rechnung |
|+=	|x += 3	|x = x + 3	|x hat den Wert von (x + 3) |x = 5 + 3 &rarr; x = 8|
|-=	|x -= 3	|x = x - 3	|x hat den Wert von (x - 3) |x = 5 - 3 &rarr; x = 2|
|*=	|x *= 3	|x = x * 3	|x hat den Wert von (x * 3)|x = 5 * 3 &rarr; x = 2|
|/=	|x /= 3	|x = x / 3	|x hat den Wert von (x / 3)|x = 5 / 3 &rarr; x = 2|
|%=	|x %= 3	|x = x % 3	|x hat den Wert des Rests von (x / 3)|x = 5 % 3 &rarr; x = 2 <br>Weil 5 /3 (bzw. 5//3) ist gleich 1 mit Rest 2|
|//=	|x //= 3	|x = x // 3	|x hat den Wert der Ganzzahldivision von (x / 3)|x = 5 // 3 &rarr; x = 1 <br>Weil die 3 nur 1 Mal ganz in die 5 passt|
|**=	|x **= 3	|x = x ** 3	|x hat den Wert von x^{3}|x = 5 ** 3 &rarr; x =  125|
|&=	x |&= 3	|x = x & 3	|x hat den Wert der bitweisen Andoperation von x & 3|x = 5 & 3 &rarr; x = 1 <br>Weil 5 binär = 101 und 3 binär 11 ist. Die And-Operation ergibt 1 weil 101 and 011 ist 001, was gleich 1 ist|
|&#124;=|	x &#124;= 3	|x = x &#124; 3	|x hat den Wert der bitweisen Andoperation von x or 3|x = 5 &#124; 3 &rarr; x =7 <br>Weil 101 or 11 = 111, was gleich 7 ist |
|^=	|x ^= 3	|x = x ^ 3	|x hat den Wert einer bitweise XOR Operation von x und 3|x = 5 ^ 3 &rarr; x = 6 <br>Weil 101 XOR 011 = 110 was gleich 6 ist|
|>>=	|x >>= 3	|x = x >> 3	|x hat den Wert einer Bitverschiebung nach rechts um 3 Stellen|x = 5 >> 3 &rarr; x = 0 <br>Weil 0101 um 3 Stellen nach Rechts verschoben 0000 ist, was gleich 0 ist|
|<<=|	x <<= 3	|x = x << 3	|x hat den Wert einer Bitverschiebung nach links um 3 Stellen)|x = 5 << 3 &rarr; x = 40 <br>Weil 0000101 um 3 Stellen nach links verschoben 101000 ist, was 40 ist|
|:=|	print(x:=3)	|x = 3 print(x)|x hat den Wert 3|keine Rechnung|

### Mathematische Operatoren :1234:
|Operator|	Name	|Beispiel|
|:---:|:---|:---|
|+	|Addition|	x + y	|
|-	|Subtratkion|	x - y	|
|*|	Multiplikation|	x * y	|
|/|	Division|	x / y	|
|%|	Modulo, der Rest, der nach einer Division übrig bleibt|	x % y	|
|**|	Expoential|	x ** y	|
|//|	Ganzzahliges Ergebnis nach einer Division (mit möglichem Rest)|	x // y	|

### Vergleichsoperatoren :information_source:
|Operator|Name|	Beispiel	|
|:---:|:---|:---|
|==	|Gleich|	x == y|	
|!=|	Ungleich|	x != y|	
|>	|Grösser als|	x > y	|
|<	|Kleiner als|	x < y	|
|>=|	Grösser oder gleich wie|	x >= y|	
<=	|Grösser oder gleich wie|x <= y|

## Kontrollstrukturen :passport_control:
Mit Kontrollstrukturen können Programme Entscheidungen treffen. Das passiert mit *Wenn &rarr; dann* Aussagen. Nehmen wir beispielsweise eine Wegbeschreibung: Folge dem Strassenverlauf 100m. *Wenn* du diese Strecke absolviert hast *dann* biege links ab. 
Programme habe keinen eigenen Willen und brauchen klare Anweisungen um funktionieren zu können. Daher ist es wichtig, dass diese  *Wenn &rarr; dann* Anweisungen präzise sind. Angenommen, wie wollen das oben genannte Beispiel in Code umsetzen, dann sieht das in Python folgendermassen aus: 
```
if (gelaufener_weg == 100):
  turn_right = True
else:
  countinue
```
Dann gibt es aber noch Szenarien, in denen wir eine Zwischenüberlegung machen müssen. Wenn wir beispielsweise einen Unfall sehen, sollten wir anhalten und den Unfallbeteiligten in ihrer Notlage helfen. Für ein solches Szenario würden wir umgangssprachlich vermultich etwas sagen wie: "Wenn du 100 Meter gelaufen bist, dann biege rechts ab, andernfalls, wenn du einen Unfall siehst halte an und helfe den verletzten, sollten beide Szenarien nicht zutreffen, dann lauf einfach weiter. "
In Pythoncode würde das wie folgt aussehen: 
```
if (gelaufener_weg == 100):
  turn_right = True
elif(unfall_passiert == True):
  helfen = True
  break 
else:
  countinue
```
## Schleifen :arrows_counterclockwise:
Du hast bis jetzt schon viele Grundlagen der Programmierung kennengelernt, aber um ein funktionierendes Programm schreiben zu können brauchst du noch das Wissen, was Schleifen sind. Generell erleichtern dir Schleifen das leben, weil sie es dir ermöglichen die Anzahl an Wiederholungen zu definieren. Das passiert entweder dadurch, dass du eine exakte Anzahl an Wiederholungen oder eine Abbruchbedingung definierst.
Angenommen du hast 10 Mitschüler und du wünscht jedem einen guten Morgen. Nun sollst du diese Tätigkeit des Grüssens dokumentieren. Würdest du dann schreiben "Ich habe gesagt 'Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen.'"? Nein, oder? 
Du würdest schreiben "Ich habe 10 mal 'Guten Morgen' gesagt."
Beim Programmieren ist das genauso. Das oben genannte Beispiel sieht in Python folgendermassen aus:
```
for x in range(10):
  print("Guten Morgen") 
```
Es gibt aber auch andere Szenarien, in denen wir uns der Situation entsprechend anpassen müssen. Wenn einer deiner Mitschüler nicht da ist, musst du ihn nicht begrüssen. Daher würdest du solange "Guten Morgen" sagen, bis du keine Mitschüler mehr hast.
In python würde der Code dann wie folgt aussehen:
```
# Wenn du deine Mitschüler vorher zählen würdest: 
while i< anzahl_mitschueler:
  print("Guten Morgen")
  i+=1

# Falls du schaust ob es noch weitere Mitschüler gibt
whle mitschueler.hasNext():
  print("Guten Morgen")
```
Ansonsten gibt es noch eine letzte Schleifenart. Diese ist dafür da, falls du mindestens einen Durchlauf dieser Schleife erreichen möchtest. Beispielsweise kann es sein, dass all deine Mitschüler krank sind, du sie also nicht begrüssen musst, aber deine Lehrerin da ist. Ihr musst du immer und auf jeden Fall einen guten Morgen wünschen. In so einem Fall kommt in Python folgender Code zum Einsatz: 
```
do {
  print("Guten Morgen")
  }
while(mitschueler.hasNext());
```
## Klassen und Methoden  :shipit:
Jetzt hast die Grundlagen des Codens fast alle erfasst. Nur noch ein Punkt fehlt: Ordnung.
Code kann je nach Aufgabe sehr lang und unstruktriert werden. Um das zu vermeiden gibt es das sogenannte *Objekt orientierte Programmieren*. Hierbei wird der Code in Klassen und Methoden verteilt. Du kannst dir eine Klasse wie eine Schulklasse vorstellen: Jede Schulklasse hat einen Klassennamen, Schüler und eine Lehrperson. Das sind sogenannte Attribute. Sie definieren eine Klasse. 
Aber in jeder Schulklasse gibt es auch Aufgaben die gemacht werden müssen: lernen, tafel putzen, Stühle hochstellen, etc. Diese Aufgaben sind Methoden oder auch Funktionen. 
In Python Code sieht das wie folgt aus:
```
class Schulklasse:
# Konstruktor mit den Attributen der Klasse
  def __init__(self, klassenname, klassenlehrer, schueler):
    self.klassenname = klassenname
    self.klassenlehrer = klassenlehrer
    self.schueler = schueler

def lernen():
# pass kannst du verwenden, wenn du noch keinen konkreten Code für die Methode hast
  pass

def tafel_putzen():
  pass

def stuehle_hochstellen():
  pass
```

## Dein erstes Python Programm :triangular_flag_on_post:
Da du jetzt die Grundlagen der Programmierung mit Python kennst, wird es Zeit dein erstes Programm zu programmieren. Denn wirklich gut im Programmeieren kannst du nur mit viel **Übung** werden. Also leg los und viel Spass!
