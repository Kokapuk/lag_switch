# Lag Switch

## Config

### preset

`"drop" | "lag"`

### lag

`{int}`: lag ms for `"lag"` `preset`

### ignore_channels

List of `ignore_channel`: channels to ignore while intercepting. By default configured to ignore discord (voices and streams) and steam (friends and activity)

### ignore_channel.port_range

`[int, int]`

### ignore_channel.protocols

List of pydivert protocols https://pythonhosted.org/pydivert/#pydivert.Protocol, e.g. `6` for TCP

### hotkey.type

`"keyboard" | "mouse"`

### hotkey.input

`hotkey.type == "keyboard"`: one of following as string value https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key, e.g. `"alt_l"` for left alt

`hotkey.type == "mouse"`: `"left" | "right" | "middle" | "x1" | "x2"`

### hotkey.mode

`"toggle" | "hold"`

### notifications.enabled

`true | false`

### notifications.volume

`0.0 - 1.0`
