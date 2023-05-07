"""Création d'un simple gestionnaire de tâche"""
import datetime


def inscription():
    utilisateur = input("quel est votre nom d'utilisateur ? ")
    mot_de_passe = input("quel est votre mot de passe ?")
    connection(utilisateur, mot_de_passe)
    return ( utilisateur, mot_de_passe )

def connection(utilisateur = None, mot_de_passe = None):
    print("Entrez vos codes")
    print()
    if utilisateur == None and mot_de_passe == None:
        utilisateur_nom = input("quel est votre nom d'utilisateur ? ")
        votre_mot_de_passe = input("quel est votre mot de passe ?")
        print("Bienvenue")
        gestionnaire()
    else:
        utilisateur_nom = input("quel est votre nom d'utilisateur ? ")
        votre_mot_de_passe = input("quel est votre mot de passe ?")
        if utilisateur_nom == utilisateur and votre_mot_de_passe == mot_de_passe:
            print("Bienvenue")
            gestionnaire()
        else:
            print("identitifiant incorrect")

def gestionnaire():
    jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    tache = {"lundi": "musculation", "mardi": "rendez vous chez le dentiste", "mercredi": "sortie à la piscine", "jeudi": "visite chez papy",
             "vendredi": "soirée entre pote", "samedi": "cours programmation", "dimanche": "repos"}
    print("Voici votre emploi du temps pour cette semaine.")
    maintenant = datetime.datetime.now()
    numero_jours = maintenant.weekday()
    print()
    print("aujourd'hui nous sommes",jours[numero_jours]," et votre activité du jour est un(e)",tache[jours[numero_jours]])





print("veuillez vous connecter ou vous inscrire si  s'il vous plaît.")
print()
choix = input("s'inscrire ou se connecter ")

if choix == "inscrire" or choix == "s'inscrire":
    inscription()
elif choix == "connecter":
    connection()



