import streamlit as st
from execbox import execbox
class Kontrollstrukturen:
    def display_intro(self):
        st.markdown('''# Kontrollstrukturen :passport_control:''')
        st.markdown('''Mit Kontrollstrukturen können Programme Entscheidungen treffen. Das passiert mit *Wenn &rarr; dann* Aussagen. Nehmen wir beispielsweise eine Wegbeschreibung: Folge dem Strassenverlauf 100m. *Wenn* du diese Strecke absolviert hast *dann* biege links ab.
            Programme habe keinen eigenen Willen und brauchen klare Anweisungen um funktionieren zu können. Daher ist es wichtig, dass diese  *Wenn &rarr; dann* Anweisungen präzise sind. Angenommen, wie wollen das oben genannte Beispiel in Code umsetzen, dann sieht das in Python folgendermassen aus:
            ''')
        st.markdown('''
        ```
            if (gelaufener_weg == 100):
              turn_right = True
              
            else:
              countinue
              
        ```
            ''')
        st.markdown('''Dann gibt es aber noch Szenarien, in denen wir eine Zwischenüberlegung machen müssen. Wenn wir beispielsweise einen Unfall sehen, sollten wir anhalten und den Unfallbeteiligten in ihrer Notlage helfen. Für ein solches Szenario würden wir umgangssprachlich vermultich etwas sagen wie: "Wenn du 100 Meter gelaufen bist, dann biege rechts ab, andernfalls, wenn du einen Unfall siehst halte an und helfe den verletzten, sollten beide Szenarien nicht zutreffen, dann lauf einfach weiter. "
            In Pythoncode würde das wie folgt aussehen: ''')
        st.markdown('''
            ```
            if (gelaufener_weg == 100):
              turn_right = True
              
            elif(unfall_passiert == True):
              helfen = True
              break
              
            else:
              countinue
            ```''')
    def exercise_1(self):
        # Initial dataframe
        st.markdown('''#### Übung zu den Kontrollstrukturen :balloon:''')
        st.markdown(
            '''Du findest unten ein funktionierendes Beispiel einer Kontrollstruktur. Spiele damit und mit den verschiedenen Werten herum, um herauszufinden, wie sie funktioniert. Sollte die Syntax nicht mehr korrekt sein, lies die Fehlernachricht und versuche mir ihrer Hilfe den Fehler zu beheben. Sobald du Änderungen am Code vorgenommen hast, klicke auf den Apply- und auf den Run-Button um die Änderung sehen zu können. ''')

        execbox("""
        import streamlit as st
name=""
if name=="":
    st.write("Bitte gib der Variable name einen Wert.")
elif name=="Max":
    st.write("Der name ist Max")
else: 
    st.write("Der name ist nicht '' und auch nicht Max.")
                        """)
    def __main__(self):
        self.display_intro()
        on = st.toggle("Übe den Umgang mit Kontrollstrukturen")
        if on:
            self.exercise_1()