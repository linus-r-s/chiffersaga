import pytest
from dataclasses import asdict
from random import randint
from src.story import Episode
from src.chiffer import Caesar
from src.story import get_episode_by_number

def test_episode():
  e = get_episode_by_number(1)
  