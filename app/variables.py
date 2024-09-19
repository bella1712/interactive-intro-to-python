import streamlit as st
import re
class Variables:
    def display_intro(self):
        st.title("Variablendeklaration")
        st.markdown('''## Variablen :wine_glass:''')
        st.markdown('''Was ist eine Variable? Du kannst dir wie kleine Boxen oder Container vorstellen, die einen Inhalt speichern können. Sie werden beim Programmieren verwendet, damit du nicht immer explizite Werte angeben musst und variabel programmieren kannst. Variablen sind sehr wichtig beim Programmieren, daher ist es auch wichtig ihnen einen sprechenden Namen zu geben. Der Inhalt der Variable ist zwar veränderlich, der Zweck ist aber in der Regel sicher. Daher benenne sie am besten auch danach. Als Beipsiel: 
            Zu Hause hast du Gläser, aus denen du trinken kannst. Das Glas ist ein Behälter für verschiedenen Flüssigkeiten: bevor du ein Glas kaufst musst du nicht wissen, ob du Wasser, Softdrinks, Cola oder irgendetwas anderes daraus trinken möchtest. Der Inhalt des Glases ist also variabel, die Funktion oder der Zweck des Glases ist aber immer gleich: Das Glas ist ein Auffangbehälter für Flüssigkeit.  
            Das Glas ist also in diesem Fall die Variable.
            Das oben genannte Beispiel sieht in Pyhton so aus:''')

        st.markdown('''    
        ```
        glas = "Wasser"
        print(glas)
        # Ausgabe: Wasser
         
        glas = "Saft"
        print(glas)
        # Ausgabe: Saft
        ```
        ''')
        st.write("Variablen werden immer klein geschrieben. Das ist eine Namenskonvention, an die du dich halten solltest, damit der Code übersichtlich und verständlich bleibt. ")
        on_1 = st.toggle("Versuche selbst eine Variable zu deklarieren :balloon:")
        if on_1:
            self.exercise_1()
        st.markdown('''#### Variablendeklaration''')
        st.markdown('''Varibalen können aber auch für Berechnungen verwendet werden. Angenommen ich möchte auf 5 Zählen, dann kann das in Python Code so aussehen:''')
        st.markdown('''
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
        ''')
        st.markdown('''Das ist allerding sehr umständlich, vorallem, wenn du später mit Schleifen arbeitest. Daher wird oft folgende Vorgehensweise verwendet:''')
        st.markdown('''    
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
            ''')
        st.markdown('''Du kannst also den Wert ein Variable mit dem Wert der Variable verändern. ''')
        on_2 = st.toggle("Wende dein gelerntes Wissen an :balloon:")
        if on_2:
            self.exercise_2()
    def exercise_1(self):
        st.markdown('''#### Übung 1 zur Variablendeklaration :balloon:''')
        st.markdown('''Deklariere eine Variable mit dem Namen **programmiersprache** und dem Wert **"Python"**''')
        options = st.multiselect(
            "Wie sieht die Variablen Deklaration aus",
            ['"','"', "programmiersprache", "Python", "="],
        )
        if options == []:
            st.write("")
        elif len(options)<4:
            st.error("Bitte benutze alle Elemente aus dem Dropdown um die Variable zu deklarieren")
        else:
            if options == ["programmiersprache", "=", '"',"Python",'"']:
                st.success('Das stimmt :white_check_mark: Die Deklaration sieht wie folgt aus: ```programmiersprache = "Python" ```')
                st.markdown('''''')
            else:
                st.error("Leider nicht :x: Probiere es weiter.")
            sneek_peek=st.checkbox("Falls du dir nicht sicher bist, findest du hier die Lösung")
            if sneek_peek:
                st.markdown('''Die Lösung ist: ```programmiersprache = "Python" ```''')
    def exercise_2(self):
        st.markdown('''#### Übung 2 zur Variablendeklaration :balloon:''')
        st.markdown('''Weise der Variable **zahl** den Wert 7 zu.''')
        declaration= st.text_input("Deklaration")
        if declaration==None or declaration=="":
            st.write("")
        else:
            if declaration.split()==["zahl", "=", "7"] or declaration.split()==["zahl=", "7"] or declaration.split()==["zahl", "=7"] or declaration.split()==["zahl=7"]:
                st.success("Sehr gut, das stimmt :white_check_mark:")
                st.write("Da du die Deklaration der Variable gemeistert hast, kannst du sie nun auch verändern")
                self.exercise_3()

            else:
                st.error("Das ist leider nicht korrekt :x: Denke daran, dass Variablen klein geschreiben werden sollten. ")
    def exercise_3(self):
        st.markdown('''#### Übung 3 zur Variablendeklaration :balloon:''')
        st.markdown('''Addiere nun **13** zu **zahl** hinzu und speichere den neuen Wert auch wieder in der Variable **zahl**''')
        addition=st.text_input("Addition")
        if addition == None or addition =="":
            st.write("")
        else:
            pattern_1= r"zahl\s*=\s*zahl\s*\+\s*13"
            pattern_2= r"zahl\s*=\s*13\s*\+\s*zahl"
            pattern_3= r"zahl\s*\+=\s*13"
            if re.match(pattern_1, addition) or re.match(pattern_2, addition) or re.match(pattern_3, addition):
                st.success("Wow, du lernst echt schnell! Deine Antwort ist richtig :white_check_mark:")
            else:
                st.error("Leider falsch :x: Versuche es gerne weiter ")
            on =st.toggle("Falls du nicht weiter kommst, findest du hier die Lösung")
            if on:
                st.markdown('''Die Lösung ist ```zahl = zahl + 13```''')

    def __main__(self):
        self.display_intro()
