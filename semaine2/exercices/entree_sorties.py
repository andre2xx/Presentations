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

def calculer_parametres_sous_reseau():
    """
    permet de calculé les informations de masque de sous réseau
    :return:
    """
    adresse_ip = input("Entrer l'adresse ip : ")
    masque = input("entrer le maseque : ")

    nb_bits_reseau = masque
    nb_bits_hotes = 32 -masque
    nb_adresse = 2** nb_bits_hotes
    nb_hotes_util =2** nb_bits_hotes-2

    print(nb_bits_reseau)
    print(nb_bits_hotes)
    print(nb_adresse)
    print(nb_hotes_util)

calculer_parametres_sous_reseau()







