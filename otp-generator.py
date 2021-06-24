import secrets as sec
import string

def list_to_str(lst):
	lst_string_list = [f'{i} ' for i in lst]
	lst_string = ''
	lst_string = lst_string.join(lst_string_list)
	return lst_string

def encrypt_text(text_to_encrpyt, stringkey = None):
	plain_text = (str(text_to_encrpyt)).lower().strip()
	plain_text = plain_text.replace(' ', '')

	plain_text_int = ([ord(char) - 97 for char in plain_text])
	plain_int_string = list_to_str(plain_text_int)

	key = []

	if bool(stringkey) == False:
		for i in range(len(plain_text_int)):
			key.append((sec.randbelow(26)))

	else: 
		key_list = stringkey.split (' ')
		key = [int(i) for i in key_list]
		key = key[:(len(plain_text_int))]

	key_string = list_to_str(key)

	encryted_int = [i+j for i,j in zip(plain_text_int, key)]
	encryted_int = [i if i <= 25 else (i-26) for i in encryted_int]
	encrpyted_int_string = list_to_str(encryted_int)
	encrypted_text = [chr(i + 97) for i in encryted_int]

	encrypted_string = ''
	encrypted_string = encrypted_string.join(encrypted_text)

	while True:
		choice = str(input("Would you like to see a full overview of the encryption (y/n): "))
		if choice == "y":
			print()
			print(f'Plain Text:\n{plain_text}')
			print()
			print(f'Plain Text Integers:\n{plain_int_string}')
			print()
			print(f'Key:\n{key_string}')
			print()
			print(f'Encrypted Integers:\n{encrpyted_int_string}')
			print()
			print(f'Encrypted String:\n{encrypted_string}')
			break

		elif choice == "n":
			print()
			print(f'Plain Text:\n{plain_text}')
			print()
			print(f'Key:\n{key_string}')
			print()
			print(f'Encrypted String:\n{encrypted_string}')
			break

		else:
			print("Invalid Selection.")

	return encrypted_string, key

def decrypt_text(cipher_text, key):
	key_list = key.split (' ')
	key_list = [int(i) for i in key_list]

	cipher_list = []
	for i in range(len(cipher_text)):
		cipher_list.append(cipher_text[i])

	encrypted_int = ([ord(char) - 97 for char in cipher_list])

	key_list = key_list[:(len(encrypted_int))]
	key = list_to_str(key_list)

	encrypted_int_string = list_to_str(encrypted_int)
	plain_text_int = [i-j if (i-j) >= 0 else ((i-j) + 26) for i,j in zip(encrypted_int, key_list)]
	plain_int_string = list_to_str(plain_text_int)
	plain_text_list = [chr(i + 97) for i in plain_text_int]


	plain_text = ''
	plain_text = plain_text.join(plain_text_list)

	while True:
		choice = str(input("Would you like to see a full overview of the decryption (y/n): "))
		if choice == "y":
			print()
			print(f'Encrypted Text:\n{cipher_text}')
			print()
			print(f'Encrypted Integers:\n{encrypted_int_string}')
			print()
			print(f'Key:\n{key}')
			print()
			print(f'Decrypted Integers:\n{plain_int_string}')
			print()
			print(f'Decrypted Text:\n{plain_text}')
			break

		elif choice == "n":
			print()
			print(f'Encrypted Text:\n{cipher_text}')
			print()
			print(f'Decrypted Text:\n{plain_text}')
			break

		else:
			print("Invalid Selection.")

def generate_keys(number_of_keys, length_of_keys):
	key_list = []

	for i in range(number_of_keys):
		key = []
		for i in range(length_of_keys):
			key.append((sec.randbelow(26)))
		key_list.append(key)

	f = open("keys.txt", "w")
	i = 0

	for i in range(len(key_list)):
		for j in range(len(key_list[i])):
			f.write(str(f'{key_list[i][j]} '))
		f.write("\n \n")

def key_to_letters(key):
	key_list = key.split (' ')
	key_list = [int(i) for i in key_list]

	text_list = [chr(i + 97) for i in key_list]

	letter_string = ''
	letter_string = letter_string.join(text_list)
	print()
	print(f'Inputted Key: \n{key}')
	print()
	print(f'Outputted Letters:\n{letter_string}')

def letters_to_key(key_letters):
	letter_list = [str(char) for char in key_letters]

	number_list = ([str(ord(char) - 97) for char in letter_list])

	number_string = ' '
	number_string = number_string.join(number_list)
	print()
	print(f'Inputted Letters:\n{key_letters}')
	print()
	print(f'Key:\n{number_string}')

def main():
	while True:
		print()
		choice = str(input("Would you like to encrypt (e) text, decrypt (d) text, generate keys (g),\nconvert keys (c) or exit (exit) the program: "))
		if choice == 'e':
			print()
			text_to_encrypt = str(input("Input text to encrypt: "))
			text_to_encrypt = text_to_encrypt.translate(str.maketrans('', '', string.punctuation))
			key = str(input('Enter a key (not required): '))
			print()
			encrypt_text(text_to_encrypt, key)

		elif choice == 'd':
			print()
			cipher = input(str("Input the encrypted text: "))
			key = input(str("Input the key: "))
			print()
			decrypt_text(cipher, key)

		elif choice == 'g':
			print()
			number_of_keys = int(input("How many keys to generate: "))
			length_of_keys = int(input("How long should each key be: "))
			key_list = []
			generate_keys(number_of_keys, length_of_keys)
			print()
			print('''Your keys have been exported as "keys.txt".''')

		elif choice == 'c':
			while True:
				print()
				choice2 = str(input("Would you like to convert a key to letters (1), letters to a key (2), or go back (back): "))
				if choice2 == "1":
					print()
					key = input(str("Input the key: "))
					key_to_letters(key)
					break

				elif choice2 == "2":
					print()
					key_letters = input(str("Input the letters: "))
					letters_to_key(key_letters)
					break

				elif choice2 == "back":
					print()
					break

				else:
					print()
					print("Invalid Selection.")


		elif choice == 'exit':
			print()
			print("Goodbye...")
			print()
			break

		else:
			print("Invalid Selection.")
		print()

main()
