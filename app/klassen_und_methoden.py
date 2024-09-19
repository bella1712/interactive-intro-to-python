import streamlit as st
class Klassen_und_Methoden:
    def display_intro_teil_1(self):
        st.markdown('''## Klassen und Methoden  :rocket:''')
        st.markdown('''
            Jetzt hast die Grundlagen des Codens fast alle erfasst. Nur noch ein Punkt fehlt: Ordnung.
            Code kann je nach Aufgabe sehr lang und unstruktriert werden. Um das zu vermeiden gibt es das sogenannte *Objekt orientierte Programmieren*. Hierbei wird der Code in Klassen und Methoden verteilt. Du kannst dir eine Klasse wie eine Schulklasse vorstellen: Jede Schulklasse hat einen Klassennamen, Schüler und eine Lehrperson. Das sind sogenannte Attribute. Sie definieren eine Klasse.
            Aber in jeder Schulklasse gibt es auch Aufgaben die gemacht werden müssen: lernen, tafel putzen, Stühle hochstellen, etc. Diese Aufgaben sind Methoden oder auch Funktionen.
            In Python Code sieht das wie folgt aus:''')
        st.markdown('''
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
            ''')
    def show_video(self):
        st.markdown("### Falls du Klassen und Methoden noch genauer erklärt bekommen möchtest, dann schaue dir gerne dieses Video an.")
        st.video("https://www.youtube.com/watch?v=i1uQgU7NOCw")
        st.write("Dieses [Video](https://www.youtube.com/watch?v=i1uQgU7NOCw) ist vom YouTube Kanal Coding Crashkurse")
    def __main__(self):
        self.display_intro_teil_1()
        toggle=st.toggle("Zeige ein zusätzliches Lernvideo :balloon:")
        if toggle:
            self.show_video()
