# Intro formatting for user
print('=====================')
print('   Ceaser Decoding   ')
print('=====================')

# Assigning required variables and asking user for required inputs to begin
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipherMessage = input('Please type the string to be decoded: ')
cipherMessage = cipherMessage.upper()
knowKey = input('Do you know the integer that was used to encode this? (yes or no) ')

# While loop ensuring that only yes or no is entered at this step
while knowKey != 'yes' and knowKey != 'no':
	print('Sorry, you can only answer with yes or no. Please try again. ')
	knowKey = input('Do you know the integer that was used to encode this? (yes or no) ')

# Once the yes/no check is passed, if yes is entered a key is requested from user	
if knowKey == 'yes':
	userKey = input('Please enter an integer between 1 and 25 as your key: ')

# Another while loop ensuring that the user enters an integer between 1 and 25
while knowKey == 'yes' and(not userKey.isdigit() or int(userKey)<= 0 or int(userKey)>25):
	print('Sorry, that is invalid. Must enter an integer between 1 and 25. ')
	userKey = input('Please enter an integer between 1 and 25 as your key: ')	

# Once the above condition is reached, this loop executes and deciphers the provided messaged based on the key provided	
if knowKey == 'yes':
	print('\nThe decrytped text must be: ', end ='')
	for x in cipherMessage:
		if x in alphabet:
			b = ord(x) - int(userKey)
			if b > 90:
				b = b - 26
				print(chr(b), end = '')
			elif b < 65:
				b = b + 26
				print(chr(b),end = '')
			else:
				print(chr(b), end = '')
		else:
			print(x, end = '')

# For easier reading in Console
print('')

# If the user enters that they do not know the key, the compiler skips to this step then prints out all 26 possible 
# combinations, with one of them being clear English while the rest are gibberish
	
if knowKey == 'no':
	print('\nThe decrypted text must be one of the following: ')
	for z in range (0,26):
		for y in cipherMessage:
			if y in alphabet:
				b = ord(y) - z
				if b > 90:
					b = b - 26
					print(chr(b), end = '')
				elif b < 65:
					b = b + 26
					print(chr(b), end = '')
				else:
					print(chr(b), end = '')
			else:
				print(y, end = '')
		print('\n')

print('')