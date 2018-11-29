import Mapper

wordfile = open("words.nsv", 'r') # Open Word List (newline separated value)
words = [w.replace('\n', '') for w in wordfile.readlines()] # Load the words into an array while stripping the \n from each word

Mapper.init(words)

## Encodes a string in our random english word format
# @param string The string to be encoded
# @returns The encoded string
def encode(string):
    latestTime, latestList = Mapper.updateList(Mapper.startTime, Mapper.startList)
    ret = ""
    for c in string:
        ret+=latestList[ord(c)] + " "
    return ret[:len(ret)-1]

## Decodes a string from our random english word format
# @param string The string to be decoded
# @returns The decoded string
def decode(string, time):
    latestTime, latestList = Mapper.updateListToTime(Mapper.startTime, Mapper.startList, time)
    ret = ""
    for w in string.split(' '):
        ret+=chr(latestList.index(w))
    return ret


## 'Test'
if __name__ == "__main__":
    string = "Hello World"
    estring = encode(string) # Encode the string
    print ("\"" + estring + "\"") # Print the encoded string
    print (Mapper.currentMinute())
    destring = decode(estring,Mapper.currentMinute()) # Decode the encoded string
    print ("\"" + destring + "\"") # Print the decode of the encoded string
    assert string == destring # Make sure the decoded string and the original match