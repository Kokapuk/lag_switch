import pydivert
from config_manager import load_config
from sound_manager import play_blocking_state_sound
from log_manager import print_blocking_state
from input_manager import bind_hotkey

config = load_config()

if config['hotkey']['mode'] == 'toggle':
    def toggle():
        global blocking
        blocking = not blocking

        if config['notifications']['enabled']:
            play_blocking_state_sound(blocking)

        print_blocking_state(blocking)

    def on_press():
        toggle()

    bind_hotkey(on_press)
elif config['hotkey']['mode'] == 'push':
    def set_blocking(new_blocking):
        global blocking
        blocking = new_blocking

        if config['notifications']['enabled']:
            play_blocking_state_sound(blocking)

        print_blocking_state(blocking)

    def on_press():
        set_blocking(True)

    def on_release():
        set_blocking(False)

    bind_hotkey(on_press, on_release)

blocking = False

print_blocking_state(blocking)

with pydivert.WinDivert('outbound and ip.SrcAddr != 127.0.0.1') as w:
    for packet in w:
        if blocking:
            continue

        w.send(packet)
