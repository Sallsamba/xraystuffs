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
