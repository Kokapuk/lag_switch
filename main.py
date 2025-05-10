import pydivert
from config_manager import load_config
from sound_manager import play_blocking_state_sound
from log_manager import print_blocking_state
from input_manager import bind_hotkey

ALLOWED_CHANNELS = [
    {"ports": range(50000, 65536), "protocols": [
        pydivert.Protocol.UDP]},  # DISCORD VOICES

    {"ports": range(27015, 27050), "protocols": [
        pydivert.Protocol.UDP, pydivert.Protocol.TCP]},  # STEAM FRIENDS AND ACTIVITY
]

config = load_config()

if config['hotkey']['mode'] == 'toggle':
    def toggle():
        global blocking
        blocking = not blocking

        if config['notifications']['enabled']:
            play_blocking_state_sound(blocking)

        print_blocking_state(blocking)

    bind_hotkey(toggle)

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

with pydivert.WinDivert("outbound and ip.SrcAddr != 127.0.0.1") as w:
    for packet in w:
        if not blocking:
            w.send(packet)
            continue

        for channel in ALLOWED_CHANNELS:
            if any(x == packet.protocol[0] for x in channel['protocols']) and packet.dst_port in channel['ports']:
                w.send(packet)
