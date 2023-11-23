# KRA OUMAR, Master I IA Janv2023
import matplotlib.pyplot as plt
import numpy as np

def tracer_courbe_x_cube():

    x = np.linspace(-10, 10, 100)  # Crée un tableau de 100 valeurs de -10 à 10

    # Calculer les valeurs y correspondantes à x^3
    y = x ** 3

    # Tracer la courbe
    plt.figure(figsize=(8, 6))  # Définir la taille de la figure
    plt.plot(x, y, label='y = x^3', color='red')  # Tracer la courbe x^3 en rouge
    plt.title('Courbe d\'équation y = x^3')  # Titre du graphique
    plt.xlabel('x')  # Nom de l'axe x
    plt.ylabel('y')  # Nom de l'axe y
    plt.grid(True)  # Activer la grille
    plt.legend()  # Afficher la légende

    # Afficher le graphique
    plt.show()