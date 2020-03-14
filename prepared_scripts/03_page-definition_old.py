# -*- coding:utf-8 -*-

from alfred import Experiment
from alfred.page import Page
import alfred.element as elm
import alfred.section as sec

def generate_experiment(self, config=None)
    exp = Experiment(config=config)

    page_01 = Page(title='Welcome')
    text_01 = elm.TextElement('Welcome text', uid='welcome')
    page_01.append()

    main = sec.Section()
    main.append(page_01)

    exp.append(main)

    return exp