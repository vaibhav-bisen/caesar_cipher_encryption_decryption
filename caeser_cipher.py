alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  # Check it is decode
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    # Check it is only alphabet
    if char in alphabet:
      # Find the index of the letter
      position = alphabet.index(char)
      # Set new index if encode shift letter in forword else reversed
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    # When it contain special/space/number the append as itm is
    else:
      end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")

# Import the logo from art.py.
from art import logo
print(logo)

# Restart the cipher program again and again?
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  # When if the user enters a shift that is greater than the number of letters in the alphabet?
  # Find the moudulus of that number and shift letter according to remainder 
  shift = shift % 26 

  #Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  # If user type no program should be stop
  if result == "no":
    should_continue = False
    print("GoodBye...!")
 
