from PIL import Image, ImageDraw, ImageFont
from itertools import cycle, accumulate, pairwise
import io
from base64 import b64encode
from dataclasses import dataclass


def encode(img):
  img_io = io.BytesIO()
  img.save(img_io, 'PNG')
  return 'data:image/png;base64,' + b64encode(
    img_io.getvalue()).decode('ascii')


def generate_keyframes(msg):
  blink_lengths = {'.': 1, '-': 3, ' ': 7}
  delays = []
  for i, char in enumerate(msg._list):
    for j, sign in enumerate(char):
      delays.append(blink_lengths[sign])
      if j != len(char) - 1:
        delays.append(blink_lengths['.'])
    if i != len(msg._list) - 1 and char != ' ':
      try:
        if msg._list[i + 1] == ' ':
          continue
      except IndexError:
        pass
      delays.append(blink_lengths['-'])

  acc_delays = accumulate(delays)
  sum_delays = sum(delays)
  percentages = []
  on = True
  for delay in delays:
    percentages.append(next(acc_delays) / sum_delays * 100)

  keyframes = '@keyframes morse {\n\t\t\t0% {opacity: 1;}\n'
  for p in percentages:
    on = not on
    keyframes += f'\t\t\t{int(p)}% {{ opacity: {int(on)}; }}\n'
  keyframes += '\n}'
  return {'kf': keyframes, 'length': sum_delays}


def generate_pagoda(msg):
  im = Image.new('RGB', (1200, 100), color="whitesmoke")
  font = ImageFont.truetype('pagod.ttf', 54)
  draw = ImageDraw.Draw(im)
  draw.text((10, 20), msg, fill="#111", font=font)
  return encode(im)


def generate_squiggles(msg) -> None:
  ''' 
  Generates a visual representation of a morse code. 
  TODO: Make a dict (or class!) for the symbols and create image after we know how long the message is.
  '''
  est_word_length = len(msg) * 120  # A symbol should be around 60 pixels wide (probably could get away with a little less.)
  directions = cycle(['right', 'down', 'right', 'up'])
  lengths = {'.': 30, '-': 90, ' ': 120}
  colors = cycle(['#dc322f', '#859900', '#6c71c4', '#268bd2', '#b58900'])
  x, y = 30, 150
  im = Image.new('RGB', (est_word_length + 60, 300), '#222')
  img1 = ImageDraw.Draw(im)
  w = 6
  for c in msg:
    color = next(colors, 'white')
    # img1.ellipse([(x-5, y-5), (x+5, y+5)], fill=color)
    for dl in c:
      if dl != ' ':
        current_dir = next(directions)
        if current_dir == 'right':
          new_x = x + lengths[dl]
          img1.line([(x, y), (new_x, y)], fill=color, width=w, joint='curve')
          x = new_x
        elif current_dir == 'left':
          new_x = x - lengths[dl]
          img1.line([(x, y), (new_x, y)], fill=color, width=w, joint='curve')
          x = new_x
        elif current_dir == 'up':
          new_y = y - lengths[dl]
          img1.line([(x, y), (x, new_y)], fill=color, width=w, joint='curve')
          y = new_y
        elif current_dir == 'down':
          new_y = y + lengths[dl]
          img1.line([(x, y), (x, new_y)], fill=color, width=w, joint='curve')
          y = new_y
      # img1.ellipse([(x-5, y-5), (x+5, y+5)], fill=color)
      else:
        x += lengths['-']
    x += lengths['.']
    y = 150

  dataurl = encode(im)
  return dataurl
