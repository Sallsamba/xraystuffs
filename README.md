# BNP Product Recognition

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
J'ai utilisé le modèle pré-entraîné VGG16, un maximum de transfert learning, et j'ai entraîné mon propre modèle qui prend en entrée les features de sortie du réseaux pré-entraîné.
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

Je collabore avec Yanting. On a essayé de créer un dataset sympa. Finalement, on a abandonné l'API de Bing qu'on a utilisé la semaine dernière, à cause d'une limite de 35 images à télécharger. On a utilisé FatKun, une extension de Chrome, pour constituer notre dataset.


# BNP : Product Recognition

Cette application permet à un utilisateur de prendre une photo d'un objet qui, une fois reconnu par un algorithme de Computer Vision, lui sera proposé à l'achat à travers un financement 
par BNP Paribas et un site d'e-commerce partenaire.

## Installation et utilisation

Il faut avant tout installer les requirements  avec `pip install -r requirements.txt`.
Pour lancer l'application, il faut ensuite exécuter le fichier `GUI/train.py` qui va lancer l'interface graphique. 
Il suffit ensuite de charger son image (depuis l'ordinateur ou depuis une webcam).

## Features

L'application reconnaît pour l'instant (MVP) 9 types de produits différents. Si l'objet photographié n'est pas reconnu par l'algorithme, il est proposé à l'utilisateur de mettre à jour 
la base de données, pour qu'une fois celle-ci fournie, le modèle de Computer Vision puisse s'améliorer (et apprendre de nouvelles catégories).

Les tests ont montré une **précision (accuracy) d'environ 90%** sur la reconnaissance des produits déjà connus.

Les caractéristiques du produit reconnu sont : **son nom, son type (marque et/ou version), son prix** et une **image du produit neuf.**

L'application fournit une proposition de financement sous forme de paiement en plusieurs fois, à un taux de 1,3% et sur 12, 24, 36 ou 48 mois. 
Néanmoins, si le solde de l'utilisateur (ici fixé à 10 000 euros pour les besoins du MVP, dans une version ultérieure, l'utilisateur s'identifierait en lien avec son compte bancaire BNP) est inférieur
à la valeur du produit, le financement n'est pas proposé (pour des raisons de solvabilité).



## Auteurs

**Yanting Pan,**
**Samba Sall,**
**Hao Wang,**
**Chuyang Zeng**

En cas de bugs, merci de créer une Issue :)
