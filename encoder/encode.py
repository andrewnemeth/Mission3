
wordfile = open("words.nsv", 'r') # Open Word List (newline separated value)
words = [w.replace('\n', '') for w in wordfile.readlines()] # Load the words into an array while stripping the \n from each word

## Encodes a string in our random english word format
# @param string The string to be encoded
# @returns The encoded string
def encode(string):
    ret = ""
    for c in string:
        ret+=words[ord(c)] + " "
    return ret[:len(ret)-1]

## Decodes a string from our random english word format
# @param string The string to be decoded
# @returns The decoded string
def decode(string):
    ret = ""
    for w in string.split(' '):
        ret+=chr(words.index(w))
    return ret


## 'Test'
if __name__ == "__main__":
    string = "Hello World"
    estring = encode(string) # Encode the string
    print "\"" + estring + "\"" # Print the encoded string
    destring = decode(estring) # Decode the encoded string
    print "\"" + destring + "\"" # Print the decode of the encoded string
    assert string is destring # Make sure the decoded string and the original match