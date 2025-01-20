import configparser
from typing import List
from models import Browser, BrowserProfile
from config import get_browsers_titles

def get_firefox_profiles(browser: Browser, path: str) -> List[BrowserProfile]:
    browser_titles = get_browsers_titles('firefox')

    name = browser['name']
    icon = browser['icon']
    title = browser_titles[name]

    profiles: List[BrowserProfile] = []

    config_file = f"{path}/profiles.ini"
    config = configparser.ConfigParser()
    config.read(config_file)

    for profile in config.sections():
        try:
            browser_profile = config.get(profile, "Name")

            profiles.append({
                "icon": {
                    "path": f"icons/{icon}"
                },
                "arg": f"{name} {browser_profile}",
                "subtitle": f"Open {title} using {browser_profile} profile.",
                "title": browser_profile,
            })

        except configparser.NoOptionError:
            pass

    return profiles
