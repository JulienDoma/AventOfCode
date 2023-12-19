#################################### Part 1 ####################################
import pandas

df = pandas.read_csv("1data.csv",header=None)

list_numbers = []
for row in df[0]:
    new_list = [x for x in row if x.isdigit()]
    if len(new_list) == 1:
        new_list.append(new_list[0])
        list_numbers.append(new_list)
    else:
        list_numbers.append(new_list[::len(new_list)-1])

print("Résultat du challenge 1 : ", sum([int(x[0]+x[1]) for x in list_numbers]))



#################################### Part 2 ####################################

################## Code de test sur une simple chaîne ##################
# string = 'oneight'
# digits = {
#     "one":"o1e",
#     "two":"t2o",
#     "three":"t3e",
#     "four":"f4r",
#     "five":"f5e",
#     "six":"s6x",
#     "seven":"s7n",
#     "eight":"e8t",
#     "nine":"n9n",
# }
#
# for key in digits:
#     while key in string:
#         string = string.replace(key,digits[key])
# print(string)

# list_numbers = []
# new_list = [x for x in string if x.isdigit()]
# if len(new_list) == 1:
#     new_list.append(new_list[0])
#     list_numbers.append(new_list)
# else:
#     list_numbers.append(new_list[::len(new_list)-1])
# print(list_numbers)

################## Code de application à un df ##################
import pandas

df = pandas.read_csv("1data.csv",header=None)
digits = {
    "one":"o1e",
    "two":"t2o",
    "three":"t3e",
    "four":"f4r",
    "five":"f5e",
    "six":"s6x",
    "seven":"s7n",
    "eight":"e8t",
    "nine":"n9n",
}

# Parcours du DataFrame et création d'une nouvelle liste qui contient les lignes transformées grâce au replace
# While permet de supprimer toutes les intances d'un chiffre dans la chaîne (s'il trouve deux fois three par exemple, il remplacera deux fois par t3e)
# On remplace pas simplement par 1 2 ou 3 pour éviter l'overlapping de certaines chaînes de caractères (oneight par exemple)
# Ici le code va remplacer one par o1n et eight par e8t ce qui fait qu'on obtient bien o1e8t et on ne perd pas d'infos
# On applique cette logique à tout notre mappage
new_df = []
for row in df[0]:
    for key in digits:
        while key in row:
            row = row.replace(key, digits[key])
    new_df.append(row)

# Même solution que la Partie 1 une fois les lignes transformées
list_numbers = []
for item in new_df:
    new_list = [x for x in item if x.isdigit()]
    if len(new_list) == 1:
        new_list.append(new_list[0])
        list_numbers.append(new_list)
    else:
        list_numbers.append(new_list[::len(new_list)-1])

print("Résultat du challenge 2 : ",sum([int(x[0]+x[1]) for x in list_numbers]))
