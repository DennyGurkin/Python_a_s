import heapq
from collections import Counter, namedtuple

class Node (namedtuple("Node", ["left", "right"])):
    def walk(self, codes, code):
        self.left.walk(codes, code + "0")
        self.right.walk(codes, code + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, codes, code):
        codes[self.char] = code or "0"

def compress(enigma):
    heap = []
    for char, frequensy in Counter(enigma).items():
        heap.append((frequensy, len(heap), Leaf(char)))
    heapq.heapify(heap)
    count = len(heap)
    while len(heap) > 1:
        frequensy1, count1, left = heapq.heappop(heap)
        frequensy2, count2, right = heapq.heappop(heap)
        heapq.heappush(heap, (frequensy1 + frequensy2, count,  Node(left, right)))
        count += 1
    code = {}
    if heap:
        [(frequensy, count, root)] = heap
        root.walk(code, "")
    return code

def decompress(encoded, code):
    spam = []
    encoded_char = ""
    for char in encoded:
        encoded_char += char
        for decoded_char in code:
            if code.get(decoded_char) == encoded_char:
                spam.append(decoded_char)
                encoded_char = ""
                break
    return "".join(spam)


enigma = input("Введите сжимаемую строку: ")
code = compress(enigma)

encoded = "".join(code[char] for char in enigma)
print('Словарь:')
for char in code:
    print(f'{char} : {code[char]}')

print(f'Сжимаем строку: {encoded}')
print(f'Разжимаем обратно:{decompress(encoded, code)}')