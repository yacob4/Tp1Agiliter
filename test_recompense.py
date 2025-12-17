import unittest

# On suppose que Quete et Recompense sont déjà importées / définies


class TestRecompense(unittest.TestCase):

    def setUp(self):
        self.quete = Quete("Vaincre le dragon")
        self.recompense = Recompense("Épée légendaire", 100)

    def test_getNom(self):
        self.assertEqual("Épée légendaire", self.recompense.getNom())

    def test_getBonusXp(self):
        self.assertEqual(100, self.recompense.getBonusXp())

    def test_getQuete_initialementNone(self):
        self.assertIsNone(self.recompense.getQuete())

    def test_lierRecompenseAQuete(self):
        self.quete.attribuerRecompense(self.recompense)
        self.assertEqual(self.quete, self.recompense.getQuete())

    def test_delierRecompenseDeQuete(self):
        self.quete.attribuerRecompense(self.recompense)
        self.quete.attribuerRecompense(None)
        self.assertIsNone(self.recompense.getQuete())

    def test_recompense_changeDeQuete(self):
        q1 = Quete("Q1")
        q2 = Quete("Q2")
        r = Recompense("Couronne", 50)

        q1.attribuerRecompense(r)
        q2.attribuerRecompense(r)

        self.assertIsNone(q1.getRecompense())
        self.assertEqual(q2, r.getQuete())


if __name__ == "__main__":
    unittest.main()
