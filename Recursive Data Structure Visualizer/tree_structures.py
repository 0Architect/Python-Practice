class Node:
    def __init__(self, value: str | None = None) -> None:
        self.__value = value
    
    def __str__(self):
        return self.__value if self.__value is not None else ""

class BinaryTree:
    def __init__(self, node: Node):
        self.node = node
        self.children: dict[str, BinaryTree]
    
    def preorder(self):
        print(self.node)
        if self.children["left"]:
            self.children["left"].preorder()
        if self.children["right"]:
            self.children["right"].preorder()
        return

    def inorder(self):
        if self.children["left"]:
            self.children["left"].inorder()
        print(self.node)
        if self.children["right"]:
            self.children["right"].inorder()
        return
        
    def postorder(self):
        if self.children["left"]:
            self.children["left"].inorder()
        if self.children["right"]:
            self.children["right"].inorder()
        print(self.node)
        return

    def insertleftchild(self, value: Node):
        self.children["left"] = BinaryTree(value)

    def insertrightchild(self, value: Node):
        self.children["right"] = BinaryTree(value)
    
    def traverseLeft(self):
        if self.children["left"]:
            return self.children["left"]

    def traverseRight(self):
        if self.children["right"]:
            return self.children["right"]

class Trie:
    def __init__(self, vocabulary: list[str]):
        self.vocabulary = vocabulary
        self.organized_vocabulary: dict[str, list[str]] = {}
        self.children: dict[str, Trie] = {}

        for i in range(len(self.vocabulary)):
            word = self.vocabulary[i]
            if word:
                self.vocabulary[i] = word[1:]
                self.organized_vocabulary[word[0]].append(self.vocabulary[i])
        for letter in self.organized_vocabulary.keys():
            self.children[letter] = Trie(self.organized_vocabulary[letter])
    
    def __str__(self) -> str:
        output = ""
        for letter in self.organized_vocabulary.keys():
            output += letter
            output += str(self.children[letter])
            output += '\n'
        return output

test1 = Trie(["Apple, Attack, Appole, Bark, Bast, Batch, Cat, Cart, Cartoon"])
print(test1)
# TODO: Rewrite Trie using insertion instead of how I did it.