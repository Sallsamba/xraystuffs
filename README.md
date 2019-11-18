# BNP_productrecognition

### Samba Sall : 

L'idée est de faire une application qui détecte un objet sur une image en entrée, et propose à l'utilisateur de l'acheter ou le vendre sur un site partenaire (avec des infos en plus)

Pour faire de la reconnaissance d'objets dans un but "commercial", j'ai deux idées principales. 
Il s'agit dans tous les cas d'utiliser un modèle pré-entraîné de Keras (exemple VGG), pour faire la détection d'objets.

Soit on se contente des **classes de ImageNet (1000 classes d'objets)**, soit on fait du **transfer learning pour gérer nos propres objets** (par exemple un magasin partenaire).
L'avantage du transfer learning c'est qu'on a plus de spécificité. L'inconvénient c'est qu'il faut gérer un dataset, et qu'il faut gérer un algorithme pour la reconnaissance à partir des features (k-NN c'est bof)


Notre application pourrait ensuite détecter la nature de l'objet dont on lui donne l'image. Ensuite, sur un site internet de e-commerce partenaire, un algorithme effectue les recherches par rapport à l'objet 
et fait à l'utilisateur des propositions financières pour l'acheter (où le vendre). Pourquoi pas du JavaScript ?

Les deux features sont totalement indépendantes, mais l'une se fait en Python, l'autre en JS, donc il faut un lien.