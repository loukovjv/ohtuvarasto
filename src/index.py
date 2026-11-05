"""Pääohjelma, joka demonstroi Varasto-luokan toimintaa."""

from varasto import Varasto


def tulosta_luonti_ja_getterit(mehua, olutta):
    """Tulostaa varastojen alkutilanteen ja oluen getterit."""
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def testaa_setterit(mehua):
    """Testaa mehuvaraston setteritoimintoja."""
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def testaa_virhetilanteet(olutta):
    """Testaa virhetilanteita ja poikkeustapauksia varastojen käytössä."""
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

    print("Varasto(100.0, 150.0):")
    ylivuoto = Varasto(100.0, 150.0)
    print(ylivuoto)

    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0):")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")


def testaa_otto_virheet(olutta, mehua):
    """Testaa liian suuria ottoja ja negatiivisia ottoja."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0):")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.ota_varastosta(-32.9):")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def main():
    """Pääohjelman suorituslohko."""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    tulosta_luonti_ja_getterit(mehua, olutta)
    testaa_setterit(mehua)
    testaa_virhetilanteet(olutta)
    testaa_otto_virheet(olutta, mehua)


if __name__ == "__main__":
    main()
