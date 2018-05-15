import os
from time import sleep

class Encaz:
    
###############################################################
####################### INITIALIZE PROGRAM. ###################
###############################################################
    def __init__(self):
        # INITIALIZE ENCRYPTION, DECRYPTION LETTERS.
        self._ENCRYPTED_LETTERS = { 
        "0": 'N', "1": 'G', "2": 'E', "3": '+', 
        '4': '=', '5': 'U', '6': 'Q', '7': '|', 
        '8': 'C', '9': 'D', "A": '4', "B": '7',
        "C": '`', "D": '9', "E": '8', "F": '2',
        "G": 'B', "T": 'X', "K": '?', "M": '}',
        "N": '<', "L": "&", "Q": '$', "W": '*', "R": '#',
        "Y": '[', "U": '!', "O": "^", "P": '/', "S": '(',
        "H": '-', "J": '~', "Z": ';', "X": ".", "V": ',',
        "I": ')', " ": "%"
        }

        self._DECRYPTED_LETTERS = {
            "N": '0', "G": '1', "E": '2', "+": '3', '=': '4',
            'U': '5', 'Q': '6', 'C': '8', 'D': '9', "4": 'A',
            "|": '7', "`": 'C', "9": 'D', "8": 'E', "2": 'F',
            "B": 'G', "X": 'T', "?": 'K', "}": 'M', "<": 'N',
            "&": "L", "$": 'Q', "*": 'W', "#": 'R', "[": 'Y',
            "!": 'U', "^": "O", "/": 'P', "(": 'S', "-": 'H',
            "~": 'J', ";": 'Z', ".": "X",  ",": 'V', ")": 'I',
            "%": " ", "7":'B'
        }

        # MENU.
        print("What do you want to do:")
        print("1-Encryption.")
        print("2-Decryption.")

        # DECLARE VARIABLES FOR HOLDING INPUTS.
        self.menuInput = input("===> ")
        self.encryptedString = ""
        self.decryptedString = ""

        if(self.menuInput == "1"):
            # ENCRYPTION METHOD.
            self.encrypt()
            

        elif(self.menuInput == "2"):
            # DECRYPTION METHOD.
            self.decrypt()
        else:
            # WHAT HAPPENS WHEN YOU INPUT WRONG INPUT.
            os.system("cls")
            print("Wrong input !!")
            sleep(1)
            os.system("cls")
            self.__init__()

###############################################################
####################### ENCRYPTION. ###########################
###############################################################
    def encrypt(self):
        # GET THE STRING YOU WANT TO ENCRYPT FROM THE USER.
        os.system("cls")
        stringInput = input("Enter your string: ").upper()
        stringInput = list(stringInput)

        for letter in stringInput:
            if(letter in self._ENCRYPTED_LETTERS):
                self.encryptedString += self._ENCRYPTED_LETTERS[letter]
            else:
                print("letter => ", letter, " is not found !")
                break

        # WRITE TO FILE
        self.writeString()

        self.askContinue()

###############################################################
####################### DECRYPTION. ###########################
###############################################################
    def decrypt(self):
         # GET THE STRING YOU WANT TO DECRYPT FROM THE USER.
        os.system("cls")
        stringInput = input("Enter your string: ").strip()
        stringInput = list(stringInput)

        for letter in stringInput:
            if(letter in self._DECRYPTED_LETTERS):
                self.decryptedString += self._DECRYPTED_LETTERS[letter]
            else:
                print("letter => ", letter, " is not found !")
                break

        # WRITE TO FILE
        self.writeString()

        self.askContinue()

    
    # WRITE STRING TO A FILE.
    def writeString(self):
        if(len(self.encryptedString) > 0):
            try:
                i = 0
                file = open('encaz.txt', 'w')
                done = file.write("Your encrypted string => " + self.encryptedString)
                if(done):
                    print("\n####### Encryption is done! please check the file created ########")
            except IOError as err:
                print("Opps! this error occured: ", err)
            

        elif(len(self.decryptedString) > 0):
            try:
                i = 0
                file = open('encaz.txt', 'w')
                done = file.write("Your encrypted string => " + self.decryptedString)
                if(done):
                    print("\n####### Decryption is done! please check the file created ########")
            except IOError as err:
                print("Opps! this error occured: ", err)
        else:
            pass

    # GET ENCRYPTED STRING.
    def getEncryptedString(self):
            if(len(self.encryptedString) > 0):
                return self.encryptedString
            else:
                print("There is no string")

    # GET DECRYPTED STRING.
    def getDecryptedString(self):
            if(len(self.decryptedString) > 0):
                return self.decryptedString
            else:
                print("There is no string")



###############################################################
####################### ASK CONTINUE. #########################
###############################################################
    # ASK CONTINUE METHOD.
    def askContinue(self):
        ans = input("\n\nclose program ? (y/n) ").lower()

        if(ans == "n"):
            os.system("cls")
            sleep(1)
            self.__init__()
        else:
            os.system("cls")
            print("Bye! :)")
            exit()
           

            

enc = Encaz()

