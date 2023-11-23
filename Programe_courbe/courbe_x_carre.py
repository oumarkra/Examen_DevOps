# KRA OUMAR Master I IA Janv2023
import matplotlib.pyplot as plt
import numpy as np

def tracer_courbe_x_carre():

    x = np.linspace(-10, 10, 100)  # Crée un tableau de 100 valeurs de -10 à 10

    # Calculer les valeurs y correspondantes à x^2
    y = x ** 2

    # Tracer la courbe
    plt.figure(figsize=(8, 6))  # Définir la taille de la figure
    plt.plot(x, y, label='y = x^2', color='blue')  # Tracer la courbe x^2 en bleu
    plt.title('Courbe d\'équation y = x^2')  # Titre du graphique
    plt.xlabel('x')  # Nom de l'axe x
    plt.ylabel('y')  # Nom de l'axe y
    plt.grid(True)  # Activer la grille
    plt.legend()  # Afficher la légende

    # Afficher le graphique
    plt.show()