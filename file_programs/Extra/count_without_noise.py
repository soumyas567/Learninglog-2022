'''
removes stopwords of noise.txt from a data.txt and save in cleanfile.txt
To run : python count_without_noise.py noise.txt data.txt
'''
import string,sys
import count_words as cs


def remove_punctuations(line):
    return line.translate(str.maketrans('','',string.punctuation))

def read_words(f):
    words=[]
    for line in  f.readlines():
        line = remove_punctuations(line).lower()
        words.extend([word for word in line.split()])
    return words

def replace_line(line,noise_words):
    wordlist = line.split()
    for word in noise_words:        
        if word in wordlist:
            wordlist.remove(word)
    return " ".join(wordlist)

def write_to_file(lines):
    with open("cleanfile.txt","w") as f:
        f.writelines(lines)



def remove_from_file(noise_words):
    try:
        with open(sys.argv[2],'r+') as f:
            lines=""
            for line in f.readlines():
                line = remove_punctuations(line).lower()
                if any(word in line.split() for word in noise_words):
                    line = replace_line(line,noise_words)
                lines = lines + line +"\n"
            write_to_file(lines)


    except:
        print(sys.argv[2]+" not found")



if __name__ =='__main__':
    try:
        with open(sys.argv[1],'r') as f1:
            noise_words = read_words(f1)  
            remove_from_file(noise_words)
    except:
        print(sys.argv[1]+" not found")
        
    