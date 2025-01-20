from typing import Dict, TypedDict

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
