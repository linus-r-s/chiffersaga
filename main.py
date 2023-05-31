from flask import Flask, render_template
from src.chiffer import Cipher, Morse, Caesar
from src.story import get_episode_by_number
from src.generate import generate_squiggles, generate_pagoda
from src.util import get_random_word, get_random_from_category
from dataclasses import dataclass, asdict
from random import randint
import string
from itertools import cycle
import pytest

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', img=generate_pagoda('bakom coop kl 17'))

@app.route('/episode/<number>')
def episode(number):
  if number == '5':
    return render_template('final.html')
  episode = get_episode_by_number(number)
  if episode:
    return render_template('episode.html', episode=episode)
  else:
    return render_template('no_such_episode.html', number=number)
  
@app.route('/caesarkod')
def caesarkod():
  letters = string.ascii_uppercase + 'ÅÄÖ'
  return render_template('caesarkod.html', letters=letters)

@app.route('/morsekod')
def morse():
  m = Morse()
  return render_template('morse.html', alphabet=m.alphabet)

#pytest.main()
app.run(host='0.0.0.0', port=81, debug=True)
#pytest.main()