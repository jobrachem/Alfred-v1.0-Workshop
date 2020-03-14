# -*- coding:utf-8 -*-

from alfred import Experiment
from alfred.page import Page
import alfred.element as elm
import alfred.section as sec

class DynamicPage(Page):

    def on_showing_widget(self):
        text = self._experiment.data_manager.find_experiment_data_by_uid('welcome_page')['welcome_text']
        text_element = elm.TextElement(text, name='dynamic_page_text')
        self.append(text_element)


def generate_experiment(self, config=None):
    exp = Experiment(config=config)

    page_01 = Page(title='Welcome', uid='welcome_page')
    text_01 = elm.TextEntryElement('Welcome text', name='welcome_text')
    page_01.append(text_01)

    page02 = DynamicPage(title='DynamicPage', uid='dynamic_page')

    main = sec.Section()
    main.append(page_01, page02)

    exp.append(main)

    return exp