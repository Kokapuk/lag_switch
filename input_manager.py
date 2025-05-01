from pynput import mouse, keyboard
from config_manager import load_config

config = load_config()

if config['hotkey']['type'] == 'keyboard':
    hotkey = keyboard.Key[config['hotkey']['input']]
elif config['hotkey']['type'] == 'mouse':
    hotkey = mouse.Button[config['hotkey']['input']]


def bind_hotkey(on_press, on_release=None):
    is_hotkey_pressed = False

    def on_click(x, y, button, pressed):
        if button == hotkey:
            if pressed:
                on_press()
            elif on_release:
                on_release()

    def on_press_internal(key):
        nonlocal is_hotkey_pressed
        if key == hotkey and not is_hotkey_pressed:
            is_hotkey_pressed = True
            on_press()

    def on_release_internal(key):
        nonlocal is_hotkey_pressed
        if key == hotkey:
            is_hotkey_pressed = False

            if on_release:
                on_release()

    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

    keyboard_listener = keyboard.Listener(
        on_press=on_press_internal, on_release=on_release_internal)
    keyboard_listener.start()
