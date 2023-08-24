from random import randint

code_length = 4

possibilities = ["a", "b", "c", "d", "e", "f"]
print(possibilities)

code = []

for _ in range(code_length):
    index = randint(0, len(possibilities)-1)
    value = possibilities[index]
    
    code.append(value)

# print(code)

answer = None

tries = 12

while answer != code and tries > 0:

    answer = input("Veuillez rentrer une séquence de " + str(code_length) + " lettres (a à f) : ")

    while len(answer) != code_length:
        print("Veuillez entrer le bon nombre de lettres.")
        answer = input("Veuillez rentrer une séquence de " + str(code_length) + " lettres (a à f) : ")
    
    answer = list(answer)

    # print(answer)

    correct_places = []

    for index in range(code_length):
        if code[index] == answer[index]:
            correct_places.append(index)

    print("Lettre(s) bien placée(s) : " + str(len(correct_places)))

    # print(correct_place)

    wrong_places = []

    for index_answer in range(len(answer)):
        for index_code in range(len(code)):
            if answer[index_answer] == code[index_code] and index_code not in correct_places and index_answer not in correct_places and index_code not in wrong_places:
                wrong_places.append(index_code)
                break
    
    print("Lettre(s) mal placée(s) : " + str(len(wrong_places)))

    # print(wrong_places)

    tries -= 1

    print("Il te reste " + str(tries) + " essai(s).")

if answer == code:
    print("Félicitations ! Tu as trouvé la bonne combinaison !")
else:
    print("Tu as perdu. La bonne réponse était " + str(code))