import streamlit as st
from info import Info
from variables import Variables
from datentypen import Datentypen
from operatoren import Operatoren
from klassen_und_methoden import Klassen_und_Methoden
from kontrollstrukturen import Kontrollstrukturen
from schleifen import Schleifen
from applikationsaufbau_und_deployment import Applikationsaufbau_und_deployment
from htbuilder import HtmlElement, div, hr, a, p, img, styles
from htbuilder.units import percent, px


info = Info()
variables =Variables()
datentypen = Datentypen()
operatoren =Operatoren()
klassen_und_methoden = Klassen_und_Methoden()
kontrollstrukturen =Kontrollstrukturen()
schleifen = Schleifen()
app = Applikationsaufbau_und_deployment()
st.set_page_config(page_title="Python für Anfänger", layout="centered", initial_sidebar_state="expanded")

# Hide the default footer
hide_st_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made in ",
        image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
              width=px(25), height=px(25)),
        " with ❤️ by ",
        link("https://github.com/bella1712", "Isabella Freitag"),
    ]
    layout(*myargs)

def footer():
    myargs = [
        "Made in ",
        image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
              width=px(25), height=px(25)),
        " with ❤️ by ",
        link("https://github.com/bella1712", "Isabella Freitag"),
    ]
    layout(*myargs)

page_names_to_funcs = {
    "Informationsseite": info.display_intro,
    "Variablendeklaration": variables.__main__,
    "Datentypen": datentypen.__main__,
    "Operatoren": operatoren.__main__,
    "Kontrollstrukturen":kontrollstrukturen.__main__,
    "Schleifen":schleifen.__main__,
    "Klassen und Methoden":klassen_und_methoden.__main__,
    "Applikationsaufbau und Deployment": app.__main__,



}
task_name = st.sidebar.selectbox("Bitte wähle eine Seite aus :balloon:", page_names_to_funcs.keys())
page_names_to_funcs[task_name]()
footer()

