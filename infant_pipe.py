#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:26:28 2019

@author: askaydevs (sk_singh18@outlook.com)
"""
import PyPDF2
import os
from os import listdir
from os.path import isfile, join
import re
import spacy
from tika import parser

path = 'Solverminds_Data/Sample' #Files residence

#A function for extracting the text from the files and returns as a string object
def pdf_extract(file, dir_path = 'Solverminds_Data/Sample'):
    extract = join(dir_path, file)
    file_data = parser.from_file(extract)
    text = file_data['content'].strip()
    #text = text[73:]
    text = str(text.strip())
    return text
#print(processed)
def process(text):
    processed = re.sub(r'[^\w\s]', ' ', text)
    #processed = text.replace('\n', ' ')
    processed = re.sub(' +', '', processed)
    processed = processed.strip()
    return processed

def input_writer():
    if not os.path.exists('test_input.txt'):
        with open('test_input.txt', 'wb') as f:
            f.write(b + processed)
            print("Transformation done successfully!!\n")
        f.close()

def rem_hf_panama(fr_text): # TODO: def rem_hf_hongkong
    fr_text = fr_text.strip()
    return fr_text[fr_text.find('Consular and Maritime Affairs')+len('Consular and Maritime Affairs'):fr_text.find('Inquiries concerning the subject of this Circular should be directed to:'):1] # This setting is specific to panama documents

def get_body(text): # this body still need some refresher
    n_text = rem_hf_panama(text)
    index = []
    for _ in re.findall(' +', n_text):
        index.append(n_text.find(_))
    for i in range(0, len(index)):
        if (index[i+1] > index[i]):
            indice = index[i + 1]
            break
        else:
            i += 1
    return n_text[indice:len(n_text):1].strip()
