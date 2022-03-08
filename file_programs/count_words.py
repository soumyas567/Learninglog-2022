'''
Count the number of words in a file
To run : python count_words.py filename.txt
'''
import string,sys

def remove_punctuations(line):
    return line.translate(str.maketrans('','',string.punctuation))
   

def count_words(filename):
    '''count the number of words in a file'''
    with open(filename,'r') as f:
        count = 0
        for line in  f.readlines():
                line = remove_punctuations(line)
                count += len(line.split())
    return count

if __name__ =='__main__':
    try:
        print("Number of Words",count_words(sys.argv[1]))     
    except: 
        print(sys.argv[0]+" not found")    