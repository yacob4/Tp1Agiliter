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

### Structure interne de la Quête

Une quête doit pouvoir stocker son état et évoluer dans le temps.

Pour cela, nous lui ajoutons :
- un **titre** (`String`)
- une **expérience** (`int`)
- un **constructeur**
- une méthode permettant de gagner de l’XP

```java
public class Quete {
    private String titre;
    private int xp;

    public Quete(String titre) {
        this.titre = titre;
        this.xp = 0;
    }

    public String getTitre() {
        return titre;
    }

    public int getXp() {
        return xp;
    }

    public void ajouterXP(int points) {
        if (points <= 0) return;
        xp += points;
    }
}
Avant d’ajouter de l’XP, nous vérifions que la valeur est valide.
Une quête ne peut progresser que par des actions positives.


Donner vie à une Quête
Notre guilde d’aventuriers est maintenant prête.
Il ne reste plus qu’à créer une véritable quête.

Dans BlueJ :

clic droit sur la classe Quete

choisir new Quete(String titre)

donner un nom à la quête


🎉 Félicitations !
Vous avez réussi à créer une classe et à l’instancier.

🏆 Vous gagnez 10 XP