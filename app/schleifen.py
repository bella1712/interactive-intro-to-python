import streamlit as st
class Schleifen:
    def display_info(self):
        st.markdown('''# Schleifen :arrows_counterclockwise:''')
        st.markdown(''' Du hast bis jetzt schon viele Grundlagen der Programmierung kennengelernt, aber um ein funktionierendes Programm schreiben zu können brauchst du noch das Wissen, was Schleifen sind. Generell erleichtern dir Schleifen das leben, weil sie es dir ermöglichen die Anzahl an Wiederholungen zu definieren. Das passiert entweder dadurch, dass du eine exakte Anzahl an Wiederholungen oder eine Abbruchbedingung definierst.
            Angenommen du hast 10 Mitschüler und du wünscht jedem einen guten Morgen. Nun sollst du diese Tätigkeit des Grüssens dokumentieren. Würdest du dann schreiben "Ich habe gesagt 'Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen, Guten Morgen.'"? Nein, oder?
            Du würdest schreiben "Ich habe 10 mal 'Guten Morgen' gesagt."
            In einem Programm musst du allerdings die 10fache Wiederholung durchführen und dafür verwendet man Schleifen: Dadurch ersparst du dir die Arbeit den Schritt mehrfach auszuführen und kannst alles in einer Struktur zusammenfassen.
            Beim Programmieren ist das genauso. Das oben genannte Beispiel sieht in Python folgendermassen aus:''')
        st.markdown('''
            ```
            for x in range(10):
              print("Guten Morgen")
            ```
            ''')
        st.markdown('''Es gibt aber auch andere Szenarien, in denen wir uns der Situation entsprechend anpassen müssen. Wenn einer deiner Mitschüler nicht da ist, musst du ihn nicht begrüssen. Daher würdest du solange "Guten Morgen" sagen, bis du keine Mitschüler mehr hast.
            In python würde der Code dann wie folgt aussehen:''')
        st.markdown('''
            ```
            # Wenn du deine Mitschüler vorher zählen würdest:
            while i< anzahl_mitschueler:
              print("Guten Morgen")
              i+=1
            
            # Falls du schaust ob es noch weitere Mitschüler gibt
            whle mitschueler.hasNext():
              print("Guten Morgen")
            ```
            ''')
        st.markdown('''
            Ansonsten gibt es noch eine letzte Schleifenart. Diese ist dafür da, falls du mindestens einen Durchlauf dieser Schleife erreichen möchtest. Beispielsweise kann es sein, dass all deine Mitschüler krank sind, du sie also nicht begrüssen musst, aber deine Lehrerin da ist. Ihr musst du immer und auf jeden Fall einen guten Morgen wünschen. In so einem Fall kommt in Python folgender Code zum Einsatz:
          ''')
        st.markdown('''            ```
            do {
              print("Guten Morgen")
              }
            while(mitschueler.hasNext());
            ```''')

    def __main__(self):
        self.display_info()