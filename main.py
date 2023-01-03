from InquirerPy import inquirer
import pyperclip

import ciphers.base as base
import ciphers.v2 as v2
import ciphers.v3 as v3

def main():
	done = False 

	while not done:
		choice = inquirer.select(
			message="encode or decode?",
			choices=["encode", "decode", "exit"]
		).execute()

		if choice == "encode":
			text = inquirer.text(message="text to encode").execute()
			e = v3.encode(text)
			#print(base.encode(text))
			#print(v2.encode(text))
			print(e)
			pyperclip.copy(e)
			
		elif choice == "decode":
			text = inquirer.text(message="text to decode").execute()
			d = v3.decode(text)
			print(d)
			pyperclip.copy(d)

		else:
			done = True


if __name__ == "__main__":
	main()