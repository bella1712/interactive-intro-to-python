import streamlit as st
import re
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
        |  Boolean | Hat die Werte *True* oder *False* und wird oft für Entscheidungen verwendet. Mehr dazu findest du im Kapitel Kontrollstrukturen und Schleifen| bool_1=True, bool_2=False|
        | Integer  | Repräsentiert eine ganze Zahl. |integer=2|
        |Float| Repräsentiert eine Fliesskommazahl  |float_1=2.0, float_2=2f |
        |String | Repräsentiert ein Zeichen oder eine Zeichenkette und muss immer in Anführungszeichen gesetzt werden. Eigentlich handelt es sich bei einem String um ein Objekt, dennoch wird der String wie ein primitiver Datentyp initialisiert. |string_1='Hello',  string_2="World!"|
        ''')

    def display_intro_teil_2(self):
        st.markdown('''### Nicht primitive Datentypen :alien:''')
        st.markdown('''
           | Datentyp  |  Beschreibung |Deklaration in Python|
           |:---:|:---|:---|
            |  List |Ein Liste die Elemente aus verschiedenen Datentypen enthalten kann   |list = []|
            |  Tuple | Funktioniert ähnlich wie eine Liste, ist aber unveränderlich  |tuple = ()|
            | Dictionary | Ein Datentyp in dem Key-Value Paare gespeichert werden. Beispiel: "Name": "Max Muster"  |dict = {key : value}|
            | Set  |Ähnlich wie die Liste. Allerdings ist ein Set ungeordnet, unveränderlich und hat keinen Index. Des Weiteren dürfen Elemente in einem Set nicht doppelt vorkommen |set = set()|
            |Array   | Funktioniert wie eine Liste, da Python eigentlich keinen Array support hat. Daher werden prinzipiell Listen verwendet  |arr = []|
           ''')

    def exercise_1(self):
        self.question_1()
        self.question_2()
        self.question_3()



    def question_1(self):
        st.markdown('''#### Übungen zu den primitiven Datentypen :balloon:''')
        st.write("Wähle die passenden Antworten aus:")
        #if answer_1 not in st.session_state:

        question_1 = st.radio(
            "Welche Werte kann ein Boolean in Python haben?",
            ["**Yes** und **No**", "**yes** und **no**", "**True** und **False**", "**true** und **false**"],
            index=None,
            horizontal=True,
        )
        if question_1==None:
            st.write("")
        elif question_1 == "**True** und **False**":
            st.success("Richtig, in Python hat kann ein Boolean die Werte **True** und **False** haben :white_check_mark:")
            st.session_state.disabled=True
        else:
            st.error("Leider falsch. Probiere es gerne noch einmal :x:")
    def question_2(self):
        question_2 = st.radio(
            "Welche Option ist kein String?",
            ["**'123'**", '**"Hallo"**', "**Hallo**", '**"123abc"**'],
            index=None,
            horizontal=True,
        )
        if question_2 == None:
            st.write("")
        elif question_2 == "**Hallo**":
            st.success(
                "Sehr gut, **Hallo** hat keine Anführungszeichen und wird daher nicht als String erkannt  :white_check_mark:. ")
            st.write(
                "Um einen String zu erstellen, musst du ihn mittels einfachen oder doppelten Anführungszeichen kennzeichen. Hier siehst du noch einmal ein Beispiel:")
            st.markdown('''
                   ``` 
                   string_hallo = "Hallo"
                   string_zahl= '123'
                   string_gemischt = "abc123"
                   ```
                   ''')
            st.session_state.disabled = True
        else:
            st.error("Leider falsch :x: Probiere es gerne noch einmal")

    def question_3(self):
        question_3 = st.number_input("Gib eine float Zahl zwischen 0.5 und 3.5 an.", value=None,
                                     placeholder="Gib eine Zahl zwischen 0.5 und 3.5 ein")
        if question_3 == None:
            st.write("")
        else:
            if question_3 >= 3.5:
                st.error("Leider falsch :x: Die Zahl muss kleiner als 3.5 sein ")
            elif question_3 <= 0.5:
                st.error("Leider falsch:x: Die Zahl muss grösser als 0.5 sein")
            else:
                st.success(
                    "Richtig. Denke daran, du kannst einen float entweder als Fliesskommazahl oder als Zahl mit einem kleinem f am Ende deklarieren :white_check_mark: ")
                st.markdown('''
                       ```
                       float_fliesskomma = 2.3
                       float_mit_kleinem_f = 3f
                       ```
                       ''')



    def question_4(self):
        st.markdown('''#### Übung zu den nicht primitiven Datentypen :balloon:''')
        solution=["Liste", "Tuple", "Dictionary"]
        options = st.multiselect(
            "Welche der genannten Datentypen sind *nicht primitive Datentypen* in Python?",
            ["Integer", "Liste", "Float", "String", "Tuple", "Dictionary","Boolean"],
        )
        if options ==[]:
            st.write("")
        else:
            if sorted(solution) == sorted(options):
                st.success("Korrekt. All diese Datentypen sind nicht primitive Datentypen :white_check_mark:")
            else:
                st.error("Leider nicht :x: versuche es gerne weiter")

        preview = st.checkbox("Falls du nicht weiter kommst, kannst du hier einen kurzen Blick in die Lösung werfen.")
        if preview:
            string= ""
            for ele in solution:
                string +=(ele + " ")
            st.write("Die Lösung ist: ", string)

    def question_5(self):
        st.markdown('''#### Übung zu dictionaries :balloon:''')
        st.markdown('''Ein wichtiger Datentyp in Python ist der Dictionary. Durch ihn können Daten einander zugeordnet werden, ähnlich wie ein echter Dictionaire, der dir ein Wort und eine Erklärung liefert.''')
        st.markdown('''Erstelle einen Dictionary mit dem Namen ```my_dict``` und gib ihm die Schlüssel ```name```, ```alter``` und ```hobby```. Die Werte sind ```Max```, ```18``` und ```Fussball```. Du kannst die Werte auch austauschen und durch eigene Werte ersetzen.''')
        input = st.text_input("Eine Variable my_dict vom Typ Dictionary mit den Schlüsseln name, alter und hobby und den Werten Max, 18 und Fussball", "my_dict = ...")
        pattern_1 = r'^my_dict\s*=\s*dict\(\s*name\s*=\s*"[^"]+"\s*,\s*alter\s*=\s*\d+\s*,\s*hobby\s*=\s*"[^"]+"\s*\)\s*$'
        pattern_2=r'^my_dict\s*=\s*dict\(\s*name\s*=\s*\'[^\']+\'\s*,\s*alter\s*=\s*\d+\s*,\s*hobby\s*=\s*\'[^\']+\'\s*\)\s*$'
        pattern_3=r'^my_dict\s*=\s*\{\s*"name"\s*:\s*"[^"]+"\s*,\s*"alter"\s*:\s*\d+\s*,\s*"hobby"\s*:\s*"[^"]+"\s*\}\s*$'
        pattern_4=r'^my_dict\s*=\s*\{\s*\'name\'\s*:\s*\'[^\']+\'\s*,\s*\'alter\'\s*:\s*\d+\s*,\s*\'hobby\'\s*:\s*\'[^\']+\'\s*\}\s*$'


        #if re.match(pattern_one_quotation, input) or re.match(pattern_two_quotations, input):
        if input=="" or input == "my_dict = ...":
            st.write("")
        else:
            if re.match(pattern_1,input)or re.match(pattern_2, input) or re.match(pattern_3, input) or re.match(pattern_4, input):
                st.success("Sehr gut, das stimmt :white_check_mark:")
                st.write("Super, da du jetzt weisst, wie man einen Dictionary erstellt, siehst du hier noch, wie man auf die Elemente zugreift und sie gegebenenfalls verändern kann:")
                st.markdown('''
                ```
                # Deklaration des dictionary
                my_dict = dict(name = "Max", alter = 18, hobby = "Fussball")
                
                # Um auf das Element mit dem Schlüssel "name" zuzugreifen: 
                name= my_dict.get("name")
                print(name)
                # Output: Max
                
                # Um alle Schlüssel (keys) zu erhalten: 
                keys = my_dict.keys()
                print(keys)
                #Output: dict_keys(['name', 'alter', 'hobby'])
                
                # Um auf alle Werte sehen zu können: 
                values = my_dict.values()
                print(values)
                #Output: dict_values(['Max', 18, 'Fussball'])
                
                # Um alle Items des Dictionary zu sehen: 
                items= my_dict.items()
                print(intems)
                #Output: dict_items([('name', 'Max'), ('alter', 18), ('hobby', 'Fussball')])
                
                # Um ein neues Schlüsses-Werte-Paar (key-value pair) hinzuzufügen:
                my_dict["lieblingsfarbe"] = "gelb"
                print(my_dict)
                #Output: {'name' : 'Max', 'alter' : 18, 'hobby' : 'Fussball', 'lieblingsfarbe' : 'gelb'}                
                ```
                ''')

            else:
                st.error("Das ist leider nicht korrekt :x:. Versuche es erneut. Falls du Hilfe brauchst, kannst du gerne googlen oder dir folgenden [Link](https://www.w3schools.com/python/python_dictionaries.asp) anschauen ")


    def exercise_2(self):
        self.question_4()
        self.question_5()

    def __main__(self):
        self.display_intro_teil_1()
        on_1 = st.toggle("Zeige die Übungsaufgaben zu den primitiven Datentypen :balloon:")
        if on_1:
            self.exercise_1()
        self.display_intro_teil_2()
        on_2= st.toggle("Zeige die Übungsaufgaben zu den nicht-primitiven Datentypen :balloon:")
        if on_2:
            self.exercise_2()


