import array

wordfile = open("words.nsv", 'r')
words = [w.replace('\n', '') for w in wordfile.readlines()]

def encode(string):
    ret = ""
    for c in string:
        ret+=words[ord(c)] + " "
    return ret[:len(ret)-1]

def decode(string):
    ret = ""
    for w in string.split(' '):
        ret+=chr(words.index(w))
    return ret


if __name__ == "__main__":
    string = "Hello World"
    estring = encode(string)
    print "\"" + estring + "\""
    print "\"" + decode(estring) + "\""