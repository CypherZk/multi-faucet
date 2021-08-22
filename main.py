import time
import pyautogui
from pynput.keyboard import Key, Controller

_faucet = ['arrrtip faucet', 'kmdtip faucet', 'beantip faucet', 'tkltip faucet', 'clctip faucet', 'vrsctip faucet', 'katztip faucet'
, 'nmdtip faucet', 'edgtip faucet', 'raintip faucet', 'gptip faucet', 'chipstip faucet', 'postip faucet', 'zillatip faucet'
, 'xgctip faucet', 'mcltip faucet', 'gettip faucet']

keyboard = Controller()
key = "!"

time.sleep(5)
for f in _faucet:
    keyboard.press(key)
    keyboard.release(key)
    pyautogui.write(f)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.5)

pyautogui.alert('Done.')
