import random


def render_captcha_value(length):
    alphabet = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'
    word = random.sample(alphabet, length)
    return ''.join(word)
