# -*- coding:utf-8 -*-

from alfred import Experiment
from alfred.page import Page
from alfred.helpmates import parse_xml_to_dict
import alfred.section as sec
import alfred.element as elm



class Welcome(Page):
    def on_showing(self):
        text = elm.TextElement('text2')
        self.append(text)


class Page02(Page):
    def on_showing(self):
        textentry = elm.TextEntryElement('Enter some text', name='text_page02')
        self.append(textentry)


class Page03(Page):
    def on_showing(self):
        numberentry = elm.NumberEntryElement('Enter a number')

        page02_dictionary = self.get_page_data('page02')
        text = elm.TextElement(page02_dictionary['text_page02'])

        self.append(numberentry, text)


class LoopPage(Page):
    def on_showing(self):
        text = elm.TextElement(self.values.loop_text, name='text_{i}'.format(i=self.values.i))
        self.append(text)


class Welcome(Page):
    def on_showing(self):
        text = elm.TextElement(self.values.consent)
        self.append(text)


class ImagePage(Page):
    def on_showing(self):
        image = elm.ImageElement('files/Bild{i}.jpg'.format(i=self.values.i))
        self.append(image)



def generate_experiment(self, config=None):
    exp = Experiment(config=config)

    # instr = parse_xml_to_dict(exp.subpath('files/instructions.xml'))

    # Welcome
    # welcome = Welcome(title='Welcome', values=instr)

    # Alternative definition of welcome
    welcome2 = Welcome(title='Welcome')
    # welcome2.values.consent = instr['consent']

    # page 01
    page01 = Page(title='page01')
    text = elm.TextElement('text')
    page01.append(text)

    # page02
    page02_instance = Page02(title='page02', uid='page02')

    # page03
    page03 = Page03(title='page03')

    # looped pages
    looped_pages = sec.Section()
    for i in [1, 2, 3]:
        page = LoopPage(title='Looped Page {number}'.format(number=i))
        page.values.loop_text = 'This is page number {number}'.format(number=i)
        page.values.i = i
        looped_pages.append(page)


    # image pages
    image_pages = sec.Section()
    for i in [1, 2, 3]:
        page = ImagePage(title='Image Page {i}'.format(i=i))
        page.values.i = i
        image_pages.append(page)


    main = sec.Section()
    main.append(image_pages)
    # main.append(page01, page02_instance, page03)

    exp.append(main)

    return exp

