#Option2

def Op2():
    from gtts import gTTS
    import os
    print("""\n
    ~~~~~~~~~~~~~~~~~~~~~~~
    You Have Opted Option 2 
    ~~~~~~~~~~~~~~~~~~~~~~~
    """)

    print("""
    Note : 
    1| The File Should Be A .txt File
    2| The OutPut Speech Will Be In English Language 
    """)

    FileName = input("\n    Enter The File Name : ")

    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Your Text Is Being Played Now
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

    fh = open(FileName, "r")
    myText = fh.read().replace("\n"," ")
    
    language = "en"

    output = gTTS(text=myText, lang=language, slow=False)

    output.save("Output.mp3")
    fh.close
    os.system("start Output.mp3")

if __name__ == '__main__':
    Op2()