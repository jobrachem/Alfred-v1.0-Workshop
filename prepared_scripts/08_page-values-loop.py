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

class LoopPage(Page):
    def on_showing(self):
        text = elm.TextElement(self.values.loop_text)
        self.append(text)

# experiment generation
def generate_experiment(self, config=None):
    exp = Experiment(config=config)

    # page01
    page_01 = Welcome(title='Welcome', uid='welcome')
    page_01.values.welcome_text = 'Welcome Text'

    # looped pages
    loop_section = sec.SegmentedSection()
    for i in range(5):
        page = LoopPage(title='Loop Page {n}'.format(n=i), uid='looped_{n}'.format(n=i))
        page.values.loop_text = 'Loop Text of Page {n}'.format(n=i)
        loop_section.append(page)


    # fill main section
    main = sec.Section()
    main.append(page_01, loop_section)

    exp.append(main)

    return exp