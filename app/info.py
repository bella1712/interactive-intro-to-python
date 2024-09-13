import streamlit as st
class Info:

    def display_intro(self):
        st.title("Interaktive Einführung in Python :snake:")
        st.write("Dieses Repository soll dir eine kurze Einführung in das Programmieren mit Python geben. Du wirst lernen, welche Datentypen und Operatoren es gibt und wofür sie da sind. Ausserdem werdet wirst du lernen, was Variablen, Kontrollstrukturen und Schleifen sind. ")

        st.markdown('''
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
              ''')
        st.markdown('''
            ## Dein erstes Python Programm :triangular_flag_on_post:
            Da du jetzt die Grundlagen der Programmierung mit Python kennst, wird es Zeit dein erstes Programm zu programmieren. Denn wirklich gut im Programmeieren kannst du nur mit viel **Übung** werden. Also leg los und viel Spass!
              ''')



