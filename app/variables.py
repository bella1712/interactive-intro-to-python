import streamlit as st
class Variables:
    def display_intro(self):
        st.title("Variablendeklaration")
        st.markdown('''## Variablen :wine_glass:''')
        st.markdown(''' Variablen kannst du dir wie kleine Boxen oder Container vorstellen, die einen Inhalt speichern können. Sie werden beim Programmieren verwendet, damit du nicht immer explizite Werte angeben musst und variabel programmieren kannst. 
            Wenn du beispielsweise zu Hause ein Glas hast, aus dem du trinkst, dann musst du auch nicht vorher bestimmen, ob da nur Wasser herein kommt, sondern du kannst auch andere Getränke wie Saft hineinfüllen. Ähnlich ist das mit Variablen. 
            Das oben genannte Beispiel sieht in Pyhton so aus:''')

        st.markdown('''    
        ```
            glas = "Wasser"
            print(glas)
            # Ausgabe: Wasser
            
            glas = "Saft"
            print(glas)
            # Ausgabe: Saft
            ```''')
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
            ```''')
        st.markdown('''Das ist allerding sehr umständlich, vorallem, wenn du später mit Schleifen arbeitest. Daher wird oft folgende Vorgehensweise verwendet:''')
        st.markdown('''    ```
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
            ```''')
        st.markdown('''Du kannst also den Wert ein Variable mit dem Wert der Variable verändern. ''')


    def __main__(self):
        self.display_intro()
