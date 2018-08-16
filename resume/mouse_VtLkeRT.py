import pyautogui

def main():
    while (1):
        pyautogui.click(x=555, y=502, clicks=1, interval=0, button='left')
        pyautogui.click(x=555, y=732, clicks=1, interval=0, button='left')
        pyautogui.click(x=627, y=455, clicks=1, interval=0, button='left')
        pyautogui.click(x=595, y=823, clicks=1, interval=0, button='left')
if __name__ == "__main__": main()
