def Op1():
    from gtts import gTTS
    from googletrans import Translator
    import os 

    opts = {
    "English":"en",
    "Hindi":"hi",
    "Kannada":"kn",
    "Malayalam":"ml",
    "Tamil":"ta",
    "Telugu":"te",
    }

    print("""\n
    ~~~~~~~~~~~~~~~~~~~~~~~
    You Have Opted Option 1 
    ~~~~~~~~~~~~~~~~~~~~~~~
    """)

    print("""
    The Languages Available - 
    1| English  4| Tamil
    2| Hindi    5| Telugu
    3| Kannada  6| Malayalam
    """)

    print("""
    Note : 
    1| Enter Text In English 
    2| The Language Is Case Sensitive 
    """)


    
    UserTxT = input("\n    Enter Text That Has To Be Converted Into Speech : ")
    UserLan = str(input("\n    Enter Language : "))
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Your Text Is Beging Played Now
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)


    a = list(opts.keys())
    b = list(opts.values())

    Lan = None
    LanIndex = None 

    for i in a: 
        if UserLan==i:
            Lan=i
            x = a.index(i)
            LanIndex=b[x]
        else:
            continue
    
    translator = Translator()
    FinalTxT = translator.translate(UserTxT, dest=LanIndex)
    Txt = FinalTxT.text

    output = gTTS(text=Txt, lang=LanIndex, slow=False)

    output.save("Speech.mp3")
    os.system("start Speech.mp3")

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
    Your Text Is Beging Played Now
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

    fh = open(FileName, "r")
    myText = fh.read().replace("\n"," ")
    
    language = "en"

    output = gTTS(text=myText, lang=language, slow=False)

    output.save("Output.mp3")
    fh.close
    os.system("start Output.mp3")




print("""
~~~~~~~~~~ Welcome To Text To Speech Converter ~~~~~~~~~~
""")
print("""
Menu :
1| Converts The Typed Text Into Speech [Your preferred Language]
2| Converts The .txt File Into Speech 
""")

opt = int(input("\nEnter Option Number : "))
if opt == 1:
  Op1()
elif opt == 2:
  Op2()
else:
  print("|Invalid Option|")