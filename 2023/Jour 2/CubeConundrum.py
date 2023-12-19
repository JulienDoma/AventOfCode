#################################### Part 1 ####################################
import csv
import re

# On parcourt le fichier ligne par ligne et on découpe la ligne au niveau des : pour séparer l'id de game des tirages
dict_game = {}
with open('2data.csv') as file:
    lines = csv.reader(file, delimiter=":")
    for line in lines:
        dict_game[line[0]] = line[1]

# Pour chaque game dans le dictionnaire, on regarde tous les tirages, si le tirage contient 'blue'
# et qu'il est supérieur à la valeur maximale dans le dictionnaire de la partie, alors on remplace avec le nouveau tirage
# qui devient le nouveau max d'une couleur pour une partie donnée

# Une autre solution ici (plus simple) serait de simplement comparer la valeur du tirage avec la valeur max attendue
# Si jamais une des couleurs dépasse, alors on ne compte pas la partie et on passe à la suivante
# Néanmoins, avec cette méthode la partie 2 demande tout de même de faire les manipulations ci-dessous
for key in dict_game:
    dict_partie = {
        "blue" : 0,
        "red" : 0,
        "green" : 0
    }
    liste_des_tirages = re.split(';|,', dict_game[key])
    for tirage in liste_des_tirages:

        if "blue" in tirage:
            if dict_partie["blue"] < int(tirage.rstrip('blue').strip()):
                dict_partie["blue"] = int(tirage.rstrip('blue').strip())

        if "green" in tirage:
            if dict_partie["green"] < int(tirage.rstrip('green').strip()):
                dict_partie["green"] = int(tirage.rstrip('green').strip())

        if "red" in tirage:
            if dict_partie["red"] < int(tirage.rstrip('red').strip()):
                dict_partie["red"] = int(tirage.rstrip('red').strip())

    dict_game[key] = dict_partie

# On vérifie avec nos max de chaque tirage si les couleurs ne dépassent pas la valeur maximale attendue
list_id_possible = []
for game in dict_game:
    if dict_game[game]['red'] <= 12 and dict_game[game]['green'] <= 13 and dict_game[game]['blue'] <= 14:
        list_id_possible.append(int(game.lstrip('Game')))

print(sum(list_id_possible))

#################################### Part 2 ####################################

# On part du même dictionnaire final de la partie 1, sauf qu'on multiplie les max de chaque couleurs ensembles
# au lieu de vérifier leurs valeurs
power_of_games = []
for game in dict_game.values():
    power_of_games.append(eval(str(game['red']) + "*" + str(game['blue']) + "*" + str(game['green'])))

print(sum(power_of_games))
