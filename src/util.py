import json
from random import choice

categories = {
  'animals': [
    'apa', 
    'gorilla', 
    'häst', 
    'flodhäst', 
    'krokodil', 
    'giraff', 
    'blåval', 
    'hund',
    'katt',
    'uggla',
    'fisk',
    'skata',
    'haj',
    'lama',
    'kamel',
    'ko',
    'elefant',
    'myra',
    'björn',
    'lejon',
    'undulat',
    'lodjur',
    'valross',
    'säl',
    'spindel',
    'boaorm',
    'kobra',
    'örn',
    'groda',
    'igelkott',
    'råtta',
    'bäver',
    'surikat',
    'padda',
    'ödla'
            ],
  'cities': [
    'Malmö',
    'Göteborg',
    'Stockholm',
    'Norrköping',
    'Linköping',
    'Örebro',
    'Helsingborg',
    'Trelleborg',
    'Halmstad',
    'Umeå',
    'Sundsvall',
    'Växjö',
    'Borås',
    'Kristianstad',
    'Jönköping',
    'Kalmar',
    'Visby',
    'Falun',
    'Karlstad',
    'Uppsala',
    'Lund',
    'Västerås',
    'Eslöv'
           ]
}

def get_random_word():

  line_pos = json.load(open('data/words.json', 'r'))

  with open('data/svenska-ord.txt', 'r') as f:
      chosen_line = choice(list(line_pos.keys()))
      f.seek(line_pos[chosen_line])
      line = f.readline()
  return line.strip()

def get_random_from_category(c):
  return choice(categories.get(c))