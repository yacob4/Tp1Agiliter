# 🏰 La Quête du Village Oublié

> 🧙‍♂️ *Dans un monde lointain, chaque action compte.*  
> *Une quête n’est jamais vide de sens : elle accumule de l’expérience…*  
> *et parfois, une récompense vient couronner l’effort.*

---

## 🗺️ Table des matières

- 🎬 [Introduction](#-introduction)
- 📜 [Chapitre 1 – Naissance d’une Quête](#-chapitre-1--naissance-dune-quête)
- 🔥 [Chapitre 2 – La Quête prend vie](#-chapitre-2--la-quête-prend-vie)
- 💎 [Chapitre 3 – L’apparition d’une Récompense](#-chapitre-3--lapparition-dune-récompense)
- 🔗 [Chapitre 4 – Le lien sacré](#-chapitre-4--le-lien-sacré)
- ⚔️ [Chapitre 5 – Le sauvetage du village](#-chapitre-5--le-sauvetage-du-village)
- ⚖️ [Chapitre 6 – Les sages écrivent les règles](#-chapitre-6--les-sages-écrivent-les-règles)

---

## 🎬 Introduction

Bienvenue, **aventurier du code**.

Ce tutoriel est une **aventure pédagogique** dont l’objectif est double :

- 🧠 comprendre la **programmation orientée objet**
- 🧪 apprendre à **tester et valider son monde** avec **des tests**

Chaque action réussie vous fera **gagner de l’XP**.  
Chaque erreur… vous apprendra quelque chose.

---

## 📜 Chapitre 1 – Naissance d’une Quête

Nous commençons notre aventure en créant notre **objet principal** :  
✨ **la Quête**.

Dans ce monde, une quête n’est pas un simple mot.  
Elle possède des caractéristiques bien précises :

- 🏷️ un **titre**
- ✨ une quantité d’**expérience (XP)** gagnée au fil des actions

---

### 🧱 Création de la classe `Quete`

Pour créer notre classe **Quete**, il suffit de :

1. Faire un **clic droit** dans BlueJ  
2. Choisir **Nouvelle classe**
3. Sélectionner :
   - **Langage** : Java  
   - **Type** : Classe  
   - **Nom** : `Quete`
📸 *Création de la classe `Quete` dans BlueJ*  

![Création de la classe Quete](photo/Image1.png)
Une fois la classe créée, nous devons la compiler.

concernant le code on retrouve le titre en string (chaine de caractère)
Puis l’EX en Int (nombre pas décimaux)
Un constructeur et l’encapsulation
Et enfin une méthode « ajouterXP » qui permet de gagner de
l’EX, pour cela on doit vérifier si on gagne de l’EX puis
l’ajouter a l’expérience déjà existante
![Création de la classe Quete en code !!](photo/Image2.png)
🧠 Pourquoi cette méthode ?
Avant d’ajouter de l’XP, nous vérifions que la valeur est valide.
Une quête ne peut progresser que par des actions positives.

🧙‍♂️ Naissance de la guilde d’aventuriers

À présent, notre guilde d’aventuriers est prête à créer des quêtes.

Mais comment donner vie à une quête ?

🔥 Instanciation d’une Quête

Dans BlueJ :

Clic droit sur la classe Quete

Choisir new Quete(String titre)

Donner un nom à la quête

![Création d'une Instance de Quete!!](photo/Image3.png)


🎉 Félicitations !
Vous avez réussi à créer une classe et à l’instancier.

🏆 Vous gagnez 10 XP