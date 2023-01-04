import qrcode
import qrcode as qr
import time
import os

# Get the user's home directory
home_dir = os.path.expanduser('~')

# Join the home directory and the Downloads directory
downloads_dir = os.path.join(home_dir, 'Downloads')

sources = {}

#Process
def main():
    print("Hello user!")
    print("You can create multiple qr codes at a time. ")
    print("Follow these Scheme: [Content],[Filename]")
    print("")
    print("To continue please press [ENTER]")
    input()
    getSources()

def getSources():
    clearInterface()
    print("Please enter a source. When finished, leave line empty and press [ENTER].")
    print("Follow these Scheme: [Content],[Filename] + press [ENTER]")
    print(" ")
    print("Current queue: " + len(sources).__str__())
    source = input()
    source = source.split(",")
    if len(source) == 2:
        sources.update({source[0]:source[1]})
        clearInterface()
        getSources()
    else:
        menu()

def convertQueue():
    clearInterface()
    for url, filename in sources.items():
        img = qr.make(url)
        img.save(downloads_dir + "\\" + filename + ".png")
        print("QR Code created with filename: " + filename + " in " + downloads_dir + "\\" + filename)
    time.sleep(1)
    print("All QR Codes are succesfully created. Press any key to end this program.")
    input()


#process



#extra

def menu():
    clearInterface()
    print("Options:     ")
    print("             [1] Add another source")
    print("             [2] convert queue to qr code")
    a = input()

    if a == "1":
        getSources()
    elif a == "2":
        convertQueue()
    else:
        menu()


def clearInterface():
    for i in range(50):
        print("")

#extra


main()