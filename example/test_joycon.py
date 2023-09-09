import tft_config
import tft_buttons
import s3lcd
import utime
from machine import Pin

tft = tft_config.config(tft_config.WIDE)
buttons = tft_buttons.Buttons()


def main():
    try:
        tft.init()
        tft.fill(s3lcd.WHITE)
        while True:
            # 渲染屏幕
            tft.rect(20, 70, 40, 30, s3lcd.RED)
            tft.rect(80, 20, 30, 40, s3lcd.RED)
            tft.rect(80, 110, 30, 40, s3lcd.RED)
            tft.rect(130, 70, 40, 30, s3lcd.RED)
            tft.rect(260, 45, 40, 30, s3lcd.RED)
            tft.rect(200, 95, 40, 30, s3lcd.RED)
            # 上
            if buttons.up.value() == 0:
                tft.fill_rect(80, 20, 30, 40, s3lcd.RED)
            else:
                tft.fill_rect(80, 20, 30, 40, s3lcd.WHITE)
                tft.rect(80, 20, 30, 40, s3lcd.RED)
            # 下
            if buttons.down.value() == 0:
                tft.fill_rect(80, 110, 30, 40, s3lcd.RED)
            else:
                tft.fill_rect(80, 110, 30, 40, s3lcd.WHITE)
                tft.rect(80, 110, 30, 40, s3lcd.RED)
            # 左
            if buttons.left.value() == 0:
                tft.fill_rect(20, 70, 40, 30, s3lcd.RED)
            else:
                tft.fill_rect(20, 70, 40, 30, s3lcd.WHITE)
                tft.rect(20, 70, 40, 30, s3lcd.RED)
            # 右
            if buttons.right.value() == 0:
                tft.fill_rect(130, 70, 40, 30, s3lcd.RED)
            else:
                tft.fill_rect(130, 70, 40, 30, s3lcd.WHITE)
                tft.rect(130, 70, 40, 30, s3lcd.RED)
            # A
            if buttons.a.value() == 0:
                tft.fill_rect(200, 95, 40, 30, s3lcd.RED)
            else:
                tft.fill_rect(200, 95, 40, 30, s3lcd.WHITE)
                tft.rect(200, 95, 40, 30, s3lcd.RED)
            # B
            if buttons.b.value() == 0:
                tft.fill_rect(260, 45, 40, 30, s3lcd.RED)
            else:
                tft.fill_rect(260, 45, 40, 30, s3lcd.WHITE)
                tft.rect(260, 45, 40, 30, s3lcd.RED)
            tft.show()
        utime.sleep(1)
        tft.fill(s3lcd.WHITE)
    finally:
        tft.deinit()

main()