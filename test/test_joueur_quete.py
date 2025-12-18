import unittest

from Classe.Quete import Quete
from Classe.Joueur import Joueur


class TestAssociationJoueurQuete(unittest.TestCase):

    def test_quete_peut_etre_sans_joueur(self):
        q = Quete("Q1")
        self.assertIsNone(q.getJoueur())

    def test_ajouter_quete_chez_joueur_met_a_jour_les_deux_cotes(self):
        j = Joueur("Alice")
        q = Quete("Q1")

        j.ajouterQuete(q)

        self.assertEqual(j, q.getJoueur())
        self.assertIn(q, j.getQuetes())

    def test_retirer_quete_met_a_jour_les_deux_cotes(self):
        j = Joueur("Alice")
        q = Quete("Q1")
        j.ajouterQuete(q)

        j.retirerQuete(q)

        self.assertIsNone(q.getJoueur())
        self.assertNotIn(q, j.getQuetes())

    def test_une_quete_ne_peut_avoir_qu_un_joueur(self):
        j1 = Joueur("Alice")
        j2 = Joueur("Bob")
        q = Quete("Q1")

        j1.ajouterQuete(q)
        j2.ajouterQuete(q)  # transfert

        self.assertEqual(j2, q.getJoueur())
        self.assertNotIn(q, j1.getQuetes())
        self.assertIn(q, j2.getQuetes())

    def test_pas_de_doublon_si_on_ajoute_deux_fois(self):
        j = Joueur("Alice")
        q = Quete("Q1")

        j.ajouterQuete(q)
        j.ajouterQuete(q)

        self.assertEqual(1, len(j.getQuetes()))

    def test_attribuerJoueur_depuis_quete(self):
        j = Joueur("Alice")
        q = Quete("Q1")

        q.attribuerJoueur(j)

        self.assertEqual(j, q.getJoueur())
        self.assertIn(q, j.getQuetes())

    def test_attribuerJoueur_none_detache(self):
        j = Joueur("Alice")
        q = Quete("Q1")
        j.ajouterQuete(q)

        q.attribuerJoueur(None)

        self.assertIsNone(q.getJoueur())
        self.assertNotIn(q, j.getQuetes())


if __name__ == "__main__":
    unittest.main()
