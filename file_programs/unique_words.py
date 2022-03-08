'''
To run : python unique_words.py filename.txt
'''

import string,sys

def remove_punctuations(line):
    return line.translate(str.maketrans('','',string.punctuation))

def create_histogram(line,word_dictionary):
    for word in line.split():
                if word not in word_dictionary:
                    word_dictionary[word] =1
                else:
                    word_dictionary[word] +=1
    return word_dictionary

def count_word_frequency(filename):
    word_dictionary = dict()
    with open(filename,'r') as f:
        for line in  f.readlines():
                line = remove_punctuations(line).lower()
                word_dictionary = create_histogram(line,word_dictionary)   
    return word_dictionary

def count_unique(filename):
    word_dictionary = count_word_frequency(filename)
    unique_words = [key for key,value in word_dictionary.items() if value ==1]
    return len(unique_words)
        


if __name__ =='__main__':
    try:
        print("Number of unique words are:",(count_unique(sys.argv[1])))     
    except: 
        print(sys.argv[1]+" not found")

    