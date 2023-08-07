#!/usr/bin/env python
# coding: utf-8

import numpy as np




Rotor_1 = ["8","c","x",")","6","ç",".","-","z","f","g","_","9","?",",","h","ı","i","7","j","n","u","k","q","r","5","ş","t","4"," ","v",\
          "0","1","ü","2","a","-","b","s","l","y","m","(","o","e","ğ","ö","d","+","p","3"]

Rotor_2 = ["t","e",",","y","f","-","1","h","ı","d","7","+","ğ","ç","?","k","9","a",")","n","o","3","p","q",".","g","-","r","ş","l","i","_"," ","j","u","b","ü","v",\
          "0","m","x","2","c","4","5","s","ö","8","(","z","6"]

Rotor_3 = ["y","b",")","l","c","p","_","9","x","e","0","f","n","q","8"," ","g","5","ü","ğ","z","i","ç","j",".","a","h","o","r","s","d","(","k","ş","t","u","-",\
          "1","ı","-","ö","v","?","2","3",",","4","6","m","7","+"]

alphabet = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","q","r","s","ş","t","u","ü","v","x","y","z",\
          "0","1","2","3","4","5","6","7","8","9"," ",",",".","?","_","-",")","(","+","-"]




encryptedbool = True #True for encrypted, False for descrypted




def is_convertible_to_int(str):
    try:
        int(str)
        return False
    except ValueError:
        return True #first time we see it, we think it must be reversed but i want to break while loop.




Password = "0"
while(Password[-1] != "E" and Password[-1] != "C" or len(Password) != 7 or is_convertible_to_int(Password[0:6])):
    Password = input("Password(First 6 digit is number and last letter is E for Encrypt, C for Descrypt)\n (Example:010101E) :",)
    if(Password[-1] != "E" and Password[-1] != "C" or len(Password) != 7 or is_convertible_to_int(Password[0:6])):
        print("You entered invalid password.")




if(Password[-1] == "E"):
    encryptedbool = True
elif(Password[-1] == "C"):
    encryptedbool = False




boolwhile = True 
while(boolwhile):
    InputTextPath = input("File path of input text: ")
    try:
        with open(InputTextPath, "r", encoding="utf-8") as file:
            enctext = file.read()
        boolwhile = False
    except:
        print("File not find.")
        boolwhile = True



enctext = enctext.lower()




def newpassword(password):
    newpassword = [[],[],[]]
    for i in range(3):
        newpassword[i] = int(password[i*2]+ password[i*2+1])
        length = len(alphabet)-1
        while(newpassword[i] > length):
            newpassword[i] -= length
    return newpassword



def Set_RotateRotor(password,Rotors):
    new_password = newpassword(password)
    NewRotors = [[],[],[]]
    for i in range(len(Rotors)):
        for x in Rotors[i]:
            DelArray = Rotors[i][:int(new_password[i])]
            AppArray = Rotors[i][int(new_password[i]):]
            NewRotors[i] = AppArray + DelArray
    return NewRotors




def RotateRotor(Rotor):
    deletedletter = Rotor.pop(0)
    Rotor.append(deletedletter)
    return Rotor




Rotor_1,Rotor_2,Rotor_3 = Set_RotateRotor(Password,[Rotor_1,Rotor_2,Rotor_3])[0],Set_RotateRotor(Password,[Rotor_1,Rotor_2,Rotor_3])[1],Set_RotateRotor(Password,[Rotor_1,Rotor_2,Rotor_3])[2]



lengthofgiventext = len(enctext)




if(encryptedbool):
    EncryptedTextFinal = []
    for i in range(lengthofgiventext):#Encrypt the text file
        if(enctext[i] not in alphabet):
            EncryptedTextFinal.append(enctext[i])
        else:
            letterindex = alphabet.index(enctext[i])
            letterindex1 = alphabet.index(Rotor_1[letterindex])
            RotateRotor(Rotor_1)
            letterindex2 = alphabet.index(Rotor_2[letterindex1])
            RotateRotor(Rotor_2)
            letter = Rotor_3[letterindex2]
            RotateRotor(Rotor_3)
            EncryptedTextFinal.append(letter)
else:
    DescryptedText = []
    for i in range(lengthofgiventext):#Descrypt the text file
        if(enctext[i] not in alphabet):
            DescryptedText.append(enctext[i])
        else:
            letterindex2 = Rotor_3.index(enctext[i])
            RotateRotor(Rotor_3)
            latterindex1 = Rotor_2.index(alphabet[letterindex2])
            RotateRotor(Rotor_2)
            latterindex = Rotor_1.index(alphabet[latterindex1])
            RotateRotor(Rotor_1)
            letter = alphabet[latterindex]
            DescryptedText.append(letter)



if(encryptedbool):
    EncryptedFinal = ""
    for x in EncryptedTextFinal:
        EncryptedFinal += x
else:
    DescryptedFinal = ""
    for x in DescryptedText:
        DescryptedFinal += x



boolwhile1 = True
while(boolwhile1):
    Pathofoutput = input("File path for output(don't write '\\' for at the last latter)\n Example: C:\\Users\\A\\Desktop :")
    try:
        if(encryptedbool):
            with open(Pathofoutput+"\Encrypted.txt", "w",encoding="utf-8") as file:
                file.write(EncryptedFinal)
        else:
            with open(Pathofoutput+"\Descrypted.txt", "w",encoding="utf-8") as file:
                file.write(DescryptedFinal)
        boolwhile1 = False
    except:
        print("Invalid file path.")
        boolwhile1 = True





