from func import trable_all
from func import ascii_art
import time

ascii_art()

try:
    trable = int(input('ใส่เลขแม่สูตรคูณตัวแรก: '))
    time.sleep(0.3)
    trable_last = int(input('ใส่เลขแม่สูตรคูณตัวสุดท้าย: '))
    time.sleep(0.3)
    trable_block = int(input('แม่สูตรคูณที่ไม่ต้องการให้แสดง: '))
    time.sleep(1)
except:
    time.sleep(0.3)
    print('กรุณาลองใหม่อีกครั้ง และกรอกเป็นตัวเลขเท่านั้น!!!')
    exit()

trable_all(trable, trable_last, trable_block)
