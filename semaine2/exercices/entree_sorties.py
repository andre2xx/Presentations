###################################################
#Entrées: l'adresse IP, le masque de sous-réseau
#Sorties: Nombre de bits pour le réseau
# Nombre de bits pour les hôtes
# Nombre total d'adresses
# Nombre d'hôtes utilisables
#Formules: Nb_bits_reseau = Masque
# Nb_bits_hotes = 32- Masque
# Nb_adresses = 2 ** Nb_bits_hotes
# Nb_hotes_util = 2 ** Nb_bits_hotes - 2
# Adresse_IP, Masque Nb_bits_reseau
# Nb_bits_hotes
# Nb_adresses
# Nb_hotes_util
####################################################

def calculer_informations():
    """
    permet de calculer les informations selon une adresse ip et ensuite afficher les informations calculé
    :return:
    """
    adresse_ip = input("Entrer une adresse ip: ")
    masque = input("Entrer le masuqe de sous-réseau: ")
    nb_bit_reseau = masque
    nb_bits_hotes =32-masque
    nb_adresse = 2 ** nb_bits_hotes
    nb_hotes_util = 2 ** nb_bits_hotes -2

    print("Voici: ")











# if __name__ == "__main__":

