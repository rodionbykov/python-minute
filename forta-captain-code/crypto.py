alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt_caesar(num, text):
  result  = ''
  
  for k in text.lower(): 
    try:
      i = (alphabet.index(k) + num) % 26
      result += alphabet[i]
    except ValueError:
      result += k
  
  return result.lower()

def decrypt_caesar(num, text):
  result = ''
  
  for k in text.lower():
    try:
      i = (alphabet.index(k) - num) % 26
      result += alphabet[i]
    except ValueError:
      result += k
 
  return result.lower()

num = int(input("Please input shift number, e.g. 13: "))

text = input("Please input text: ")

ciphertext = encrypt_caesar(num, text)

print("Encoded text: ", ciphertext)

cleantext = decrypt_caesar(num, ciphertext)

print("Clean text: ", cleantext)
