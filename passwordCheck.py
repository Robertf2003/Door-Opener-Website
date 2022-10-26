
file = open('passwordFile.txt','r')
password = file.read()
print(password)
def passwordCheck(input):
    if(password == input):
        return True
    
    return False
