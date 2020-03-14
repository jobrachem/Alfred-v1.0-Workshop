# -*- coding:utf-8 -*-

from alfred import Experiment
from alfred.page import Page
import alfred.element as elm
import alfred.section as sec

class Welcome(Page):
    def on_showing(self):
        text = elm.TextElement('text')
        self.append(text)

class Script(object):
    def generate_experiment(self, config=None):
        exp = Experiment(config=config)

        page = Welcome(title='page title')

        main = sec.Section()
        main.append(page)

        exp.append(main)
        return exp

generate_experiment = Script().generate_experiment
