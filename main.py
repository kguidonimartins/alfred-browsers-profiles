#!/usr/bin/env python3

import os
import json
import configparser
from typing import Dict, List, TypedDict, Optional

class BrowserProfile(TypedDict):
    icon: Dict[str, str]
    arg: str
    subtitle: str
    title: str

class Browser(TypedDict):
    name: str
    icon: str
    app: str
    path: str
    title: str

def get_browsers() -> Dict[str, List[Browser]]:
    f = open('browsers.json')
    supported_browsers = json.load(f)
    return supported_browsers

def get_browsers_titles(browser: str) -> Dict[str, str]:
    supported_browsers = get_browsers()
    titles: Dict[str, str] = {}
    for browser_info in supported_browsers[browser]:
        titles[browser_info['name']] = browser_info['title']
    return titles

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
                    "arg": f"'{name}' '{root}/{dir}'",
                    "subtitle": f"Open {title} using {browser_profile} profile.",
                    "title": browser_profile,
                })

    return profiles

def main() -> None:
    home = os.path.expanduser("~")
    supported_browsers = get_browsers()
    profiles: List[BrowserProfile] = []

    for browser in supported_browsers['chromium']:
        if os.path.exists(browser['app']):
            path = f"{home}/{browser['path']}"
            prof = get_chromium_profiles(browser, path)
            profiles.extend(prof)

    for browser in supported_browsers['firefox']:
        if os.path.exists(browser['app']):
            path = f"{home}/{browser['path']}"
            prof = get_firefox_profiles(browser, path)
            profiles.extend(prof)

    for browser in supported_browsers['orion']:
        if os.path.exists(browser['app']):
            path = f"{home}/{browser['path']}"
            prof = get_orion_profiles(browser, path)
            profiles.extend(prof)

    result = json.dumps({"items": profiles}, indent=2)
    print(result)

if __name__ == "__main__":
    main()
