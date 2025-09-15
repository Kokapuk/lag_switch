from config_manager import load_config
from sound_manager import play_enabled_state_sound
from log_manager import print_enabled_state
from input_manager import bind_hotkey
from handle_packets import handle_drop_packets, handle_lag_packets


config = load_config()

if config['hotkey']['mode'] == 'toggle':
    def toggle():
        global enabled
        enabled['value'] = not enabled['value']

        if config['notifications']['enabled']:
            play_enabled_state_sound(enabled['value'])

        print_enabled_state(enabled['value'])

    bind_hotkey(toggle)

elif config['hotkey']['mode'] == 'push':
    def set_enabled(new_enabled):
        global enabled
        enabled['value'] = new_enabled

        if config['notifications']['enabled']:
            play_enabled_state_sound(enabled['value'])

        print_enabled_state(enabled['value'])

    def on_press():
        set_enabled(True)

    def on_release():
        set_enabled(False)

    bind_hotkey(on_press, on_release)

enabled = {'value': False}

print_enabled_state(enabled['value'])

match config['preset']:
    case 'drop':
        handle_drop_packets(enabled)
    case 'lag':
        handle_lag_packets(enabled)
