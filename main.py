# On vous donne une list n, parcourez cette liste et affichez ses valeurs
import re


def display_list(ma_liste: list):
    for list_element in ma_liste:
        print(list_element)


#En python, les str sont egalement des tableau. des tableau de caractères
#Avec cette information, afficher chaque lettre d'une phrase donnée en parametre
def display_word_str(un_mot : str):
    print("TODO")

# Completez la fonction afin qu'elle puisse nous afficher les 100 premiers nombres entiers
def display_hundred_int():
    print("TODO")


# generez des nombres random, ajoutez les dans un tableau et faites la moyenne des notes.
# Si la note, est en dessous de 10 (exclu), affichez "Non admin", sinon, "admin"
def mention_moyenne():
    print("TODO")


# Affichez le nombre de voyelle que comporte un mot saisie par l'utilisateur
# Vous pouvez varier cet exercice en affichant le nombre de consonne
def display_number_voyelle():
    entered_str = input("Please enter something: ")
    voy_list = ['a', 'e', 'i', 'o', 'u', 'y']
    nb_voy = len(list(filter(lambda character: character in voy_list, list(entered_str))))
    nb_letters = len(re.findall(r'[a-zA-Z]', entered_str))
    return nb_letters - nb_voy


# Affichez la table de multiplication (jusque 10 inclus) d'un nombre saisie par l'utilisateur
# different de 0
def table_multiplication():
    entered_nb = int(input("Please enter something: "))
    if entered_nb > 10 or entered_nb < 1:
        return
    else:
       mult_table = ""
       for i in range(1,entered_nb+1):
           for j in range(1,10):
                mult_table += '{} x {} = {} \n'.format(i,j,i*j)
           mult_table += "\n"
       return mult_table


# Calculez la factorielle d'un nombre
# Pour rappel, la factorielle de 5 vaux (1*2*3*4*5)
def factorielle(n: int):
    if n < 0:
        n = abs(n)
    if n == 1:
        return n
    else:
        return n*factorielle(n-1)

if __name__ == "__main__":
 print(display_number_voyelle())