#simulated RSA encryption
import time
import rsa

Message = input("before we begin.... what message would you like to encrypt ? : ").encode('utf8')


def Menu():
    a = input (" \n Choose a menu option : \n 1. Encrypt a message \n 2. Decrypt a message \n 3. Sign a message \n 4. Exit : ")
    match a:
        case "1":
            EncryptSequence()
        case "2":
            DecryptSequence()
        case "3":
            Sign()
        case "4":
            exit()
    while a != "1" or "2" or "3" or "4":
        Menu()
                



def EncryptSequence():
    print ("creating keys ....")
    PublicKey,PrivateKey = GetKeys()
    time.sleep(1)
    print ("keys made !")
    print ("the message : ", Message,"is being encoded ...")
    print("encoded!")
    time.sleep(1)
    EncryptedMessage = Encrypt(PublicKey,Message)
    print("This is the Encrypted Message : " , EncryptedMessage) #done by third party with the public key
    
    

    
    
def DecryptSequence():
    try:
        PublicKey,PrivateKey  = GetKeys()
        print("Decrypting ...")
        time.sleep(1)
        print ("the decrypted message is ... : ", Decrypt(PrivateKey,Encrypt(PublicKey,Message)))
        
    except:
        print ("nothing to decrypt")
        
        

def Sign():
    PublicKey,PrivateKey = GetKeys()
    Signature = rsa.sign(Message,PrivateKey,'SHA-1')
    print ("the signature for your message is : \n ",Signature)
    hash1 = rsa.compute_hash(Message,'SHA-1')
    time.sleep(1)
    print ("\n and the calculated hash is ... :" , hash1)
    time.sleep(1)      
    print ("\n putting it together... the signed hash is : " ,rsa.sign_hash(hash1,PrivateKey,'SHA-1'))
    time.sleep(1)
    print ("now we can verify the signature... this should return SHA-1 if the signature is correct! : ", rsa.verify(Message,Signature,PublicKey))
    
    
def GetKeys():
    FirstPublicKey,FirstPrivateKey = rsa.newkeys(512)#private and public keys created
    return(FirstPublicKey,FirstPrivateKey)


def Encrypt(PublicKey,Message):
    return (rsa.encrypt(Message,PublicKey))


def Decrypt(PrivateKey,Message):
    a = rsa.decrypt(Message,PrivateKey)
    return(a)



                
            
if __name__ == "__main__":
    Menu()
    
    
