import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_asettuu_oikein(self):

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.00)

    def test_saldo_vahenee_oikein_kun_rahat_riittaa(self):

        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.00)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):

        kortti = Maksukortti(100)

        kortti.ota_rahaa(200)

        self.assertEqual(kortti.saldo_euroina(),1.00)


    def test_metodi_palauttaa_true_jos_rahat_riittaa(self):

        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    def test_metodi_palauttaa_false_jos_rahat_ei_riita(self):

        kortti = Maksukortti(100)
    
        self.assertEqual(kortti.ota_rahaa(200), False)
