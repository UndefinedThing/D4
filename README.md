# D4

Projet Dev UF B2

## Sommaire

- Présentation de l'équipe
- Contexte du projet
- Solution Technique
- Fonctionnaltiés
- Problèmes rencontrés et solutions
- Bilan personnnel

## Présentation de l'équipe

Notre équipe est composé de 3 personnes :

- SALMI Pierre
- VICENTE Théo
- PETIT Martin

Nous sommes tous 3 étudiants en deuxiéme année d'informatique à Ynov Bordeaux.

## Contexte du projet

Dans le cadre du Projet Dev de notre 2nd année, un logicel pour montrer nos compétences dans ce domaine.

## Solution technique

Nous avons choisi de faire un serveur de matchmaking avec un jeu d'échec et une ChatRoom.

Le logiciel se compose d'un client lourd, composer d'une chat room et d'un jeu d'échec

## Fontionnalités

Le logiciel propose plusieurs fonctionnatiltés :

- Une page de connexion et d'enregistrement
- Une page d'accés aux compte de l'utlisateur connecté ainsi que a la création et acccés aux salles de jeu et chat disponible
- Une page de jeu d'échec avec un adversaire
- Une page de Chat pour parler avec les autres joueurs

## Problèmes rencontrés et solutions

- Base de données -> utilisation d'une base de donnée en local au niveau du serveur
- Message client/serveur -> utilisation d'une librairie python pour transformer la data en bytes pour la transférer
- Tkinter -> incomprehension de certain probleme lier à cette librairie python

## Installation

- Veuillez télécharger l'archive du projet
- Récupérez le dossier main
- Pour jouer en local, oubliez pas de changer l'adresse du serveur et du client dans ces 2 fichiers respectifs : [Network.py](./main/interfaceClient/Network.py) & [Server.py](./main/interfaceClient/Server.py) dans le dossier interfaceClient
- Pour jouer en ligne, oubliez pas de changer l'adresse du serveur et du client dans ces 2 fichiers respectifs : [Network.py](./main/interfaceClient/Network.py) & [Server.py](./main/interfaceClient/Server.py) dans le dossier interfaceClient
