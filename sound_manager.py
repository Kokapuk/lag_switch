from os import environ, path
from config_manager import load_config

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer

mixer.init()
SOUND_ENABLE = mixer.Sound(path.abspath(
    path.join(__file__, '../resources/enable.mp3')))
SOUND_DISABLE = mixer.Sound(path.abspath(
    path.join(__file__, '../resources/disable.mp3')))

config = load_config()

SOUND_ENABLE.set_volume(config['notifications']['volume'])
SOUND_DISABLE.set_volume(config['notifications']['volume'])


def play_enabled_state_sound(enabled):
    if enabled:
        SOUND_ENABLE.play()
    else:
        SOUND_DISABLE.play()
