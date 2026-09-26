WINDEX_ALPHABET = "!AaBbCcDdEeFf123456"
MAIN_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789., !?:;@/\\|_+-'\"#₽&()*~`•√π÷×§∆£€$¢^°={}©®™✓[]<>\nабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
DIVIDER = len(WINDEX_ALPHABET) - 1
SEPARATOR = ":"

def encode(text: str) -> str:
	indexes = []
	for s in text:
		num = MAIN_ALPHABET.index(s) + 1
		if num <= DIVIDER:
			indexes.append((0, num))
		elif num % DIVIDER == 0:
			indexes.append((num // DIVIDER, 0))
		else:
			indexes.append((num // DIVIDER, num % DIVIDER))
	output = []
	for i in indexes:
		ap = ""
		for n in i:
			ap += WINDEX_ALPHABET[n]
		output.append(ap)
	
	return SEPARATOR.join(output)


def decode(text: str) -> str:
	if text[-1] == SEPARATOR:
		text = text[:-1]
	input = text.split(SEPARATOR)
	output = ""
	for i in input:
		k = WINDEX_ALPHABET.index(i[0]) * DIVIDER
		n = WINDEX_ALPHABET.index(i[1])
		k += n
		m = MAIN_ALPHABET[k - 1]
		output += m
	
	return output
