import random
import time


def login():
    num = random.randint(1000, 9999)
    service = random.choice(['ya', 'gmail', 'yahoo', 'mail'])
    domain = random.choice(['com', 'ru', 'net', 'de', 'cn', 'io'])
    login = f'testuser-{num}@{service}.{domain}'
    return login


def password():
    num = random.randint(2, 9)
    password = int(time.time()) * num
    password = str(password)
    return password[::-1]


def wrong_password():
    wrong_password = random.randint(1, 99999)
    return wrong_password