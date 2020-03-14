# -*- coding:utf-8 -*-

from alfred import Experiment
from alfred.page import Page
import alfred.element as elm
import alfred.section as sec

# pages definition
class Welcome(Page):
    def on_showing(self):
        text = elm.TextElement(self.values.welcome_text)
        self.append(text)

# experiment generation
def generate_experiment(self, config=None):
    exp = Experiment(config=config)

    page_01 = Welcome(title='Welcome', uid='welcome')
    page_01.values.welcome_text = 'Welcome Text'

    # fill main section
    main = sec.Section()
    main.append(page_01)

    exp.append(main)

    return exp
