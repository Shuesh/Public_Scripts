def main():
    word = input("Enter your word: ")
    output_str = translate(word)
    print(output_str)


def translate(word):
    braille = dict(capital='000001',space='000000',a='100000',b='110000',c='100100',d='100110',e='100010',f='110100',g='110110',h='110010',i='010100',j='010110',k='101000',l='111000',m='101100',n='101110',o='101010',p='111100',q='111110',r='111010',s='011100',t='011110',u='101001',v='111001',w='010111',x='101101',y='101111',z='101011')
    
    output_str = ''
    for letter in word:
        if (letter.isupper()):
            output_str += braille['capital']
            letter = letter.lower()
        if (letter != ' '):
            output_str += braille[letter]
        else:
            output_str += braille['space']

    return output_str

main()

