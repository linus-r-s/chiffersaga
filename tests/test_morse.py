from src.chiffer import Morse
from src.generate import generate_keyframes

def test_keyframes():
  m = Morse()
  enc = m.encrypt('an na anna')
  print(enc._list)
  print(enc.keyframes)
  print(enc.length)