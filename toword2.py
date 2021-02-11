# -*- coding: utf-8 -*-
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Inches
import jinja2

doc = DocxTemplate("1_Смоленский б-р, дом 17, стр. 5 ТЗК _ФИНАЛ_ДЛЯ ТЗК.docx")
images = {'main1.jpg': InlineImage(doc,'images/main1.jpg', width=Inches(4.73))}

context = {
    'customer': 'Фонд капитального ремонта многоквартирных домов города Москвы',
    'adress': 'г. Москва, ЦАО, Смоленский б-р, дом 17, стр. 5',
    'main_image': images['main1.jpg'],

}

jinja_env = jinja2.Environment(autoescape=True)
doc.render(context, jinja_env)
doc.save("result-final.docx")