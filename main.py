import string
from string import ascii_lowercase

def countLetter():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read();

    frankDict = {};
    for l in file_contents:
        l2 = l.lower()
        if l2.isalpha():
            if l2 in frankDict:
                frankDict[l2] = frankDict[l2]+1
            else:
                frankDict[l2] = 1
            
    return frankDict

def printReport(letterDict):
    for x in string.ascii_lowercase:
        print(f"The '{x}' character was found {letterDict[x]} times")

def main():
   printReport( countLetter());       

if __name__ == "__main__":
    main()