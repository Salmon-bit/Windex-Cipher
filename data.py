import json

SAVE_FILE = "settings.json"
DEFAULT_DATA = {
        "windex_alphabet": "!AaBbCcDdEeFf123456",
        "main_alphabet": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789., !?:;@/\\|_+-'\"#₽&()*~`•√π÷×§∆£€$¢^°={}©®™✓[]<>абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСИУФХЦЧШЩЪЫЬЭЮЯ",
        "separator": ":"
}


def get_settings() -> dict:
    with open(SAVE_FILE, 'r', encoding="UTF-8") as f:
        data = json.load(f)
    
    return data


def save_settings(settings: dict) -> None:
    with open(SAVE_FILE, 'w', encoding="UTF-8") as f:
        json.dump(settings, f)


def save_default_data() -> None:
    with open(SAVE_FILE, 'w', encoding="UTF-8") as f:
        json.dump(DEFAULT_DATA, f)
