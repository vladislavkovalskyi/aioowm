from typing import Optional


async def language_handler(language: Optional[str] = "ru") -> str:
    """
    :param language: accepts language identifier (ru, en, fr)
    :return: True if lang in identifiers. False if lang not in identifiers
    """

    identifiers = ("af", "al", "ar", "az", "bg", "ca", "cz", "da", "de", "el", "en", "eu",
                   "fa", "fi", "fr", "gl", "he", "hi", "hr", "hu", "id", "it", "ja", "kr",
                   "la", "lt", "mk", "no", "nl", "pl", "pt", "pt_br", "ro", "ru", "sv", "se",
                   "sk", "sl", "sp", "es", "sr", "th", "tr", "ua", "uk", "vi", "zh_cn", "zn_tw",
                   "zu")

    if language.lower() not in identifiers:
        raise TypeError("Unknown language identifier!")
    else:
        return language.lower()