# -*- coding: utf-8 -*-
# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


class TicketMaker:
    def __init__(self, template_path=None, font_path=None):
        if template_path is None:
            self.template_path = os.path.join("images", "ticket_template.png")
        else:
            self.template_path = template_path
        if font_path is None:
            self.font_path = os.path.join("python_snippets//fonts", "ofont_ru_Arial Narrow.ttf")
        else:
            self.font_path = font_path
        self.fio = None
        self.from_ = None
        self.to = None
        self.date = None

    def make_ticket(self, out_path=None):
        self.fio, self.from_, self.to, self.date = self.collect_information()
        im = Image.open(self.template_path)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=16)

        y = im.size[1] - 275
        message = f"{self.fio}"
        draw.text((45, y), message, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 190 - font.size
        message = f"{self.from_}"
        draw.text((45, y), message, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 125 - font.size
        message = f"{self.to}"
        draw.text((45, y), message, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 125 - font.size
        message = f"{self.date}"
        draw.text((285, y), message, font=font, fill=ImageColor.colormap['black'])

        out_path = self.out_path if out_path else 'ticket.png'
        im.save(out_path)
        print(f'Post card saved as {out_path}')

    def collect_information(self):
        fio = str(input("Введите фамилию, имя и отчество через пробел: "))
        from_ = str(input("Введите место отправления: "))
        to = str(input("Введите место назначения: "))
        date = str(input("Введите дату отправления: "))
        return fio, from_, to, date


if __name__ == '__main__':
    maker = TicketMaker()
    maker.make_ticket()

#
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.