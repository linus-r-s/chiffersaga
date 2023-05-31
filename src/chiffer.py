from dataclasses import dataclass
from src.generate import generate_pagoda, generate_squiggles, generate_keyframes
import string

class Cipher:
  def __repr__(self) -> str:
    try:
      if hasattr(self, 'key'):
        return f'<{self.__type__} type cipher with key {self.key}>'
      else:
        return f'<{self.__type__} type cipher.>'
    except:
      return '<Cipher of unknown type>'

class Anagram(Cipher):
  """ A mock class """
  __type__ = 'Anagram'
  def encrypt(self, msg):
    return 'Eranårkn AB'
    
class Pagoda(Cipher):
  __type__ = 'Pagoda'
  def encrypt(self, msg):
    return generate_pagoda(msg)

class Squiggle(Cipher):
  __type__ = 'Squiggle'
  def encrypt(self, msg):
    m = Morse()
    morse = m.encrypt(msg)  
    return generate_squiggles(morse._list)

class Caesar(Cipher):
    """Create a Caesar type cipher."""
    __type__ = 'Caesar'

    def __init__(self, key=0):
        self.key = key
        #self.logger = logging.getLogger(__name__)
        #self.logger.info(f'Created Caesar type cipher with key {self.key}.')

    def encrypt(self, message):
        """Return message encrypted with key."""
        uppers = string.ascii_uppercase + 'ÅÄÖ'
        lowers = string.ascii_lowercase + 'åäö'
        encrypted = ''
        for c in message:
          if c in uppers:
            encrypted += uppers[(uppers.index(c) + self.key) % len(uppers)]
            # encrypted += chr((int(ord(c)) - 146+self.key) % 26 + 65) 
          elif c in lowers:
            encrypted += lowers[(lowers.index(c) + self.key) % len(lowers)]
            # elif c.islower():
            #     encrypted += chr((int(ord(c)) - 97+self.key) % 26 + 97)
          else:
            encrypted += c
        return encrypted

    def decrypt(self, message):
        """Return message decrypted with key."""
        self.key = -self.key
        decrypted = self.encrypt(message)
        self.key = -self.key
        return decrypted

    def change_key(self, key):
        self.key = key

class Morse(Cipher):
  __type__ = 'Morse'

  alphabet = { 'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        'Å': '.--.-', 'Ä': '.-.-', 'Ö': '---.',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-', ' ': ' '}
  

  def encrypt(self, message: str):
    class Encrypted:
      _list = []
      _str = ''
      keyframes = ''
      length = ''

      def __repr__(self) -> str:
        return self._str

    encrypted = Encrypted()
    for c in message:
      m = self.alphabet.get(c.upper())
      encrypted._list.append(m)
      encrypted._str += f'{m} '
      #encrypted._str = encrypted._str.strip()
    encrypted.keyframes, encrypted.length = generate_keyframes(encrypted).values()
    return encrypted

  def decrypt(self, message) -> str:
    decrypted = ''
    for c in message:
      for k, v in self.alphabet.items():
        if c == v:
          decrypted += k
    return decrypted