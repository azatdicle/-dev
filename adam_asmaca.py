import sys
name = input("isminizi giriniz:")
print("Oyuna Hosgeldin "+name)

Kelime="Azat"
can=5
guess_string=""
while can>0:
    charter_left=0
    for caharter in Kelime:
        
        if caharter in guess_string :   
            print(caharter)
        else:
            print("-")
            charter_left+=1
    
    if charter_left==0:
        print("Kazandın")
        break
    
    guess=input("Tahmin:")
    guess_string+=guess
    
    if guess not in Kelime:
        can-=1
        print("Yanlis Tahmin :(")
        print("Kalan can "+ str(can))
        
        if can==0:
            print("Oyun Bitti......")
            break
