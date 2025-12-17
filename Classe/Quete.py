class Quete:
    def __init__(self, titre: str):
        self._titre = titre
        self._xp = 0
        self._recompense = None  # type: Recompense | None

    def getTitre(self) -> str:
        return self._titre

    def getXp(self) -> int:
        return self._xp

    def setTitre(self, titre: str) -> None:
        self._titre = titre

    def ajouterXp(self, points: int) -> None:
        if points > 0:
            self._xp += points

    def getRecompense(self):
        return self._recompense

    def xpTotalAvecBonus(self) -> int:
        return self._xp if self._recompense is None else self._xp + self._recompense.getBonusXp()

    def attribuerRecompense(self, nouvelle) -> None:
        # Même logique que Java: maintenir la relation bidirectionnelle Quete <-> Recompense
        if self._recompense is not nouvelle:
            if self._recompense is not None:
                ancienne = self._recompense
                self._recompense = None
                ancienne.setQueteInternal(None)

            self._recompense = nouvelle
            if nouvelle is not None:
                ancienne_quete = nouvelle.getQuete()
                if ancienne_quete is not None and ancienne_quete is not self:
                    ancienne_quete.attribuerRecompense(None)

                nouvelle.setQueteInternal(self)
