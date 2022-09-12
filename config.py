from abilities import abilities

config = {
    "class": "arcana",
    "ilvl-endless": 1370,
    "ilvl-aor": 1445,
    "selectLevel": True,
    "floor3": False,
    "performance": False,
    "interact": "g",
    "move": "left",
    "blink": "space",
    "meleeAttack": "c",
    "awakening": "v",
    # "mageTouch": "",
    "healthPot": "f1",
    "healthPotAtPercent": 0.3,
    "useAwakening": True,
    "useSpeciality1": True,
    "useSpeciality2": True,
    "autoRepair": True,
    "shortcutEnterChaos": True,
    "useHealthPot": True,
    "usePotion": True,
    "regions": {
        "minimap": (1655, 170, 260, 200),  # (1700, 200, 125, 120)
        "abilities": (625, 779, 300, 155),
        "leaveMenu": (0, 154, 250, 300),
        "buffs": (625, 779, 300, 60),
        "center": (782, 353, 400, 350),
    },
    "screenResolutionX": 1920,
    "screenResolutionY": 1080,
    "clickableAreaX": 500,
    "clickableAreaY": 250,
    "screenCenterX": 960,
    "screenCenterY": 540,
    "minimapCenterX": 1772,
    "minimapCenterY": 272,
    "timeLimit": 360000,
    "blackScreenTimeLimit": 30000,
    "delayedStart": 3300,
    "healthCheckX": 690,
    "healthCheckY": 854,
}

config["abilities"] = abilities[config["class"]]
