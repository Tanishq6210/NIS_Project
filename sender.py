import sys
sys.path

from embed import embedFunc
from extract import extractFunc
from AES import encrypt,decrypt
import pyperclip as py


def hideFunc(SM,password,CM):
    encSM=encrypt(password,SM)
    print("Encrypted secret message going to send:",encSM)
    print("Cover message=",CM)
    CM_HM=embedFunc(encSM,CM)
    print("After embedding, Cover message=",CM_HM)
    py.copy(CM_HM)
    return CM_HM
    


