# -*- coding:utf-8 -*-

from alfred import Experiment
from alfred.page import Page
from alfred.helpmates import parse_xml_to_dict
import alfred.element as elm
import alfred.section as sec

# pages definition
class Welcome(Page):
    def on_showing(self):
        consent = elm.TextElement(self.values.consent)
        self.append(consent)

# experiment generation
def generate_experiment(self, config=None):
    exp = Experiment(config=config)

    # import file
    instr = parse_xml_to_dict('files/instructions.xml')

    # initialise page
    page_01 = Welcome(title='Welcome', uid='welcome')
    page_01.values.consent = instr['consent']

    # fill main section
    main = sec.Section()
    main.append(page_01)

    exp.append(main)

    return exp
