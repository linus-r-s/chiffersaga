from dataclasses import dataclass, field
from src.chiffer import Cipher, Pagoda, Caesar, Squiggle, Anagram, Morse


@dataclass
class Episode():
  number: int
  title: str
  text: str
  cipher: Cipher
  message: str
  encrypted: str = field(init=False)
  hints: list

  def __post_init__(self):
    self.encrypted = self.cipher.encrypt(self.message)


episodes = []

e1 = Episode(number=1,
             title='Avsnitt 1: En mystisk man',
             text='''
    Ni är på väg hem från skolan när ni får syn på en Mystisk Man. Ni följer efter honom en bit och ser att han tappar en papperslapp! När han försvunnit utom synhåll smyger ni er fram och tittar på lappen.
  ''',
             cipher=Pagoda(),
             message='bakom coop kl 17',
             hints=[
               'Ledtråd 1: Det verkar vara en plats och en tid...',
               'Ledtråd 2: Det är ett brädgårdschiffer.',
               'Ledtråd 3: Kolla på väggen till höger ovanför tavlan.',
               'Ledtråd 4: Första bokstaven är ett B...'
             ])

e2 = Episode(
  number=2,
  title='Avsnitt 2: Bakom Coop',
  text='''
    Ni sticker till Coop en stund innan tiden på lappen och snokar runt. Efter en stunds letande hittar ni några märkliga tecken som verkar vara ritade med gatukritor på en mur.
  ''',
  cipher=Squiggle(),
  message='det händer ikväll',
  hints=[
    'Ledtråd 1: Titta på vad tecknen består av.',
    'Ledtråd 2: De verkar bestå av långa och korta streck...',
    'Ledtråd 3: Något annat som består av långa och korta streck är ju morsekod.'
  ])

e3 = Episode(
  number=3,
  title='Avsnitt 3: Källaren',
  text='''
  Något skumt är i görningen! Ni gömmer er och väntar tills klockan blir 17. Mycket riktigt dyker den Mystiske Mannen upp och börjar, precis som ni gjorde alldeles nyss, att leta efter meddelandet. Till slut hittar han märkena på muren, avkodar dem och tvättar sedan bort dem.
  </p><p class="lh-copy">
  När den Mystiske Mannen går iväg smyger ni efter och snart ser ni honom gå in i en dörr som leder ner i en källare. På dörren står en skylt som verkar vara namnet på ett företag. Ni misstänker att namnet är en kod för något annat, men vad?
  ''',
  cipher=Anagram(),
  message='bankrånare',
  hints=[
    'Ledtråd 1: Koden är ett anagram, av en ganska enkel sort.',
    'Ledtråd 2: Det ska bli ett ord som beskriver vad de egentligen sysslar med.',
    'Ledtråd 3: Första bokstaven i ordet är B.',
    'Ledtråd 4: Andra bokstaven i ordet är A. Ser du vart det här är på väg?',
    'Ledtråd 5: Läs "Eranårkn AB" baklänges.'
  ])

e4 = Episode(number=4,
             title='Avsnitt 4: Den trasiga lampan',
             text='''
  Så de är bankrånare! Och de verkar ha ett rån på gång. Ni bestämmer er för att hänga kvar utanför källaren för att se vad som händer...
  </p><p class="lh-copy">Efter ett bra tag, när solen gått ned, ser ni hur en lampa i fönstret börjar blinka. Först tror ni den är trasig, men inser efter ett tag att den blinkar med ett återkommande mönster!
  ''',
             cipher=Morse(),
             message='skånebanken',
             hints=['Ledtråd 1: Ordet ska bli målet för rånet.'])

e4.hints.append(
  f'Ledtråd 2: Ni skriver ner blinkningarna och får då:<br><span class="code">{e4.encrypted._str}</span>'
)

episodes.append(e1)
episodes.append(e2)
episodes.append(e3)
episodes.append(e4)


def get_episode_by_number(number):
  for episode in episodes:
    if episode.number == int(number):
      return episode
  return False
