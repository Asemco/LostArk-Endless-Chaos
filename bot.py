from config import config
import pyautogui
import pydirectinput
import time
import random
from datetime import date
from pyscreeze import ImageNotFoundException
import traceback

pydirectinput.PAUSE = 0.05
newStates = {
    "status": "inCity",
    "abilities": [],
    "abilityScreenshots": [],
    "bossBarLocated": False,
    "clearCount": 0,
    "fullClearCount": 0,
    "moveTime": 0,
    "botStartTime": None,
    "instanceStartTime": None,
    "deathCount": 0,
    "healthPotCount": 0,
    "timeoutCount": 0,
    "goldPortalCount": 0,
    "purplePortalCount": 0,
    "badRunCount": 0,
    "gameRestartCount": 0,
    "gameCrashCount": 0,
    "gameOfflineCount": 0,
    "maxTime": -1,
    "floor3Mode": True,
    "multiCharacterModeState": [],
}

def main():
    print("Screen automation starting...")
    cycle_count = 0
    terra_count = 0
    gaia_count = 0
    
    while True:
        prev_x = None
        prev_y = None
        cycle_count += 1
        print(f"\n=== Cycle {cycle_count} ===")
        print(f"Gaia found: {gaia_count}, Terra found: {terra_count}")
        
        # Step 1a: Check for gaia_1.png or gaia_2.png
        gaia_1 = None
        gaia_2 = None
        try:
            gaia_1 = pyautogui.locateCenterOnScreen(
                ".\\screenshots\\gaia_1.png",
                confidence=0.9
            )
            if gaia_1 is not None:
                gaia_count += 1
        except Exception:
            pass
        
        try:
            gaia_2 = pyautogui.locateCenterOnScreen(
                ".\\screenshots\\gaia_2.png",
                confidence=0.9
            )
            if gaia_2 is not None:
                gaia_count += 1
        except Exception:
            pass
        
        # Step 1b: Check for gaia_1.png or gaia_2.png
        terra_1 = None
        terra_2 = None
        try:
            terra_1 = pyautogui.locateCenterOnScreen(
                ".\\screenshots\\terra_1.png",
                confidence=0.9
            )
            if terra_1 is not None:
                terra_count += 1
        except Exception:
            pass
        
        try:
            terra_2 = pyautogui.locateCenterOnScreen(
                ".\\screenshots\\terra_2.png",
                confidence=0.9
            )
            if terra_2 is not None:
                terra_count += 1
        except Exception:
            pass
        
        if gaia_1 is not None and gaia_2 is not None:
            print("Both Gaia found! Pausing and asking for input...")
            user_input = input("Found Gaia. Enter 1 to stop, or anything else to continue: ")
            if user_input == "1":
                print(f"Stopping script. Total cycles completed: {cycle_count}")
                break
            else:
                print("Continuing to next steps...")

        if gaia_1 is None or gaia_2 is None:
            print("Double Gaia not found. Continuing to check Terra.")

        if terra_1 is not None and terra_2 is not None:
            print("Both Terra found! Pausing and asking for input...")
            user_input = input("Found Terra. Enter 1 to stop, or anything else to continue: ")
            if user_input == "1":
                print(f"Stopping script. Total cycles completed: {cycle_count}")
                break
            else:
                print("Continuing to next steps...")

        if terra_1 is None or terra_2 is None:
            print("Double Terra not found. Continuing to check for other buttons...")
        
        # Step 2: Check for retry_button.png and click if found (repeat until found)
        while True:
            retry_button = None
            try:
                retry_button = pyautogui.locateCenterOnScreen(
                    ".\\screenshots\\retry_button.png",
                    confidence=0.8
                )
            except Exception:
                pass
            
            if retry_button is not None:
                print(f"Retry button found at {retry_button}. Clicking...")
                pydirectinput.click(x=retry_button[0], y=retry_button[1])
                sleep(100, 333)
                break
            else:
                print("Retry button not found. Retrying step 2...")
                sleep(100, 333)
        
        # Step 3: Check for tap_screen_button.png and click if found (repeat until found)
        while True:
            tap_screen_button = None
            forbidden_retry_button = None
            try:
                tap_screen_button = pyautogui.locateCenterOnScreen(
                    ".\\screenshots\\tap_screen_button.png",
                    confidence=0.8
                )
            except Exception:
                pass
            try:
                forbidden_retry_button = pyautogui.locateCenterOnScreen(
                    ".\\screenshots\\forbidden_retry_button.png",
                    confidence=0.8
                )
            except Exception:
                pass
            
            if tap_screen_button is not None:
                print(f"Tap screen button found at {tap_screen_button}. Clicking...")
                pydirectinput.click(x=tap_screen_button[0], y=tap_screen_button[1])
                prev_x=tap_screen_button[0]
                prev_y=tap_screen_button[1]
                sleep(1500, 1799)
                break
            if forbidden_retry_button is not None:
                print(f"Forbidden retry button found at {forbidden_retry_button}. Clicking...")
                pydirectinput.click(x=forbidden_retry_button[0], y=forbidden_retry_button[1])
                sleep(100, 222)
            else:
                print("Tap screen button not found. Retrying step 3...")
                sleep(100, 222)
        
        # Step 4: Check for skip_button.png and click repeatedly until not found
        while True:
            skip_button = None
            alsoRetryButton = None
            try:
                skip_button = pyautogui.locateCenterOnScreen(
                    ".\\screenshots\\skip_button.png",
                    confidence=0.8
                )
            except Exception:
                pass
            try:
                alsoRetryButton = pyautogui.locateCenterOnScreen(
                    ".\\screenshots\\retry_button.png",
                    confidence=0.8
                )
            except Exception:
                pass

            if skip_button is not None:
                print(f"Clicking on Skip Button!")
                for i in range(11):
                    pydirectinput.click(x=skip_button[0], y=skip_button[1])
                    sleep(100, 333)
            if alsoRetryButton is not None and skip_button is None:
                print("Skip button no longer found. Retry Button is on screen. Moving to next step...")
                sleep(100, 222)
                break
            else:
                print("Skip button not found and Retry Button not found. Clicking and Retrying step 4...")
                pydirectinput.click(prev_x, prev_y)
                sleep(100, 222)
        
        # Step 5: Check for tap_to_proceed_button.png and click repeatedly until not found
        while True:
            tap_to_proceed_button = None
            try:
                tap_to_proceed_button = pyautogui.locateCenterOnScreen(
                    ".\\screenshots\\tap_to_proceed_button.png",
                    confidence=0.8
                )
            except Exception:
                pass
            
            if tap_to_proceed_button is not None:
                # print(f"Tap to proceed button found at {tap_to_proceed_button}. Clicking...")
                pydirectinput.click(x=tap_to_proceed_button[0], y=tap_to_proceed_button[1])
                sleep(100, 222)
            else:
                print("Tap to proceed button no longer found. Cycle complete...")
                break
        
        print(f"Cycle {cycle_count} complete. Starting next cycle...")
        # sleep(1000, 2000)



def sleep(min, max):
    sleepTime = random.randint(min, max) / 1000.0
    if sleepTime < 0:
        return
    time.sleep(sleepTime)


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n))


if __name__ == "__main__":
    states = newStates.copy()
    main()
