import os
from typing import List
from models import Browser, BrowserProfile
from config import get_browsers_titles

def get_orion_profiles(browser: Browser, path: str) -> List[BrowserProfile]:
    browser_titles = get_browsers_titles('orion')

    name = browser['name']
    icon = browser['icon']
    title = browser_titles[name]

    profiles: List[BrowserProfile] = []

    if not os.path.isdir(path):
        return profiles

    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir.startswith("Orion - ") and dir.endswith(".app"):
                browser_profile = dir.replace("Orion - ", "").replace(".app", "")

                profiles.append({
                    "icon": {
                        "path": f"icons/{icon}"
                    },
                    "arg": f"{name} {root}/{dir}",
                    "subtitle": f"Open {title} using {browser_profile} profile.",
                    "title": browser_profile,
                })

    return profiles
