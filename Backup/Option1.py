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
    
    UserTxT = input("\n Enter Text That Has To Be Converted Into Speech : ")
    UserLan = str(input("\n Enter Language : "))

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

Op1()