## 1.
a = "Python 2023"
b = "Python 2023"
c = "Python 2023"
def sub_A_and_B(a,b,c):
      test = id(a) == id(b) == id(c)
      print(test)
      print(f"a type is {type(a)} and hex value is {hex(id(a))}")
      print(f"b type is {type(b)} and hex value is {hex(id(b))}")
      print(f"c type is {type(c)} and hex value is {hex(id(c))}")
sub_A_and_B(a,b,c)
c = "Java 11"
print("After change it its : " ,end="")
sub_A_and_B(a,b,c)



### calculator :
print(f"This is simple calculator you can give me 2 numbers and operation from these:"
      f" + | - | * | / | ^ ")
first_number = float(input("First number : "))
second_number = float(input("Second number : "))
operation = input("Operation : ")
if operation == "+":
      print(f"The outcome is {first_number + second_number}")
elif operation == "-":
      print(f"The outcome is {first_number - second_number}")
elif operation == "*":
      print(f"The outcome is {first_number * second_number}")
elif operation == "/":
      print(f"The outcome is {first_number / second_number}")
elif operation == "^":
      print(f"The outcome is {first_number ** second_number}")
else:
      print("That is the wrong operation you loose")



## Diagram :
print("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: *")
anwser_1 = input(f"1. oglądanie telewizji/filmów/seriali\
                  2.czytanie książek/czasopism\
                  3.słuchanie muzyki\
                  4.spotkania z rodziną/przyjaciółmi\
                  5.podróżowanie\
                  6.uprawianie sportu\
                  7.inne, jakie?")
anwser_2 = input(
      """
      W jakich okolicznościach czytasz książki najczęściej? *
      Można zaznaczyć kilka odpowiedzi, po przecinku
      1.podczas podróży
      2.w czasie wolnym (po pracy, na urlopie)
      3.podczas pracy/nauki (to ich element)
      4.w ogóle nie czytam
      5. inne, jakie?
      """
)
anwser_3 = input(
      """
      Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? *
      Można udzielić jednej odpowiedzi.
      1.chęć poszerzenia wiedzy
      2.czytanie mnie relaksuje/odpręża
      3.fakt, że czytanie jest modne
      4.czytanie to moje hobby
      5.konieczność nauki w związku z wykonywaną pracą/studiami
      6.odczuwam presję rodziny/środowiska, żeby czytać
      7. inny, jaki?
      """
)
anwser_4 = input(
      """
      Po książki w jakiej formie sięgasz najczęściej? *
Można udzielić jednej odpowiedzi.
1.papierowej (tradycyjnej)
2.e-booki (książki elektroniczne) na komputerze
3.e-booki na tablecie/telefonie
4.e-booki na specjalnym czytniku (np. Kindle)
      """
)
anwser_4 = input(
      """
Ile książek czytasz średnio w ciągu roku? *
1. 0
2. żadnej w całości - jedynie fragmenty
3. 1
4. 2 lub 3
5. 4-10
6. powyżej 10
      """
)
anwser_4 = input(
      """
Jak często średnio czytasz książki? *
Można udzielić jednej odpowiedzi.
codziennie
raz w tygodniu
raz w miesiącu
raz na kilka miesięcy
raz na pół roku
raz na rok
wcale
      """
)
anwser_4 = input(
      """

      """
)
