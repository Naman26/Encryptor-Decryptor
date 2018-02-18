

#Prompt key, input file and output file
val = input("Enter the key:\n")
inpt = input("Enter input file\n")
out = input("Enter output file\n")

#Tis function encodes message withe the provided key
def encode(message, key):
    char2 = ""
    for i, element in enumerate(message):
        char = ord(element)
        #if the text is lowercase
        if 97 <= char <= 122:
            char = ((char - 97) + key) % 26 + 97
            char2 += str(chr(char))
        #if the text is uppercase
        elif 65 <= char <= 90:
            char = ((char - 97) + key) % 26 + 65
            char2 += str(chr(char))
    #return the encoded string
    return char2


ch =""
#Open source file to extract text
with open('inpt', 'r') as inp:
    data = inp.readlines()

#Call encode function with the text and key
for i in data:
    ch+= str(encode(i, int(val)))
#write the encoded text to the destination file
out.write("ch")
out.close()

#Decrypter
def find_key(text):
    count= ['']*26
    for i in range(26):
        #Append the frequency of character in the list
        count[i]= int(text.count(chr(int(i)+97)))
    print(count)
    return(abs(count.index(max(count))+1+97-117))

#print the key
print(find_key(ch))



