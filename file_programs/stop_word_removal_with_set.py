'''
To run : python stop_word_removal.py noise.txt data.txt
'''
import string,sys
def remove_punctuations(line):
    return line.translate(str.maketrans('','',string.punctuation))

def read_words(f):
    words=[]
    for line in  f.readlines():
        line = remove_punctuations(line).lower()
        words.extend([word for word in line.split()])
    return words

def find_clean_words(noise_words,full_words):
    return set(full_words)-set(noise_words)



def remove_words(filename,noisefilename):
    with open(filename,'r') as f1,open(noisefilename,'r') as f2:
        full_words = read_words(f1) 
        noise_words = read_words(f2)
        clean_words = find_clean_words(noise_words,full_words)
    return len(clean_words)



if __name__ =='__main__':
    try:
        clean_words = remove_words(sys.argv[1],sys.argv[2])
        print("Clean words are",clean_words)
    except: 
       print(sys.argv[1]+" not found")
