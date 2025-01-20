#!/usr/bin/env python3

import os
import json
from typing import List
from models import BrowserProfile
from config import get_browsers
from browsers import get_chromium_profiles, get_firefox_profiles, get_orion_profiles

def main() -> None:
    home = os.path.expanduser("~")
    supported_browsers = get_browsers()
    profiles: List[BrowserProfile] = []

    for browser in supported_browsers['orion']:
        if os.path.exists(browser['app']):
            path = f"{home}/{browser['path']}"
            prof = get_orion_profiles(browser, path)
            profiles.extend(prof)

    for browser in supported_browsers['firefox']:
        if os.path.exists(browser['app']):
            path = f"{home}/{browser['path']}"
            prof = get_firefox_profiles(browser, path)
            profiles.extend(prof)

    for browser in supported_browsers['chromium']:
        if os.path.exists(browser['app']):
            path = f"{home}/{browser['path']}"
            prof = get_chromium_profiles(browser, path)
            profiles.extend(prof)

    result = json.dumps({"items": profiles}, indent=2)
    print(result)

if __name__ == "__main__":
    main()
