alphabet = ["a" , "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def chiffrer(message:str)->str:
    """
    chiffrer une mesage avec le decalage par 3
    :param message: message à chiffrer
    :return: message chiffrer
    """
    #message_chiffrer = ""
    #Pour chaque lettre dans message
    # trouer indice de lettre dans l'alphabet
    #nouvel_indice += 3
    #nouvelle_lettre = alphabet[nouvel_indice]
    #CONTATENER nouvelle_lettre DANS message_chiffre

    message_chiffre = ""
    for lettre in message:
        indice = alphabet.index(lettre)
        nouvel_indice = (indice + 3) % len(alphabet)
        nouvelle_lettre = alphabet[nouvel_indice]
        message_chiffre = message_chiffre + nouvelle_lettre



    return message_chiffre


def dechiffrer(message:str)->str:
    """
    decchifrerer une message chiffrer
    :param message: message chiffrer
    :return: message dechiffrer
    """
    message_dechiffre = ""
    for lettre in message:
        indice = alphabet.index(lettre)
        nouvel_indice = (indice - 3) % len(alphabet)
        nouvelle_lettre = alphabet[nouvel_indice]
        message_dechiffre = message_dechiffre + nouvelle_lettre

    return message_dechiffre

if __name__ == "__main__":
    print(chiffrer("basketball"))
    print(dechiffrer("aborskrqh"))