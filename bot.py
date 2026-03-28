from config import config
import pyautogui
import pydirectinput
import time
import random
from datetime import date
from pyscreeze import ImageNotFoundException
import traceback
import keyboard
from playsound import playsound

pydirectinput.PAUSE = 0.05
paused = False
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
    cloud_count = 0
    
    def pause_script():
        global paused
        paused = not paused
        if paused:
            print("Script paused. Press F12 to resume.")
        else:
            print("Script resumed.")
    
    keyboard.add_hotkey('f12', pause_script)
    
    while True:
        retry_coords = None
        tap_coords = None
        forbidden_coords = None
        skip_coords = None
        prev_x = None
        prev_y = None
        cycle_count += 1
        if paused:
            time.sleep(0.1)
            continue
        print(f"\n=== Cycle {cycle_count} === | Press F12 to pause/resume the script.")
        
        # Step 1a: Check for gaia_1.png or gaia_2.png
        gaia_1 = None
        gaia_2 = None
        try:
            gaia_1 = pyautogui.locateCenterOnScreen(
                ".\\screenshots\\gaia_1.png",
                confidence=0.8,
                grayscale=True
            )
            if gaia_1 is not None:
                gaia_count += 1
        except Exception:
            pass
        
        try:
            gaia_2 = pyautogui.locateCenterOnScreen(
                ".\\screenshots\\gaia_2.png",
                confidence=0.8,
                grayscale=True
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
                confidence=0.8,
                grayscale=True
            )
            if terra_1 is not None:
                terra_count += 1
        except Exception:
            pass
        
        try:
            terra_2 = pyautogui.locateCenterOnScreen(
                ".\\screenshots\\terra_2.png",
                confidence=0.8,
                grayscale=True
            )
            if terra_2 is not None:
                terra_count += 1
        except Exception:
            pass
        
        # Step 1c: Check for cloud_1.png or cloud_2.png
        cloud_1 = None
        cloud_2 = None
        try:
            cloud_1 = pyautogui.locateCenterOnScreen(
                ".\\screenshots\\cloud_1.png",
                confidence=0.8,
                grayscale=True
            )
            if cloud_1 is not None:
                cloud_count += 1
        except Exception:
            pass

        try:
            cloud_2 = pyautogui.locateCenterOnScreen(
                ".\\screenshots\\cloud_2.png",
                confidence=0.8,
                grayscale=True
            )
            if cloud_2 is not None:
                cloud_count += 1
        except Exception:
            pass

        if gaia_1 is not None and gaia_2 is not None:
            print("Both Gaia found! Pausing and asking for input...")
            playsound('ffxiv.mp3')
            user_input = input("Found Gaia. Enter 1 to stop, or anything else to continue: ")
            if user_input == "1":
                print(f"Stopping script. Total cycles completed: {cycle_count}")
                break
            else:
                print("Continuing to next steps...")

        # if gaia_1 is None or gaia_2 is None:
        #     print("Double Gaia not found. Continuing to check Terra.")

        if terra_1 is not None and terra_2 is not None:
            print("Both Terra found! Pausing and asking for input...")
            playsound('ffvi.mp3')
            user_input = input("Found Terra. Enter 1 to stop, or anything else to continue: ")
            if user_input == "1":
                print(f"Stopping script. Total cycles completed: {cycle_count}")
                break
            else:
                print("Continuing to next steps...")

        # if terra_1 is None or terra_2 is None:
        #     print("Double Terra not found. Continuing to check Cloud.")

        if cloud_1 is not None and cloud_2 is not None:
            print("Both Cloud found! Pausing and asking for input...")
            playsound('ffvii.mp3')
            user_input = input("Found Cloud. Enter 1 to stop, or anything else to continue: ")
            if user_input == "1":
                print(f"Stopping script. Total cycles completed: {cycle_count}")
                break
            else:
                print("Continuing to next steps...")

        # if cloud_1 is None or cloud_2 is None:
        #     print("Double Cloud not found. Continuing to check for other buttons...")

        print(f"Gaia found: {gaia_count}, Terra found: {terra_count}, Cloud found: {cloud_count}")

        # while True:
        #     if True == False:
        #         break
        
        # Step 2 combined: retry -> tap/forbidden -> skip (coords cached outside cycle)

        # find retry button once, click it, and cache coords
        while retry_coords is None:
            retry_coords = None
            try:
                retry_button = pyautogui.locateCenterOnScreen(
                    ".\\screenshots\\retry_button.png",
                    confidence=0.8
                )
            except Exception:
                retry_button = None

            if retry_button is not None:
                retry_coords = retry_button
                print(f"Retry button found at {retry_coords}.")
                if paused:
                    time.sleep(0.1)
                    continue
                pydirectinput.click(x=retry_coords[0], y=retry_coords[1])
                sleep(100, 333)

        # After retry click: repeatedly check for tap_screen_button and forbidden_retry_button
        while True:
            forbidden_coords = None
            tap_coords = None
            if paused:
                time.sleep(0.1)
                continue
            if tap_coords is None:
                try:
                    tap_screen_button = pyautogui.locateCenterOnScreen(
                        ".\\screenshots\\tap_screen_button.png",
                        confidence=0.8
                    )
                except Exception:
                    tap_screen_button = None

                if tap_screen_button is not None:
                    tap_coords = tap_screen_button

            if forbidden_coords is None:
                try:
                    forbidden_retry_button = pyautogui.locateCenterOnScreen(
                        ".\\screenshots\\forbidden_retry_button.png",
                        confidence=0.8
                    )
                except Exception:
                    forbidden_retry_button = None

                if forbidden_retry_button is not None:
                    forbidden_coords = forbidden_retry_button

            if forbidden_coords is not None:
                print(f"Forbidden retry button found at {forbidden_coords}.")
                pydirectinput.click(x=forbidden_coords[0], y=forbidden_coords[1])
                sleep(100, 222)
                continue

            if tap_coords is not None:
                print(f"Tap screen button found at {tap_coords}.")
                pydirectinput.click(x=tap_coords[0], y=tap_coords[1])
                sleep(150, 179)
                break

            sleep(100, 222)

        # Step 3 (part of combined sequence): locate skip button once and click repeatedly
        if paused:
            time.sleep(0.1)
            continue
        while skip_coords is None:
            try:
                skip_button = pyautogui.locateCenterOnScreen(
                    ".\\screenshots\\skip_button.png",
                    confidence=0.8
                )
            except Exception:
                skip_button = None
                
            tap_to_proceed = None
            retry_button = None
            if skip_button is not None:
                skip_coords = skip_button
                print(f"Skip button found at {skip_coords}.")
                while True:    
                    if paused:
                        time.sleep(0.1)
                        continue
                    pydirectinput.click(x=skip_coords[0], y=skip_coords[1])
                    try:
                        close_button = pyautogui.locateCenterOnScreen(
                            ".\\screenshots\\close_button.png",
                            confidence=0.8
                        )
                    except Exception:
                        close_button = None

                    try:
                        tap_to_proceed = pyautogui.locateCenterOnScreen(
                            ".\\screenshots\\tap_to_proceed_button.png",
                            confidence=0.8
                        )
                    except Exception:
                        tap_to_proceed = None

                    try:
                        retry_button = pyautogui.locateCenterOnScreen(
                            ".\\screenshots\\retry_button.png",
                            confidence=0.8
                        )
                    except Exception:
                        retry_button = None

                    if close_button is not None:
                        pydirectinput.click(x=close_button[0], y=close_button[1])
                    if tap_to_proceed is not None:
                        pydirectinput.click(x=skip_coords[0], y=skip_coords[1])
                    if retry_button is not None:
                        skip_coords = True
                        break

        print(f"Cycle {cycle_count} complete. Starting next cycle...")



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
