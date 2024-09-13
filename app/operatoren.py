import streamlit as st
class Operatoren:
    def display_intro_1(self):
        st.title("Operatoren :thought_balloon:")
        st.write("Operatoren werden verwendet um Zuweisungen zu machen oder Mathematische oder vergeleichende Operationen auszuführen.")
        st.markdown('''### Zuweisende Operatoren :arrow_right:''')
        st.markdown('''
            |Operator|	Beispiel|	Das Gleiche wie	| Beschreibung der Zuweisung|Rechenbeispiel mit x = 5 |
            |:---:|:---|:---|:---|:---|
            |=|	x = 5|	x = 5	|x hat den Wert 5| keine Rechnung |
            |+=	|x += 3	|x = x + 3	|x hat den Wert von (x + 3) |x = 5 + 3 &rarr; x = 8|
            |-=	|x -= 3	|x = x - 3	|x hat den Wert von (x - 3) |x = 5 - 3 &rarr; x = 2|
            |*=	|x *= 3	|x = x * 3	|x hat den Wert von (x * 3)|x = 5 * 3 &rarr; x = 2|
            |/=	|x /= 3	|x = x / 3	|x hat den Wert von (x / 3)|x = 5 / 3 &rarr; x = 2|
            |%=	|x %= 3	|x = x % 3	|x hat den Wert des Rests von (x / 3)|x = 5 % 3 &rarr; x = 2 <br>Weil 5 /3 (bzw. 5//3) ist gleich 1 mit Rest 2|
            |//=	|x //= 3	|x = x // 3	|x hat den Wert der Ganzzahldivision von (x / 3)|x = 5 // 3 &rarr; x = 1 <br>Weil die 3 nur 1 Mal ganz in die 5 passt|
            |**=	|x **= 3	|x = x ** 3	|x hat den Wert von x^{3}|x = 5 ** 3 &rarr; x =  125|
            |&=	x |&= 3	|x = x & 3	|x hat den Wert der bitweisen Andoperation von x & 3|x = 5 & 3 &rarr; x = 1 <br>Weil 5 binär = 101 und 3 binär 11 ist. Die And-Operation ergibt 1 weil 101 and 011 ist 001, was gleich 1 ist|
            |&#124;=|	x &#124;= 3	|x = x &#124; 3	|x hat den Wert der bitweisen Andoperation von x or 3|x = 5 &#124; 3 &rarr; x =7 <br>Weil 101 or 11 = 111, was gleich 7 ist |
            |^=	|x ^= 3	|x = x ^ 3	|x hat den Wert einer bitweise XOR Operation von x und 3|x = 5 ^ 3 &rarr; x = 6 <br>Weil 101 XOR 011 = 110 was gleich 6 ist|
            |>>=	|x >>= 3	|x = x >> 3	|x hat den Wert einer Bitverschiebung nach rechts um 3 Stellen|x = 5 >> 3 &rarr; x = 0 <br>Weil 0101 um 3 Stellen nach Rechts verschoben 0000 ist, was gleich 0 ist|
            |<<=|	x <<= 3	|x = x << 3	|x hat den Wert einer Bitverschiebung nach links um 3 Stellen)|x = 5 << 3 &rarr; x = 40 <br>Weil 0000101 um 3 Stellen nach links verschoben 101000 ist, was 40 ist|
            |:=|	print(x:=3)	|x = 3 print(x)|x hat den Wert 3|keine Rechnung|
            ''')

    def display_intro_2(self):
        st.markdown('''### Mathematische Operatoren :1234:''')
        st.markdown('''
            |Operator|	Name	|Beispiel|
            |:---:|:---|:---|
            |+	|Addition|	x + y	|
            |-	|Subtratkion|	x - y	|
            |*|	Multiplikation|	x * y	|
            |/|	Division|	x / y	|
            |%|	Modulo, der Rest, der nach einer Division übrig bleibt|	x % y	|
            |**|	Expoential|	x ** y	|
            |//|	Ganzzahliges Ergebnis nach einer Division (mit möglichem Rest)|	x // y	|
            ''')

    def display_intro_3(self):
        st.markdown('''### Vergleichsoperatoren :information_source:''')
        st.markdown('''
            |Operator|Name|	Beispiel	|
            |:---:|:---|:---|
            |==	|Gleich|	x == y|
            |!=|	Ungleich|	x != y|
            |>	|Grösser als|	x > y	|
            |<	|Kleiner als|	x < y	|
            |>=|	Grösser oder gleich wie|	x >= y|
            <=	|Grösser oder gleich wie|x <= y|
            ''')
    def __main__(self):
        self.display_intro_1()
        self.display_intro_2()
        self.display_intro_3()