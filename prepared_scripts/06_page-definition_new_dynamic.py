# -*- coding:utf-8 -*-

from alfred import Experiment
from alfred.page import Page
import alfred.element as elm
import alfred.section as sec

# pages definition
class Welcome(Page):
    def on_showing(self):
        text = elm.TextEntryElement('Welcome text', name='welcome_text')
        self.append(text)

class DynamicPage(Page):
    def on_showing(self):
        text = self.get_page_data('welcome_page')['welcome_text']
        text_element = elm.TextElement(text)
        self.append(text_element)

# experiment generation
def generate_experiment(self, config=None):
    exp = Experiment(config=config)

    page_01 = Welcome(title='Welcome', uid='welcome_page')
    page_02 = DynamicPage(title='Dynamic Page', uid='dynamic_page')

    main = sec.Section()
    main.append(page_01, page_02)

    exp.append(main)

    return exp
