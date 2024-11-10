class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None
        self.huff = ''

    def printNodes(self, val=''):
        newVal = val + str(self.huff)
        if self.left:
            self.left.printNodes(newVal)
        if self.right:
            self.right.printNodes(newVal)
        if not self.left and not self.right:
            print(f"{self.char} -> {newVal}")

def main():
    chars = []
    freq = []
    num_chars = int(input("Enter the number of characters: "))

    for _ in range(num_chars):
        char = input("Enter character: ")
        frequency = int(input(f"Enter frequency for {char}: "))
        chars.append(char)
        freq.append(frequency)

    nodes = [Node(chars[i], freq[i]) for i in range(len(chars))]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        
        left = nodes[0]
        right = nodes[1]
        left.huff = '0'
        right.huff = '1'

        newNode = Node(left.char + right.char, left.freq + right.freq)
        newNode.left = left
        newNode.right = right

        nodes = nodes[2:]  # Remove the first two nodes
        nodes.append(newNode)

    if nodes:
        nodes[0].printNodes()

main()
