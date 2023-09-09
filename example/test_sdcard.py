import tft_config
import utime
from machine import Pin, SPI
import s3lcd
import vga2_bold_16x32 as font
import gc

tft = tft_config.config(tft_config.WIDE)

spi = SPI(1, 60_000_000, sck=Pin(12), mosi=Pin(11), miso=Pin(13))
from sdcard import SDCard
import os
sd = SDCard(spi, Pin(10, Pin.OUT), 30_000_000)
os.mount(sd, '/sd')

def complementary_color(color565):
    inverted_color = ~color565
    return (
        ((inverted_color & 0x001F) << 11)
        | (inverted_color & 0x07E0)
        | ((inverted_color & 0xF800) >> 11)
    )

def center(using_font, text, fg=s3lcd.WHITE, bg=s3lcd.BLACK):
    length = 1 if isinstance(text, int) else len(text)
    tft.text(
        using_font,
        text,
        tft.width() // 2 - length // 2 * using_font.WIDTH,
        tft.height() // 2 - using_font.HEIGHT // 2,
        fg,
        bg,
    )


def main():
    try:
        tft.init()
        tft.fill(s3lcd.RED)
        tft.rect(0, 0, tft.width(), tft.height(), complementary_color(s3lcd.RED))
        center(font, 'SD Card Reading', s3lcd.WHITE, s3lcd.RED)
        tft.show()
        utime.sleep(1)

        for i in range(1, 4):
            image = str(i) + '.jpg'
            tft.jpg('/sd/picture/' + image, 0, 0)
            tft.show()
            utime.sleep(3)
            gc.collect()

    finally:
        tft.deinit()


main()