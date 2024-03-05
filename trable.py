from func import trable_all     #การ import ฟังก์ชันจากอีกไฟล์เพื่อเอามาใช้ในไฟล์นี้
from func import ascii_art      #การ import ฟังก์ชันจากอีกไฟล์เพื่อเอามาใช้ในไฟล์นี้
import time                     #การ import Lib เวลา เพื่อเอามาใช้ดีเลย์การทำงาน

ascii_art()  #เอาชื่อฟังก์ชันมาใส่และวงเล็บเปิด-ปิด เพื่อให้ฟังก์ชันนี้ทำงาน

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

#ฟังก์ชัน try,except คือการดัก Error หากเกิดเหตุการณ์นอกกรอบต่างๆ

trable_all(trable, trable_last, trable_block)   #เอาชื่อฟังก์ชันมาใส่เพื่อให้ฟังก์ชันนี้ทำงาน
