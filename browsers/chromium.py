import os
import json
from typing import List
from models import Browser, BrowserProfile
from config import get_browsers_titles

def get_chromium_profiles(browser: Browser, path: str) -> List[BrowserProfile]:
    browser_titles = get_browsers_titles('chromium')

    name = browser['name']
    icon = browser['icon']
    title = browser_titles[name]

    profiles: List[BrowserProfile] = []

    if not os.path.isdir(path):
        return profiles

    folders = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

    for folder in folders:
        file = f"{path}/{folder}/Preferences"
        if folder != 'System Profile' and os.path.isfile(file):
            with open(file) as f:
                data = json.load(f)
                browser_profile = data['profile']['name']

                profiles.append({
                    "icon": {
                        "path": f"icons/{icon}"
                    },
                    "arg": f"{name} {folder}",
                    "subtitle": f"Open {title} using {browser_profile} profile.",
                    "title": browser_profile,
                })

    return profiles
