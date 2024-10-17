import streamlit as st


class Applikationsaufbau_und_deployment:
    def display_general_info(self):
        st.title("Applikationsaufbau und Deployment :tada:")
        st.markdown('''In diesem Unterkapitel wird dir erklärt, wie eine Applikation in vielen Fällen aufgebaut ist. Als Beispiel dafür, kannst du dir diese Webseite ansehen: Eigentlich handelt es sich hierbei nämlich nicht um eine Webseite sondern eine Python Applikation, 
        deren Frontendkompnenten via Streamlit erstellt und deren Funktionalität im Backend implementiert wurde, und und welche deployed wurde. Falls dir die Begriffe **Frontend**, **Backend** oder **Deployment** dir nichts sagen, dann ist dieses Unterkapitel genau für dich. ''')
    def display_frontend_info(self):
        st.markdown('''## Frontend :fireworks:''')
        st.markdown('''Unter Frontend versteht man die Komponenten einer Applikation, die man tatsächlich sehen kann. Webseiten oder Applikationen werden visuell und benutzerfreundlich gestaltet. 
        Die Applikation, die ihr zur Zeit seht, wurde in Python geschrieben und das Frontend wurde mittels Streamlit geschaffen. In dieser Applikation wurde also ein Framework für das Design der Applikation verwendet.
        In vielen Fällen wird dies aber mit HTML und CSS gemacht. Vorallem durch CSS kann das Design und das Aussehen einer Applikation angepasst werden. Wenn dich das Thema mehr interessiert, 
        dann schau dir ruhig die folgenden [Kurse](https://www.codecademy.com/catalog/language/html-css) genauer an.  ''')


    def display_backend_info(self):
        st.markdown('''## Backend :page_with_curl:''')
        st.markdown('''Das Backend ist der Teil der Applikation, der nicht Sichtbar für den User ist. Hierbei wird die Funktionalität der Applikation sichergestellt. 
        Datenbankanbindungen werden hier realisiert und APIs (Application Programming Interfaces) werden gegebenenfalls angegragt. Im Backend können verschiedenste Sprachen verwendet werden. Python, Java, C++, etc. 
        Letzten Endes kommt es bei der Backendentwicklung nicht auf die Programmiersprachen drauf an. Es zählt lediglich, womit sich das Team am wohlsten fühlt und welche Programmiersprache sich am ehesten zur Realisierung der Funktionalität eignet. ''')


    def display_deployment_info(self):
        st.markdown('''## Deployment :outbox_tray:''')
        st.markdown('''Um eine Applikation für die breite Masse verfügbar zu machen, wird das sogenannte Deployment verwendet. Hierbei wird die Applikation auf einem Server gespeichert und verfügbar gemacht. 
         Oft wird dafür Webhosting verwendet. Dadurch kann eine Webseite über Netzwerke, wie das Internet, zur Verfügung gestellt werden indem eine bestimmte URL verwendet wird.''')

    def __main__(self):
        self.display_general_info()
        self.display_frontend_info()
        self.display_backend_info()
        self.display_deployment_info()