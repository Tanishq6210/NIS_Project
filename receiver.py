from extract import extractFunc
from AES import decrypt

def revealFunc(CM_HM,password):
    SM_extract=extractFunc(CM_HM)
    print("Your secret message:",decrypt(password,SM_extract))
    return decrypt(password,SM_extract)
