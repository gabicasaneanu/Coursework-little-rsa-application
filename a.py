#simulated RSA encryption
import time
import rsa
def FirstActorKeys():
    print ("creating keys ....")
    time.sleep(1)
    (FirstPublicKey,FirstPrivateKey) = rsa.newkeys(512)#private and public keys created
    print ("keys made !")
    Message = input("message to encode : ").encode('utf8')
    print("encoded!")
    time.sleep(1)
    a = Encrypt(FirstPublicKey,Message)
    print("This is the Encrypted Message : " , a) #done by third party with the public key
    time.sleep(2)
    print("Now by using the private key, the message can be decrypted...")
    time.sleep(2)
    print("the decrypted message is ..." ,Decrypt(FirstPrivateKey,a))
    
    



def Encrypt(PublicKey,Message):
        return (rsa.encrypt(Message,PublicKey))


def Decrypt(PrivateKey,Message):
        return (rsa.decrypt(Message,PrivateKey))
    
    
    

if __name__ == "__main__":
    FirstActorKeys()
    
    
