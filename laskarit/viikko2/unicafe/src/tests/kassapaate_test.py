import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

#Kassapaate alustetaan oikein
    def test_kassan_saldo_alustetaan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_lounaat_alustetaan_oikein(self):
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_maukkaat_lounaat_alustetaan_oikein(self):
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_kassa_palauttaa_oikean_euromaaran(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

#Onnistunut käteisosto nostaa kassasaldoa oikein
    def test_edullisesta_veloitetaan_oikein_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukkaasta_veloitetaan_oikein_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

#Onnistunut käteisosto kasvattaam myytyjen määrää oikein
    def test_edullisen_kateismaksu_kasvattaa_myytyjä_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukkaan_kateismaksu_kasvattaa_myytyjä_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

#Onnistuneen käteisoston vaihtorahat oikein
    def test_edullisen_kateismaksun_vaihtorahat_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_maukkaan_kateismaksun_vaihtorahat_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)

#Epäonnistuneen käteisoston rahat palautetaan
    def test_edullisen_riittamattomat_rahat_palautetaan_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100),100)

    def test_maukkaan_riittamattomat_rahat_palautetaan_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100),100)

#Epaonnistunut käteisosto ei muuta myytyjä määriä
    def test_edullisen_epaonnistunut_osto_ei_muuta_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_epaonnistunut_osto_ei_muuta_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.maukkaat, 0)

#Epaonnistunut käteisosto ei muuta kassasaldoa
    def test_edullisen_epaonnistunut_osto_ei_muuta_kassasaldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_maukkaan_epaonnistunut_osto_ei_muuta_kassasaldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

#Korttiosto veloitetaan
    def test_edullisen_korttiosto_veloitetaan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 7.60)

    def test_maukkaan_korttiosto_veloitetaan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 6.00)

#Korttiosto palauttaa true onnistuessa
    def test_edullisen_onnistunut_korttiosto_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_maukkaan_onnistunut_korttiosto_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

#Korttiosto kasvattaa myytyjen määrää
    def test_edullinen_korttiosto_kasvattaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)    

    def test_maukas_korttiosto_kasvattaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)    

#Epäonnistunut korttiosto ei muuta kortin rahamäärää
    def test_epaonnistunut_edullinen_korttiosto_ei_muuta_kortin_arvoa(self):
        kortti = Maksukortti(5)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 0.05)

    def test_epaonnistunut_maukas_korttiosto_ei_muuta_kortin_arvoa(self):
        kortti = Maksukortti(5)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 0.05)

#Korttimaksun epäonnistuminen ei muuta myytyä määrää
    def test_epaonnistunut_edullinen_korttiosto_ei_muuta_myytyja(self):
        kortti = Maksukortti(5)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_epaonnistunut_maukas_korttiosto_ei_muuta_myytyja(self):
        kortti = Maksukortti(5)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)


#Epäonnistunut osto palauttaa false
    def test_epaonnistunut_edullinen_korttiosto_palauttaa_false(self):
        kortti = Maksukortti(5)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_epaonnistunut_maukas_korttiosto_palauttaa_false(self):
        kortti = Maksukortti(5)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

#Kortin lataus
    def test_korttia_ladatessa_kassan_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_korttia_ladatessa_kortin_saldo_kasvaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)

        self.assertEqual(kortti.saldo_euroina(), 10.00)
    
    def test_kortin_lataus_ei_toimi_negatiivisella_summalla(self):
        kortti = Maksukortti(0)

        self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
