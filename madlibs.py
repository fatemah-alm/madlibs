def main():
	# write your code here
	time = input('Enter a number from 1 to 12: ')
	items = input('Enter a noun (plural): ')
	name = input('Enter a name: ').title()
	scream = input('Enter any sentence: ').upper()
	action = input('Enter a verb: ')

	result = 'It was ' + time +  ' o\'clock when I heard a knock at the door.\nI opened the door and there was a box full of ' + items + ' with a note saying "From Mr. ' + name + '."\nJust as I closed the door I heard a scream "' + scream + '."\nI froze in place and all I could do was ' + action + '.'
	print(result)

if __name__ == '__main__':
	main()

	#Enter a number from 1 to 12: 6
# Enter a noun (plural): dolls
# Enter a name: stephen sedoll
# Enter any sentence: the future is made of dolls
# Enter a verb: shake my head