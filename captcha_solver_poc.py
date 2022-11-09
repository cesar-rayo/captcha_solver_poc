import os
from captcha_solver import CaptchaSolver

local = False

if local:
    solver = CaptchaSolver('browser')
    raw_data = open('./images/captcha_1.png', 'rb').read()
    print(solver.solve_captcha(raw_data))
else:
    solver = CaptchaSolver('2captcha', api_key=os.environ["TWOCAPTCHA_KEY"])
    raw_data = open('./images/captcha_1.png', 'rb').read()
    print(solver.solve_captcha(raw_data))
