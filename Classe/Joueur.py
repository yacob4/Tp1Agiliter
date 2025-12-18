# Classe/Joueur.py

class Joueur:
    def __init__(self, nom: str):
        self._nom = nom
        self._quetes = []  # list[Quete]

    def getNom(self) -> str:
        return self._nom

    def getQuetes(self):
        # on renvoie une copie (encapsulation)
        return tuple(self._quetes)

    def ajouterQuete(self, quete) -> None:
        if quete is None:
            return

        if quete in self._quetes:
            return

        # Si la quête appartient déjà à un autre joueur, on la détache d'abord
        ancien = quete.getJoueur()
        if ancien is not None and ancien is not self:
            ancien.retirerQuete(quete)

        # Ajout côté Joueur
        self._quetes.append(quete)

        # Mise à jour côté Quete (sans boucle)
        quete.setJoueurInternal(self)

    def retirerQuete(self, quete) -> None:
        if quete is None:
            return

        if quete in self._quetes:
            self._quetes.remove(quete)
            # Mise à jour côté Quete (sans boucle)
            if quete.getJoueur() is self:
                quete.setJoueurInternal(None)

    # méthode "interne" (équivalent package-private)
    def _ajouterQueteInternal(self, quete) -> None:
        if quete not in self._quetes:
            self._quetes.append(quete)

    def _retirerQueteInternal(self, quete) -> None:
        if quete in self._quetes:
            self._quetes.remove(quete)
