import glob
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

def main():
    text_files = glob.glob("*.txt")

    dict = {}
    mostcommondict = {}
    textcounter = ''

    for i in text_files:

        if i == 'readurls.txt' or i == 'urls.txt':
            continue
        else:
            with open(i, "r") as f:
                text = f.read()

            textcounter = textcounter + text

    print("Text Has been Updated")


    textcounter = textcounter.replace('\\n', '') # Remove new lines
    textcounter = textcounter.replace('\\t', '') # Remove tabs

    textcounter = re.sub(r'\b\d+(?:\.\d+)?\s+', '', textcounter) # Remove odd phrases
    textcounter = re.sub(r'[^\w\s]', ' ', textcounter)  # Remove other odd phrases
    textcounter = re.sub(r'\x80\xe2\x94\xd0\x93\xc3\xc2', ' ', textcounter)

    word_tokens = word_tokenize(textcounter) # Tokenize the cleaned text

    clean_tokens = [word for word in word_tokens if word not in stopwords.words('english') and  # Remove Punctuation and stopwords
                    word not in string.punctuation]


    # Create a dictionary
    for t in clean_tokens:
        if t in dict.keys():
            dict[t] += 1
        else:
            dict[t] = 1

    count = 0
    for k in sorted(dict, key=lambda k: dict[k], reverse=True):
        mostcommondict[k] = dict[k]
        count += 1
        if count == 40:
            break

    print("40 most common terms: ")
    for k, v in mostcommondict.items():
        print(k, " ", v, "\n")

if __name__ == '__main__':
    main()