from Interface.ui import UI

'''
Lab 6
Se cere o soluție modulară cu arhitectura stratificata (ui, operations, domain)
Tratarea erorilor utilizând excepții
Specificații si teste; testele vor fi organizate în pachete/module corespunzătoare
Documentația va conține textul problemei și planul de iterații
Iterațiile precedente (prima iterație fiind Lab 5) vor fi disponibile pentru prezentare și trebuie sa corespundă cu planul de iterații; aceasta cerința este valabilă și pentru laboratoarele următoare
Începând cu acest laborator se va lucra în echipe de doua persoane; in caz exceptat (e.g. număr impar de studenți în semigrupa), echipa poate fi de trei persoane
Se cere implementarea tuturor funcțiilor CRUD (Create Read Update Delete) pe doua entități; e.g: adaugă, afiseaza, modifică, șterge studenți/probleme.

Lab 7 
Sa se modifice reprezentarea entităților de domeniu (de exemplu, film și client) astfel:
Una dintre entități (de exemplu, film) va fi reprezentata sub forma de lista, iar toate filmele vor fi reținute într-o lista
Cealaltă entitate (de exemplu, client) va fi reprezentata sub forma de tuple, iar toți clienții vor fi reținuti într-o mulțime (set) 
https://docs.python.org/3/tutorial/datastructures.html#sets 
https://docs.python.org/3/library/stdtypes.html#set  
Implementați o funcționalitate de căutare (sau filtrare) si una de sortare pentru fiecare entitate de domeniu. Exemple: căutare client după nume, filtrare filme după un gen, sortare cărți după titlu. 
'''


if __name__ == "__main__":
    app = UI()
    app.start()


