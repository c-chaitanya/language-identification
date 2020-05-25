#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program to identify language of a given string
"""

import fasttext

class LanguageIdentification:
    """
    Class object for Language Identification
    """

    def __init__(self):
        """
        Initializing class objects
        """
        pretrained_lang_model = "lid.176.bin"
        self.model = fasttext.load_model(pretrained_lang_model)

    def predict_lang(self, text):
        """
        Attributes
        text: type str, the sentence for which language is to be identified
        """
        predictions = self.model.predict(text, k=1) # top 1 matching languages
        return predictions

if __name__ == '__main__':
    LANGUAGE = LanguageIdentification()
    LANG = LANGUAGE.predict_lang("hej")
    print(LANG)
