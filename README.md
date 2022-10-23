# Tectonic-Generator

## Qu'est ce que Tectonic ?

Et non, je ne parle pas de cette fameuse dance et encore moins des plaques, je parle d'un jeu de logique sur papier. Oui, comme le Suduku c'est ça. Donc le Tectonic (aussi appelé Suguru), est un puzzle, qui se présente sous forme d'une grille, où dans chaque case, il faut placer les nombres de 1 à 5.

Voici les régles : 
 - Des cases adjacentes ne peuvent avoir la même valeur (toutes directions)
 - Chaque block de n cases doit contenir tous les nombres de 1 à n

Laissez moi illustrer ces deux régles : 

Voici la situation : <img width="192" alt="image" src="https://user-images.githubusercontent.com/83453511/196713560-27283a80-08db-434f-b640-0dcb76bf328c.png">

Première chose : on peut remarquer qu'il y a un groupe de cases (représentés par des traits gras), qui ne contient qu'une seule case (celui de gauche). Par la deuxième régle, on est obligé de placer un 1 dans cette case.

On obtient donc ceci : ![image](https://user-images.githubusercontent.com/83453511/196714730-14f73380-1e4b-4337-94dc-54c127f6b15d.png)

Ensuite, on ne peut pas placer de 1 dans la case du milieu, en raison de la présence d'un 1 dans la case de gauche, on ne peut donc le placer que dans la case de droite (première régle).

![image](https://user-images.githubusercontent.com/83453511/196715232-81bf7d37-337b-4218-a8ee-65f327a7b3b7.png)

Il ne reste qu'une seule case à compléter, qui ne peut être qu'un 2 (deuxième régle).

On obtient donc la grille suivante : ![image](https://user-images.githubusercontent.com/83453511/196715551-639b5e95-dde7-4530-af71-01dd730c7be5.png)

## Quel est le but de mon projet ?

Etant très passionné par ce jeu, j'ai voulu créer un algorithme permettant de générer des grilles aléatoirement selon une taille de grille donnée.

Le programme se présente comme cela : 
![image](https://user-images.githubusercontent.com/83453511/196716254-ebc95f7c-66df-4b9f-85fc-c4459599627d.png)

Il est possible de sélectionner à droite la taille de la grille ainsi que de générer des grilles qui s'affichent à gauche de l'écran.
