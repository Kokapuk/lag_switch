from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


from pygame import mixer
from config_manager import load_config
from os import path

mixer.init()
SOUND_ENABLE = mixer.Sound(path.abspath(
    path.join(__file__, '../resources/enable.mp3')))
SOUND_DISABLE = mixer.Sound(path.abspath(
    path.join(__file__, '../resources/disable.mp3')))

config = load_config()

SOUND_ENABLE.set_volume(config['notifications']['volume'])
SOUND_DISABLE.set_volume(config['notifications']['volume'])


def play_blocking_state_sound(blocking):
    if blocking:
        SOUND_ENABLE.play()
    else:
        SOUND_DISABLE.play()
