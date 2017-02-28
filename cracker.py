#!/usr/bin/env python
"""This script brute forces the password of a word document using a dictionary attack"""
import win32com.client as win32

#call the win32.Dispatch with looks like a static method returning an object
WORD = win32.Dispatch("Word.Application")
WORDLIST = "10K_most_common.txt"
DOC = r"C:\Users\niall\Downloads\MDF-SF1.docx"
'''
open wordlist and read the values into a object of type listOf<string>
and the strip out the \n
'''
PASSWORD_FILE = open(WORDLIST, 'r')
PASSWORDS = PASSWORD_FILE.readlines()
PASSWORD_FILE.close()
PASSWORDS = [item.rstrip('\n') for item in PASSWORDS]

'''
iterate through the list and pass the current value in the password list
to the open method of the word doc
if the document opens then return the password
'''

for password in PASSWORDS:
    try:
        doc = WORD.Documents.Open(DOC, False, True, None, password)
        doc.Close()
        print "The password for " + DOC + " is: " + password
        break
    except Exception as error:
        pass
