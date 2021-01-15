""" 
Test Driver File for HTML List Collector
Created By: Zafir Lari
Application: WWW List Collector

Description: Runs ListCollector Application
to parse HTML files and return unordered and
ordered list items from the file as a list.
"""

from HTML_List_Collector import ListCollector


HtmlFile = open("lists.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
parser = ListCollector()
parser.feed(source_code)
print("List Collector Returns a list of lists, first"
      " an unordered list of items and then an ordered list"
      " of items:\n")
print(parser.getLists())


""" 
SAMPLE RUN:

List Collector Returns a list of lists, first an unordered list of items and then an ordered list of items:

[['An item', 'Another', 'And another one'], ['Item one', 'Item two', 'Item three', 'Item four']]

Process finished with exit code 0
"""
