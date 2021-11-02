alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_text=""
try_again=True
while try_again:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  for letter in text:
    if letter in alphabet:
      position=alphabet.index(letter)
      if direction=="encode":
        if shift>26:
          shift=shift%26
        new_position=position+shift
      elif direction=="decode":
        if shift>26:
          shift=shift%26
        new_position=position-shift
      
      new_letter=alphabet[new_position]
      cipher_text+=new_letter
    else:
      cipher_text+=letter
  print(cipher_text)
  again=input("if you want to try again type 'y' else 'n'").lower()
  if again=="y":
    try_again=True
    cipher_text=""
  else:
    try_gain=False


  



