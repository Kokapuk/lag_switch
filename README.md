# Lag Switch

## Config

### preset

`"drop" | "lag"`

### lag
`{int}`: lag ms for `"lag"` `preset`

### hotkey.type

`"keyboard" | "mouse"`

### hotkey.input

`hotkey.type == "keyboard"`: one of following as string value https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key, for example `"alt_l"`

`hotkey.type == "mouse"`: `"left" | "right" | "middle" | "x1" | "x2"`

### hotkey.mode

`"toggle" | "push"`

### notifications.enabled

`true | false`

### notifications.volume

`0.0 - 1.0`
