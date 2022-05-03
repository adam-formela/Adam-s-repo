from datetime import datetime


def format_date(birthday_arg):
    datetime_object = datetime.strptime(birthday_arg, '%Y-%m-%d')
    birth_date = datetime.date(datetime_object)
    return birth_date


def zodiac(date):
    birth_day = date.day
    birth_month = date.month
    if birth_month == 1:
        zodiac_sign = 'Capricorn' if (birth_day < 20) else 'Aquarius'
    elif birth_month == 2:
        zodiac_sign = 'Aquarius' if (birth_day < 19) else 'Pisces'
    elif birth_month == 3:
        zodiac_sign = 'Pisces' if (birth_day < 21) else 'Aries'
    elif birth_month == 4:
        zodiac_sign = 'Aries' if (birth_day < 20) else 'Taurus'
    elif birth_month == 5:
        zodiac_sign = 'Taurus' if (birth_day < 21) else 'Gemini'
    elif birth_month == 6:
        zodiac_sign = 'Gemini' if (birth_day < 21) else 'Cancer'
    elif birth_month == 7:
        zodiac_sign = 'Cancer' if (birth_day < 23) else 'Leo'
    elif birth_month == 8:
        zodiac_sign = 'Leo' if (birth_day < 23) else 'Virgo'
    elif birth_month == 9:
        zodiac_sign = 'Virgo' if (birth_day < 23) else 'Libra'
    elif birth_month == 10:
        zodiac_sign = 'Libra' if (birth_day < 23) else 'Scorpio'
    elif birth_month == 11:
        zodiac_sign = 'Scorpio' if (birth_day < 22) else 'Sagittarius'
    elif birth_month == 12:
        zodiac_sign = 'Sagittarius' if (birth_day < 22) else 'Capricorn'
    return zodiac_sign


def check_name(name):
    if not contains_number(name):
        if name.isalnum():
            name = name.capitalize()
            return name
        return False
    else:
        return False


def contains_number(value):
    for character in value:
        if character.isdigit():
            return True
    return False


def check_date(date):
    today = datetime.today()
    today = datetime.date(today)
    if date > today:
        return False
    else:
        return True


zodiac_dict = {
    "Aries": "../static/img/Aries.jpg",
    "Taurus": "../static/img/Taurus.jpg",
    "Gemini": "../static/img/Gemini.jpg",
    "Cancer": "../static/img/Cancer.jpg",
    "Leo": "../static/img/Leo.jpg",
    "Virgo": "../static/img/Virgo.jpg",
    "Libra": "../static/img/Libra.jpg",
    "Scorpio": "../static/img/Scorpio.jpg",
    "Sagittarius": "../static/img/Sagittarius.jpg",
    "Capricorn": "../static/img/Capricorn.jpg",
    "Aquarius": "../static/img/Aquarius.jpg",
    "Pisces": "../static/img/Pisces.jpg",
}