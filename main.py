try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print('Do you want do (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()

    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break

    print('Please, enter letter e or d...')

while True:
    maxKey = len(SYMBOLS) - 1

    print('Please, enter the key (0 to {}) to use'.format(maxKey))
    response = input('> ').upper()

    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Enter the message to {}.'.format(mode))
message = input('> ')

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)

        translated += SYMBOLS[num]
    else:
        translated += symbol

print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard'.format(mode))
except:
    pass
