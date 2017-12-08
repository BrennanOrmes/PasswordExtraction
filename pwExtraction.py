import hashlib

def main():
    print("What file are you reading? (Please remember file extensions)")
    txt = input(">: ")
    print("What is the minumum plaintext length?")
    minInput = input(">: ")
    print("What is the maximum plaintext length?")
    maxInput = input(">: ")
    print("Where do you want the file to be written to? (Please remember file extensions)")
    output = input(">: ")
    print("Is there any characters you don't want included in the extraction?")
    print("(Numbers: '123...' Certain Symbols: '£$%...')")
    print("Please put spaced between each character - You can leave this blank")
    dontInclude = input(">: ")
    dontInclude = dontInclude.split(" ")
    print(dontInclude)


    extractPassword(txt, minInput, maxInput, output, dontInclude)

    # for x in passWords:
    #     print(x)  

def extractPassword(txt, minInput, maxInput, output, dontInclude):
    passWords = []
    with open(output, "w", encoding='ISO-8859-1') as OUT:
        with open(txt, encoding='ISO-8859-1') as IN:
            for line_no, line in enumerate(IN):
                # Remember not to count the newline character
                    if (len(line.strip()) >= int(minInput)) and (len(line.strip()) <= int(maxInput)):
                            if not any (x in line for x in dontInclude):
                                #print(line_no, line)
                                OUT.write(line)
    # return passWords


if __name__ == '__main__':
    main()