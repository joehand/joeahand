# -*- coding: utf-8 -*-
# Copyright (c) 2015 joehand
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import csv
import logging
from operator import itemgetter

import requests

from pelican import signals


logger = logging.getLogger(__name__)

class Gdocs_Sheet(object):

    def __init__(self, gen, url, name='default'):
        self.content = None
        self.gen = gen
        self.name = name
        #github_url = GITHUB_API.format(self.gen.settings['GITHUB_USER'])
        try:
            c = requests.get(url).content
        except:
            logger.warning("unable to open {0}".format(url))
            return
        self.content = c

    def process(self):
        if self.content is None:
            return []
        lines = self.content.splitlines()
        header = [h.strip() for h in lines[0].split(',')] #trim header
        data = list(csv.DictReader(lines[1:], fieldnames=header))
        return data


def initialize(gen):
    if not 'GDOCS' in gen.settings.keys():
        logger.warning('GDOCS not set')
    else:
        gen.plugin_sheets = []
        for sheet in gen.settings['GDOCS']:
            gen.plugin_sheets.append(
                    (sheet['name'],Gdocs_Sheet(gen, sheet['url'],name=sheet['name']))
                )

def fetch(gen, metadata):
    gen.context['gdocs_data'] = {}
    for name, obj in gen.plugin_sheets:
        data = obj.process()
        gen.context['gdocs_data'][name] = data


def register():
    signals.article_generator_init.connect(initialize)
    signals.article_generator_context.connect(fetch)
