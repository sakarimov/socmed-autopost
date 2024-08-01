import string
import secrets
from seleniumbase import SB
from faker import Faker

import re
import random
import os
import pyautogui
from datetime import datetime

fake = Faker()
marion = True
otp = 'otp'
data = 'numbers/bangladesh_try.txt'
country = 'BD'
country_code = '880'
agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
         (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")


f = open(data)
source = f.readlines()


def openPageUC(sb, url, dur):
    sb.driver.uc_open_with_reconnect(url, dur)


def humanCheckiframe(sb):
    sb.switch_to_frame("iframe")
    sb.driver.uc_click("span")


def clickHumanCheck(sb):
    if sb.is_element_visible("iframe"):
        sb.execute_script('document.querySelector("input").focus()')
        sb.send_keys("html", "\t")
        sb.driver.disconnect()
        pyautogui.press(" ")
        sb.driver.reconnect(4)


def filldataexclusivemarket(sb, data):
    try:
        sb.type('input#first_name', fake.first_name())
        sb.type('input#last_name', fake.last_name())
        sb.type('input#email', fake.pystr(15, 20).lower()+"@gmail.com")
        sb.select_option_by_value('select#country', country)
        sb.type('input#phone', data)
        sb.type('input#password', 'bajakuring')
        sb.type('input#confirmPassword', 'bajakuring')
        sb.click('input#flexCheckDefault')
        sb.click('button#submitregister')
    except Exception:
        raise Exception()


def generatepsw():
    opts = string.ascii_letters + string.digits + string.punctuation
    while True:
        psswd = ''.join(secrets.choice(opts) for i in range(12))
        if (sum(c.islower() for c in psswd) >= 2 and
            sum(c.isupper() for c in psswd) >= 2 and
            sum(c in string.punctuation for c in psswd) >= 2 and
                any(c.isdigit() for c in psswd)):
            break
    return psswd


def filldatatwitch(sb, data):
    try:
        sb.driver.uc_click(
            'button.ScCoreButton-sc-ocjdkq-0.ScCoreButtonPrimary-sc-ocjdkq-1.ljgEdo.gmCwLG')
        sb.sleep(1)
        sb.type('input#signup-username', fake.pystr(10, 15).lower())
        sb.type('input#password-input', generatepsw())
        sb.select_option_by_value(
            'select.ScInputBase-sc-vu7u7d-0.ScSelect-sc-gz38t2-0.iebopU.kxvSxQ.InjectLayout-sc-1i43xsx-0.ddpibn.tw-select', str(random.randint(1, 12)))
        sb.type('input[placeholder="Day"]', str(random.randint(1, 28)))
        sb.type('input[placeholder="Year"]', str(random.randint(1999, 2004)))
        sb.select_option_by_value('select[aria-label="Country Code"]', country)
        sb.type('input#phone-input', data)
        sb.sleep(25)
        sb.driver.uc_click('button[type="submit"]')
    except Exception:
        raise Exception()


def filldatatticketmaster(sb, data):
    try:
        sb.driver.uc_click('button.sc-6wpn76-1.eIpoux')
        sb.sleep(50)
        sb.driver.uc_click('button.sc-qXgsJ.sc-pIvzE.bVpxDS.noFocus')
        sb.sleep(50)
        sb.type("input[name='email']",
                # sb.type('input.#email\\[objectobject\\]__input',
                fake.pystr(15, 20).lower()+"@gmail.com")
        sb.type("input[name='password']", generatepsw())
        # sb.type('input#password\\[objectobject\\]__input', generatepsw())
        sb.type("input[name='firstName']", fake.first_name())
        # sb.type('input#firstname\\[objectobject\\]__input', fake.first_name())
        sb.type("input[name='lastName']", fake.last_name())
        # sb.type('input#lastname\\[objectobject\\]__input', fake.last_name())
        sb.select_option_by_value('select#dropDownGroup', country)
        sb.type("input[name='postalCode']", 44588)
        # sb.type('input#postalcode\\[objectobject\\]__input', 44588)
        sb.driver.uc_click('label.sc-pjtZy.lxKAG.checkbox--small')
        sb.type("input[name='phoneNumber']", data)
        # sb.type('input#phonenumber\\[objectobject\\]__input', data)
        sb.driver.uc_click('label.sc-pjtZy.lxKAG.checkbox--small')
        sb.driver.uc_click('button.sc-pbvBv.gaffan.sc-psfJB.bXuXEr.noFocus')
    except Exception:
        raise Exception()


def fillOtp(sb, otp):
    f = open(otp, 'r')
    qr = f.read()
    sb.type('input#txtSMSCode', qr)  # DARI WEBHOOK)
    sb.click('input#SubmitInvest')


def checkTimestamp(otp, exetime):
    mtime = os.path.getmtime(otp)
    mtime = datetime.fromtimestamp(mtime)
    exetime = exetime
    check = True
    while check:
        if mtime > exetime:
            check = False


def rest(sb):
    sb.driver.disconnect()
    connect = input('continue? ')
    if connect == '':
        sb.driver.connect()


regis = "Network.requestWillBeSent"

req = {}


def olah(req):
    postData = req['request']['postData']
    reemail = '(?<=&email=).*?(?=&)'
    rephone = '(?<=&phone=).*?(?=&)'
    postData = re.sub(reemail, fake.pystr(
        15, 20).lower()+"@gmail.com", postData)
    postData = re.sub(
        rephone, '11'+str(random.randint(10000000, 99999999)), postData)
    # body = json.loads(postData)
    body = postData
    header = req['request']['headers']
    req['request']['postData'] = postData
    return header, body, req


with SB(
        uc=True,
        user_data_dir="chprofiles/",
        disable_features="UserAgentClientHint",
        # agent=agent,
        # uc_cdp_events=True,
) as sb:
    for data in source:
        # sb.driver.delete_all_cookies()
        # url = 'https://www.exclusivemarkets.com/register'
        url = 'https://www.ticketmaster.com'
        openPageUC(sb, url, 1)
        # sb.sleep(10000)
        # sb.disconnect()
        # sb.sleep(1000)
        # sb.connect()
        # sb.uc_gui_handle_cf()
        filldatatticketmaster(sb, data)
        # sb.disconnect()
        # sb.sleep(109898)
        # sb.connect()

f.close()
