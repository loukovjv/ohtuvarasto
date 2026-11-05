"""Testimoduuli Varasto-luokan yksikkötesteille."""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Testiluokka Varasto-luokan toiminnan tarkistamiseen."""

    def setUp(self):
        """Alustaa testivaraston ennen jokaista testiä."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Testaa, että uuden varaston saldo on nolla."""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Testaa, että uudella varastolla on oikea tilavuus."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Testaa tavaran lisäämisen varastoon."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Testaa, että tavaran lisäys pienentää vapaan tilan määrää."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testaa, että varastosta ottaminen palauttaa oikean määrän tavaraa."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Testaa, että tavaran ottaminen varastosta vapauttaa tilaa."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus(self):
        """Testaa, että negatiivinen tilavuus nollataan."""
        v = Varasto(-5)
        self.assertAlmostEqual(v.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        """Testaa, että negatiivinen alkusaldo asetetaan nollaksi."""
        v = Varasto(10, -5)
        self.assertAlmostEqual(v.saldo, 0)

    def test_liian_suuri_alkusaldo(self):
        """Testaa, että tilavuutta suurempi alkusaldo rajataan tilavuuteen."""
        v = Varasto(10, 15)
        self.assertAlmostEqual(v.saldo, 10)

    def test_negatiivinen_lisays_ei_tee_mitaan(self):
        """Testaa, että negatiivinen lisäysmäärä ei muuta saldoa."""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_liikaa_tavaraa_tayttaa_varaston(self):
        """Testaa, että varastoa ei voi ylitäyttää lisäyksellä."""
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto_palauttaa_nollan(self):
        """Testaa, että negatiivinen otto palauttaa nollan eikä muuta saldoa."""
        saatu = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu, 0)

    def test_ota_enemman_kuin_varastossa_on(self):
        """Testaa, että varastosta ei voi ottaa enempää kuin siellä on."""
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijonoesitys(self):
        """Testaa varaston merkkijonoesityksen oikeellisuuden."""
        v = Varasto(10, 3)
        self.assertEqual(str(v), "saldo = 3, vielä tilaa 7")
