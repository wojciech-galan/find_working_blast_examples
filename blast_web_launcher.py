#! /usr/bin/python3
# -*- coding: utf-8 -*-

import mechanicalsoup


browser = mechanicalsoup.StatefulBrowser()
browser.open("https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome")
page = browser.get_current_page()
print (page)