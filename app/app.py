import streamlit as st
from info import Info
from variables import Variables
from datentypen import Datentypen
from operatoren import Operatoren
from klassen_und_methoden import  Klassen_und_Methoden
from kontrollstrukturen import Kontrollstrukturen
from schleifen import Schleifen

info = Info()
variables =Variables()
datentypen = Datentypen()
operatoren =Operatoren()
klassen_und_methoden = Klassen_und_Methoden()
kontrollstrukturen =Kontrollstrukturen()
schleifen = Schleifen()

page_names_to_funcs = {
    "Informationsseite": info.display_intro,
    "Variablendeklaration": variables.__main__,
    "Datentypen": datentypen.__main__,
    "Operatoren": operatoren.__main__,
    "Kontrollstrukturen":kontrollstrukturen.__main__,
    "Schleifen":schleifen.__main__,
    "Klassen und Methoden":klassen_und_methoden.__main__,



}
task_name = st.sidebar.selectbox("Bitte wähle eine Seite aus", page_names_to_funcs.keys())
page_names_to_funcs[task_name]()
