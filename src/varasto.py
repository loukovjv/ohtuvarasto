"""Moduuli tarjoaa Varasto-luokan erilaisten nestemäärien ja
tilavuuksien hallintaan.
"""


class Varasto:
    """Luokka simuloi varastoa, jonne voi lisätä tavaraa ja 
    josta voi ottaa tavaraa."""

    def __init__(self, tilavuus, alku_saldo=0):
        """Alustaa varaston annetulla tilavuudella ja 
        valinnaisella alkusaldolla."""
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            self.saldo = 0.0
        elif alku_saldo <= self.tilavuus:
            self.saldo = alku_saldo
        else:
            self.saldo = self.tilavuus

    def paljonko_mahtuu(self):
        """Palauttaa tiedon siitä, kuinka paljon varastoon vielä mahtuu."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Lisää varastoon tavaraa annetun määrän."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Ottaa varastosta tavaraa annetun määrän ja palauttaa sen."""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara
        return maara

    def __str__(self):
        """Palauttaa varaston tilan merkkijonoesityksenä."""
        tilaa = self.paljonko_mahtuu()

        return f"saldo = {self.saldo}, vielä tilaa {tilaa}"
