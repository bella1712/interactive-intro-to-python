import streamlit as st
from execbox import execbox
class Schleifen:
    def display_info_1(self):
        st.markdown('''# Schleifen :arrows_counterclockwise:''')
        st.markdown(''' Du hast bis jetzt schon viele Grundlagen der Programmierung kennengelernt, aber um ein funktionierendes Programm schreiben zu können brauchst du noch das Wissen, was Schleifen sind. Generell erleichtern dir Schleifen das leben, weil sie es dir ermöglichen die Anzahl an Wiederholungen zu definieren. Das passiert entweder dadurch, dass du eine exakte Anzahl an Wiederholungen oder eine Abbruchbedingung definierst.
            Angenommen du hast 10 Mitschüler und du wünscht jedem einen guten Morgen. Nun sollst du diese Tätigkeit des Grüssens dokumentieren. Würdest du dann schreiben "Ich habe gesagt 'Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen.'"? Nein, oder?
            Du würdest schreiben "Ich habe 10 mal 'Guten Morgen' gesagt."
            In einem Programm musst du allerdings die 10fache Wiederholung durchführen und dafür verwendet man Schleifen: Dadurch ersparst du dir die Arbeit den Schritt mehrfach auszuführen und kannst alles in einer Struktur zusammenfassen.''')
        st.markdown('''#### For-Loops''')
        st.markdown('''Für die Strukturanpassung für die mehrfachen Wiederholungen verwenden wir Schleifen. Eine sehr bekannte, iterative, also zählende Schleife, ist der For-Loop. Hierbei wir eine Variable definiert, die zum Zählen der Wiederholungen verwendet wird diefiniert. Gleichzeitig wird mit dieser hoch- oder runterzählenden Variable eine Abbruchbedingung definiert. Z.B. solange die Variable kleiner als 10 ist, mache weiter. Beim Programmieren ist das genauso. Das oben genannte Beispiel sieht in Python folgendermassen aus:''')
        st.markdown('''
            ```
            for x in range(10):
              print("Guten Morgen")
            ```
            ''')
        on_1 = st.toggle("Übe For-Loops :balloon:")
        if on_1:
            self.exercise_1()
    def display_info_2(self):
        st.markdown('''#### While-Loops''')
        st.markdown('''Es gibt aber auch andere Möglichkeiten um eine Schleifen zu mache. Wenn du deine Mitschüler vorher zählst, kannst du schauen, wie ob du "Guten Morgen" sagen musst.''')
        st.markdown('''In python würde der Code dann wie folgt aussehen:''')
        st.markdown('''
        ```
        # Wenn du deine Mitschüler vorher zählen würdest:
        i = 0
        while i < anzahl_mitschueler:
            print("Guten Morgen")
            i += 1
        ```
              ''')

        st.markdown('''Du kannst es dir aber auch einfacher machen: In dem du dir die Klassenliste vornimmst. Dadurch weisst du einerseits, wie viele Mitschüler du hast, und andererseits kannst du sie direkt mit dem Namen ansprechen. 
        Ein Programmierbeispiel mit Python wäre, wenn du eine Liste deiner Mitschüler hättest und ihnen allen mit dem Namen "Guten Morgen" wünschen möchtest. Die Liste kann jederzeit angepasst werden. Daher gehst du nach der Länge der Liste vor: ''')
        st.markdown('''
        ```            
        # Falls du nach einer Liste mit den Namen deiner Mitschüler vorgehen würdest
        liste_mitschueler= ["Max", "Marie", "Sabrina", "Tim", "Nico", "Charlene"]
            
        j = 0
        while j < len(liste_mitschueler):
            print("Guten Morgen ", liste_mitschueler[j])
        ```
            ''')
        on_2 = st.toggle("Übe While-Loops :balloon:")
        if on_2:
            self.exercise_3()
    def display_info_3(self):
        st.markdown('''
            Dann gibt es noch eine letzte Schleifenart. Diese ist dafür da, falls du mindestens einen Durchlauf dieser Schleife erreichen möchtest. Sie nennt sich Do-While-Schleife, weil die meisten Programmiersprachen, hier ist Python die Ausnahme, einen Do-Block mit der Ausführung und einen While-Block mit der Abbruchbedingung definieren.
            Beispielsweise kann es sein, dass all deine Mitschüler krank sind, du sie also nicht begrüssen musst, aber deine Lehrerin da ist. Ihr musst du immer und auf jeden Fall einen "guten Morgen" wünschen. In so einem Fall kommt in Python folgender Code zum Einsatz:
          ''')
        st.markdown('''
        ```
        counter=0
        while True:
            print("Guten Morgen")
            counter+=1
            if counter < anzahl_mitschueler:
                continue           
            else: 
                break
        ```
            ''')
        on_3 = st.toggle("Übe Do-While-Loops :balloon:")
        if on_3:
            self.exercise_4()

    def exercise_1(self):
        st.markdown('''#### Übung zur For-Loop :balloon:''')
        st.markdown(
            '''Schaue dir an, wie For-Loops funktionieren. Mit diesem interaktiven Codeblock kannst du die Werte so anpassen, wie du es möchtest. Achte aber darauf, dass die Einrückung korrekt sein muss, damit die Schleifen Syntax stimmt. Du kannst die Zahlenrange und den Outputstring gerne verändern. Beobachte was passiert und versuche dir die Struktur zu merken. Wenn du möchtest, dass dein Output sichtbar wird oder bleibt, verwende bitte das ```st.write()``` wie vorgegeben. In einem normalen Programm würdest du hier einfach einen ```print()``` Befehl haben. ''')
        st.write("Sollte etwas schief gehen, dann bekommst du eine Fehlermeldung angezeigt, die dir hilft den Code zu reparieren.")
        # Draw an execbox with some initial text.
        execbox("""
        import streamlit as st
        
        
# Beispiel 1
for i in range(0,3):
    st.write("Hallo" ,i)
st.write ("i ist gleich: ", i)
    """)
        on = st.toggle("Hier findest du noch eine andere Art des For-Loops :balloon:")
        if on:
            self.exercise_2()

    def exercise_2(self):
        st.write("Ändere gerne die Elemente in der Liste ab und schau was passiert. Du kannst Elemente ändern, hinzufügen oder löschen. ")
        execbox("""
        import streamlit as st
# Beispiel 2:
schueler_liste=["Max", "Moritz", "Melanie", "Marta"]
for schueler in schueler_liste:
    st.write(schueler, schueler_liste.index(schueler))
        """)
    def exercise_3(self):
        st.markdown('''#### Übung zu den While-Loops :balloon:''')
        st.markdown('''schau dir die While Schleife an und überlege dir, wie sie funktionert. Ändere gerne die Abbruchbedingung ```counter < len(schueler_liste)``` um zu sehen was passiert. Du darfst auch gerne die Rechnung des Counters ```counter += 1``` verändern und schauen was passiert. Falls du eine Unendliche Schleife bekommen solltest, keine Panik: **Lade einfach die Seite neu**. Und solltest du einen Syntax-Fehler machen, dann lass dir wieder durch die Fehlermeldung helfen. ''')

        execbox("""
        import streamlit as st
        
        
schueler_liste=["Max", "Moritz", "Melanie", "Marta"]
counter = 0
while counter < len(schueler_liste):
    st.write(schueler_liste[counter], counter)
    counter += 1
st.write("Counter: ", counter)
                """)

    def exercise_4(self):
        st.markdown('''#### Übung zu den Do-While-Loops :balloon:''')
        st.markdown('''schau dir die While Schleife an und überlege dir, wie sie funktionert. Ändere gerne die Abbruchbedingung ```counter < listen_laenge``` um zu sehen was passiert. Du darfst auch gerne die Rechnung des Counters ```counter += 1``` verändern und schauen was passiert. Falls du eine Unendliche Schleife bekommen solltest, keine Panik: **Lade einfach die Seite neu**. Und solltest du einen Syntax-Fehler machen, dann lass dir wieder durch die Fehlermeldung helfen.''')
        execbox("""
        import streamlit as st
                        
schueler_liste=["Max", "Moritz", "Melanie", "Marta"]
listen_laenge = len(schueler_liste)   
counter=0                   
while(True):
    st.write(schueler_liste[counter])
    counter+=1
    if(counter < listen_laenge):
        continue
    else:
        break
                        """)
    def __main__(self):
        self.display_info_1()
        self.display_info_2()
        self.display_info_3()
