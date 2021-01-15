"""
Practical Problems Using Trees
Created By: Zafir Lari
Application: WWW List Collector

Description: Runs ListCollector Application
to parse HTML files and return unordered and
ordered list items from the file as a list.
"""


from abc import ABC
from html.parser import HTMLParser


class ListCollector(HTMLParser, ABC):
    """ Parses HTML files and creates a Python
    list for every ordered and unordered list in
    the HTML document
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.unorderedlistdata = []
        self.orderedlistdata = []
        self.readytoaddunordered = False
        self.readytoaddordered = False

    def handle_starttag(self, tag, attrs):
        if tag.startswith("ul"):
            self.readytoaddunordered = True
        if tag.startswith("ol"):
            self.readytoaddordered = True

    def handle_endtag(self, tag):
        if tag.endswith("ul"):
            self.readytoaddunordered = False
        if tag.endswith("ol"):
            self.readytoaddordered = False

    def handle_data(self, data):
        if self.readytoaddunordered is True:
            self.unorderedlistdata.append(data)
        if self.readytoaddordered is True:
            self.orderedlistdata.append(data)

    def getLists(self):
        for i in self.unorderedlistdata:
            if "\n" in i:
                self.unorderedlistdata.remove(i)
        for j in self.orderedlistdata:
            if "\n" in j:
                self.orderedlistdata.remove(j)
        return [self.unorderedlistdata, self.orderedlistdata]



