# BNP_productrecognition

Le projet consiste en la mise en place d'une application de reconnaissance de produits, qui permet, une fois un produit reconnu, de faire des propositions financières (de crédit) à l'utilisateur pour l'acheter.

## MVP : 

Le MVP doit permettre de : 

**Charger une image en vue de sa reconnaissance**

**A partir d'un dataset d'images spécifié à l'avance (par exemple 3 marques de téléphones différents, 3 marques de voitures différentes, 3 marques de canapés différentes, etc.), reconnaître la classe de l'objet**

**Une fois la classe de l'objet reconnue, aller sur un site spécialisé pour récupérer les caractéristiques de l'objet**

**Faire une proposition financière à l'utilisateur**

**Avoir une application conviviale à utiliser (GUI)**

### Samba Sall : 

Mon rôle était de programmer toute la partie machine learning du projet : choix du modèle, data-preprocessing, fine-tuning, fitting, et validation.
J'ai utilisé le modèle pré-entraîné VGGFace, un maximum de transfert learning, et j'ai entraîné mon propre modèle qui prend en entrée les features de sortie du réseaux pré-entraîné.
J'ai pu avoir une très bonne précision sur mes classes (~92%) pour les validations.
Toutefois, il faut garder en tête que le dataset est constitué d'objets assez différents visuellement (fait exprès pour le MVP) donc dans la réalité le taux pourrait baisser un peu (mais à mon avis pas trop... peut-être qu'on restera au dessus de 90% !!!)

### Hao Wang:

Ma partie consiste  à chercher des informations sur les produits détectés dans les sites d'e-commerce, une fois que j'obtiens les noms des produits qui viennent de Samba. Pour cela, 
j'extrais les informations (par exemple les prix, les formes, les couleurs, etc grace aux modules 'requests' et 'BeautifulSoup' ou 'lxml' pour analyser les sites. Plusieurs sites 
sont ainsi comparés. A la fin, une proposition financière est donnée basée sur les considérations de tous les facteurs des produits.

Si nécessaire, une visualisation des données est ajoutée dans le code pour montrer les résultats plus clairement pour les clients.


### Yanting PAN :

Ma partie consiste à créer un dataset d'images de 3 marques de téléphones différents, 3 marques de voitures différentes et 3 marques de canapés différentes. Chacun contient une centaine d'image.
Le programme va transférer le nom détecté à Samba pour la suite de programme. Si jamais l'objet n'est pas reconnue, une fonction va demander à l'utilisateur les caractéristiques, et l'ajouter à la base de données.

### Chuyang Zeng

Je collabore avec Yanting. On a essayé de créer un dataset sympa. Finalement, on a abandonné l'API de Bing qu'on a utilisé la semaine dernière, à cause d'une limite de 35 images à télécharger. On a utilisé FunKun, une extension de Chrome, pour constituer notre dataset.


