
file = open('passwordFile.txt','r')
password = file.read()

def passwordCheck(input):
    if(password == input):
        return True
    
    return False
