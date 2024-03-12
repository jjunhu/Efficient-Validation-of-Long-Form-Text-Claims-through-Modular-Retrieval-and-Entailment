import pandas as pd
import numpy as np
from nltk import ngrams
from collections import Counter

QUERY = "depth_3_summary"
DOCUMENT = "book_text"
FILE_PATH = 'data/extracted_data.csv'


l2_QUERY = "depth_2_summary"
l2_DOCUMENT = "book_text"
l2_FILE_PATH = 'data/l2_extracted_data.csv'


l1_QUERY = "depth_1_summary"
l1_DOCUMENT = "book_text"
l1_FILE_PATH = 'data/l1_extracted_data.csv'

# get the first 25 books for the 175B
def get_evaluation_set_175():
    data = pd.read_csv(FILE_PATH)
    return data[(data["book_num"] < 25) & (data["model_size"] == "175b")]

def get_evaluation_set_6():
    data = pd.read_csv(FILE_PATH)
    return data[(data["book_num"] < 25) & (data["model_size"] == "6b")]

def get_evaluation_set():
    data = pd.read_csv(FILE_PATH)
    return data[:4000]

# TODO: change data size for evaluation

def l2_get_evaluation_set_175():
    data = pd.read_csv(l2_FILE_PATH)
    return data[(data["book_num"] < 25) & (data["model_size"] == "175b")]

def l2_get_evaluation_set_6():
    data = pd.read_csv(l2_FILE_PATH)
    return data[(data["book_num"] < 25) & (data["model_size"] == "6b")]

def l2_get_evaluation_set():
    data = pd.read_csv(l2_FILE_PATH)
    return data[:4000]

def l1_get_evaluation_set_175():
    data = pd.read_csv(l1_FILE_PATH)
    return data[(data["book_num"] < 25) & (data["model_size"] == "175b")]

def l1_get_evaluation_set_6():
    data = pd.read_csv(l1_FILE_PATH)
    return data[(data["book_num"] < 25) & (data["model_size"] == "6b")]

def l1_get_evaluation_set():
    data = pd.read_csv(l1_FILE_PATH)
    return data[:4000]

def two_gram_overlap(str1, str2):
    grams1 = Counter(ngrams(str1.split(), 2))
    grams2 = Counter(ngrams(str2.split(), 2))
    overlap = sum((grams1 & grams2).values())
    total = sum((grams1 | grams2).values())
    return overlap / total if total > 0 else 0