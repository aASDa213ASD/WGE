import vgamepad as vg

#########################################################
#            PYNPUT Library keys and buttons            #
#########################################################
#   This section lists all possible keyboard and mouse  #
#   key/button names available to be used.              #
#                                                       #
#   Special keys:                                       #
#       'alt', 'alt_l', 'alt_r', 'alt_gr',              #
#       'backspace', 'caps_lock', 'cmd',                #
#       'cmd_r', 'ctrl', 'ctrl_l', 'ctrl_r',            #
#       'delete', 'down', 'end', 'enter',               #
#       'esc', 'f1', 'f2', 'f3', 'f4', 'f5',            #
#       'f6', 'f7', 'f8', 'f9', 'f10', 'f11',           #
#       'f12', 'f13', 'f14', 'f15', 'f16', 'f17',       #
#       'f18', 'f19', 'f20', 'f21', 'f22', 'f23',       #
#       'f24', 'home', 'left', 'page_down', 'page_up',  #
#       'right', 'shift', 'shift_r', 'space', 'tab',    #
#       'up', 'media_play_pause', 'media_volume_mute',  #
#       'media_volume_down', 'media_volume_up',         #
#       'media_previous', 'media_next', 'insert',       #
#       'menu', 'num_lock', 'pause', 'print_screen',    #
#       'scroll_lock'                                   #
#                                                       #
#   Alphanumeric Keys:                                  #
#       'a', 'b', 'c', 'd', 'e', 'f',                   #
#       'g', 'h', 'i', 'j', 'k', 'l',                   #
#       'm', 'n', 'o', 'p', 'q', 'r',                   #
#       's', 't', 'u', 'v', 'w', 'x',                   #
#       'y', 'z', '0', '1', '2', '3',                   #
#       '4', '5', '6', '7', '8', '9'                    #
#                                                       #
#   Mouse buttons:                                      #
#       'unknown', 'left', 'middle',                    #
#       'right', 'x1', 'x2',                            #
#       'scroll_up', 'scroll_down',                     #
#       'scroll_left', 'scroll_right'                   #
#########################################################

#########################################################
#   - JOYCON_MIN / JOYCON_MAX are both determining      #
#     minimum and maximum values of a stick position.   #
#     Ideally you leave this as is since those values   #
#     are default for most known controllers out there. #
#     Default: -32768 / 32768                           #
#########################################################
JOYCON_MIN = -32768
JOYCON_MAX = 32768

#########################################################
#   - JOYCON_RIGHT_SENSITIVITY affects two factors      #
#     1. Sensitivity of your mouse movement correlated  #
#     to how fast a stick will reach it's maximum       #
#     or minimum position.                              #
#     2. Deadzone of mouse movement where stick will    #
#     simply not react until you move your mouse        #
#     far enough from origin position.                  #
#     Default: 300                                      #
#########################################################
JOYCON_RIGHT_SENSITIVITY = 150

#########################################################
#   - PAUSE_KEY obviously enough is responsible for     #
#     pausing the gamepad from listening both of your   #
#     mouse and keyboard, useful if you are alt tabing. #
#########################################################
PAUSE_KEY = 'caps_lock'

#########################################################
#   - HIDE_CURSOR_KEY is responsible for hiding or      #
#     showing the cursor through Windows API wrapper    #
#########################################################
HIDE_CURSOR_KEY = 'f1'

#########################################################
#   - MOUSE_KEYBINDS this section is bound to mouse     #
#     listener therefore it won't recognize any other   #
#     buttons except the mouse ones, here you can       #
#     redefine what each button do and bind any         #
#     XUSB_BUTTON of a gamepad.                         #
#########################################################
MOUSE_KEYBINDS = {
    'left': vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    'right': 'left_trigger',   # Left trigger method hook
    'middle': 'right_trigger', # Right trigger method hook
    'x1': 'calibrate',         # Right joycon calibration hook
}

#########################################################
#   - MOVEMENT_KEYBINDS this section is bound to        #
#     left joycon therefore it won't work with any      #
#     XUSB_BUTTON, here you can redefine your left      #
#     stick axes and bind any keyboard key.             #
#########################################################
MOVEMENT_KEYBINDS = {
    'w': {
        'method': 'set_axis',
        'axis': 'y',
        'value': JOYCON_MAX
    },
    'a': {
        'method': 'set_axis',
        'axis': 'x',
        'value': JOYCON_MIN
    },
    's': {
        'method': 'set_axis',
        'axis': 'y',
        'value': JOYCON_MIN
    },
    'd': {
        'method': 'set_axis',
        'axis': 'x',
        'value': JOYCON_MAX
    },
    'shift_r': {
        # Left joycon method hook, makes stick go only half-way in
        'method': 'switch_half_mode',
    },
}

#########################################################
#   - GENERAL_KEYBINDS this section is not bound to     #
#     any joycon, therefore it only recognizes          #
#     XUSB_BUTTON bound to a certain keyboard key       #
#     here you will hold most of your keyboard binds.   #
#########################################################
GENERAL_KEYBINDS = {
    'e': vg.XUSB_BUTTON.XUSB_GAMEPAD_B,            
    'm': vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,   
    'q': vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,  
    'r': vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    'z': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    'x': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    'c': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    'v': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    'shift': vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    'space': vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    'alt_l': vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
    'ctrl_l': vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    'ctrl_r': vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
}
