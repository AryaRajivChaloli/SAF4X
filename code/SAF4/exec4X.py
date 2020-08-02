import os
import sys
from exec20 import find_sentiment20

def find_sentiment(strinput):
    output = find_sentiment20(strinput)
    return(output)

if __name__=='__main__':
    print(find_sentiment(sys.argv[1]))