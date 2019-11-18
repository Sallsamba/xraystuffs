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

### Hao Wang:
Ma partie consiste  à chercher des informations sur les produits détectés dans les sites d'e-commerce, une fois que j'obtiens les noms des produits qui viennent de Samba. Pour cela, 
j'extrais les informations (par exemple les prix, les formes, les couleurs, etc grace aux modules 'requests' et 'BeautifulSoup' ou 'lxml' pour analyser les sites. Plusieurs sites 
sont ainsi comparés. A la fin, une proposition financière est donnée basée sur les considérations de tous les facteurs des produits.

Si nécessaire, une visualisation des données est ajoutée dans le code pour montrer les résultas plus clairement pour les clients.


### Yanting PAN :

Ma partie consiste à créer un dataset d'images de 3 marques de téléphones différents, 3 marques de voitures différentes et 3 marques de canapés différentes. Chacun contient une centaine d'image.
Le programme va transférer le nom détecté à Samba pour la suite de programme. Si jamais l'objet n'est pas reconnue, une fonction va demander à l'utilisateur les caractéristiques, et l'ajouter à la base de données.


##

### MVP : 

Le MVP doit permettre de : 

**Charger une image en vue de sa reconnaissance**

**A partir d'un dataset d'images spécifié à l'avance (par exemple 3 marques de téléphones différents, 3 marques de voitures différentes, 3 marques de canapés différentes, etc.), reconnaître la classe de l'objet**

**Une fois la classe de l'objet reconnue, aller sur un site spécialisé pour récupérer les caractéristiques de l'objet**

**Faire une proposition financière à l'utilisateur**

**Si jamais l'objet n'est pas reconnue, demander à l'utilisateur les caractéristiques, et l'ajouter à la base de données**