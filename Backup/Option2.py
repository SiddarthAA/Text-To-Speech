def Op2():
    from gtts import gTTS
    import os

    FileName = input("Enter The File Name : ")

    fh = open(FileName, "r")
    myText = fh.read().replace("\n"," ")
    
    language = "en"

    output = gTTS(text=myText, lang=language, slow=False)

    output.save("Output.mp3")
    fh.close
    os.system("start Output.mp3")

if __name__ == "__main__":
    Op2()

