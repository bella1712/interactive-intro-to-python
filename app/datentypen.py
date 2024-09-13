import streamlit as st
class Datentypen:
    def display_intro_teil_1(self):
        st.title("Datentypen :page_facing_up:")
        st.write("Du kannst dir Datentpyen wie eine Unterteilung verschiedener Kategorien vorstellen. Stell dir deinen Alltag vor:")
        st.markdown('''
            - Du redest &rarr; dafür verwendest du **Wörter**
            - Du rechnest &rarr; dafür verwendest du **Zahlen**
            - Du musst dich für etwas entscheiden &rarr; dafür verwendetst du **Affirmation und Negation**
            - Du musst Wörter bustabieren &rarr; dafür verwendest du **Buchstaben**
            - Du putzt dir deine Zähne &rarr; dafür verwendest du einen **Routine**''')
        st.markdown('''Wenn du programmierst, musst du deinem Programm sagen, was es machen soll. Da Programme keine Intuition haben, so wie du es tust, musst du ihm helfen und ihm sagen, was du von ihm möchtest. Ein Beispiel: Du möchtest, dass dein Programm einen Text ausgibt. Damit das funktioniert muss das Programm wissen, dass es sich um einen **Text** und nicht um eine **Zahl** oder gar eine **Handlung** handelt. Um diese Unterscheidung machen zu können gibt es in Python Datentypen.
        ''')
        st.markdown('''### Primitive Datentypen :sunglasses:''')
        st.markdown('''
        | Datentyp  |  Beschreibung |Deklaration in Python|
        |:---:|:---|:---|
        |  Boolean | Hat die Werte *True* oder *False* und wird oft für Entscheidungen verwendet. Mehr dazu findest du im Kapitel Kontrollstrukturen und Schleifen| bool_1 = True <br>bool_2 = False|
        | Integer  | Repräsentiert eine ganze Zahl. |integer = 2|
        |Float| Repräsentiert eine Fliesskommazahl  |float_1 = 2.0 <br> float_2 = 2f |
        |String | Repräsentiert ein Zeichen oder eine Zeichenkette und muss immer in Anführungszeichen gesetzt werden |string_1 = 'Hello' <br> string_2 ="World!"|
        ''')

    def display_intro_teil_2(self):
        st.markdown('''### Nicht primitive Datentypen :alien:''')
        st.markdown('''
           | Datentyp  |  Beschreibung |Deklaration in Python|
           |:---:|:---|:---|
            |  List |Ein Liste die Elemente aus verschiedenen Datentypen enthalten kann   |list = []|
            |  Tuple | Funktioniert ähnlich wie eine Liste, ist aber unveränderlich  |tuple = ()|
            | Dictionary | Ein Datentyp in dem Key-Value Paare gespeichert werden. Beispiel: "Name": "Max Muster"  |dict = {key : value}|
            | Set  |Ähnlich wie die Liste. Allerdings ist ein Set ungeordnet, unveränderlich und hat keinen Index |set = {}|
            |Array   | Funktioniert wie eine Liste, da Python eigentlich keinen Array support hat. Daher werden prinzipiell Listen verwendet  |arr = []|
           ''')
    def __main__(self):
        self.display_intro_teil_1()
        self.display_intro_teil_2()

