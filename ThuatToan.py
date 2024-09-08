import string

def TaoMaTran(key):
    matrix = [[None]*5 for _ in range(5)]
    alphabet = list(string.ascii_uppercase)
    alphabet.remove('J')
    key = key.upper().replace('J', 'I')
    alphabet = ['I' if ch=='J' else ch for ch in alphabet]
    new_key = ''
    for ch in key:
        if ch not in new_key:
            new_key += ch
    key = new_key

    idx = 0
    for ch in key:
        row, col = divmod(idx, 5)
        matrix[row][col] = ch
        alphabet.remove(ch)
        idx += 1

    for ch in alphabet:
        row, col = divmod(idx, 5)
        matrix[row][col] = ch
        idx += 1

    return matrix

def LapMa(matrix, plain_text):
    plain_text = plain_text.upper().replace(' ', '').replace('J', 'I')
    if len(plain_text) % 2 != 0:
        plain_text += 'X'
    pairs = [plain_text[i:i+2] for i in range(0, len(plain_text), 2)]
    cipher_text = ''
    for pair in pairs:
        pos1 = [(row, col) for row in range(5) for col in range(5) if matrix[row][col] == pair[0]][0]
        pos2 = [(row, col) for row in range(5) for col in range(5) if matrix[row][col] == pair[1]][0]
        if pos1[0] == pos2[0]:  
            cipher_text += matrix[pos1[0]][(pos1[1]+1)%5] + matrix[pos2[0]][(pos2[1]+1)%5]
        elif pos1[1] == pos2[1]:  
            cipher_text += matrix[(pos1[0]+1)%5][pos1[1]] + matrix[(pos2[0]+1)%5][pos2[1]]
        else: 
            cipher_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
    return cipher_text

def GiaiMa(matrix, cipher_text):
    pairs = [cipher_text[i:i+2] for i in range(0, len(cipher_text), 2)]
    plain_text = ''
    for pair in pairs:
        pos1 = [(row, col) for row in range(5) for col in range(5) if matrix[row][col] == pair[0]][0]
        pos2 = [(row, col) for row in range(5) for col in range(5) if matrix[row][col] == pair[1]][0]
        if pos1[0] == pos2[0]:  
            plain_text += matrix[pos1[0]][(pos1[1]-1)%5] + matrix[pos2[0]][(pos2[1]-1)%5]
        elif pos1[1] == pos2[1]: 
            plain_text += matrix[(pos1[0]-1)%5][pos1[1]] + matrix[(pos2[0]-1)%5][pos2[1]]
        else:  
            plain_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
    return plain_text

