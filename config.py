import json
from typing import Dict, List
from models import Browser

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
