BRANCH_MIDDLE = '\u251c\u2500\u2500' 
BRANCH_LAST = '\u2514\u2500\u2500' 
VERTICAL_LINE = "│   "
INDENT_SPACE = "    "
class Node:
    def __init__(self, value: str | None = None) -> None:
        self.__value = value
    
    def __str__(self):
        return self.__value if self.__value is not None else ""

class Tree:
    def __init__(self):
        self.children: dict[str, Tree] = {}

    def view_tree(self, parent_input: str = "", indent_level: int = 0):
        output = parent_input
        letters = list(self.children.keys())
        num_size = len(letters)
        for i, letter in enumerate(letters):
            if i != num_size - 1:
                current_branch = BRANCH_MIDDLE
            else:
                current_branch = BRANCH_LAST
            print(f"{output}{current_branch} {letter}")
            output += VERTICAL_LINE if i != num_size - 1 else INDENT_SPACE
            self.children[letter].view_tree(parent_input = output, indent_level= indent_level+1)

class BinaryTree(Tree):
    def __init__(self, node: Node):
        super().__init__()
        self.node = node
    
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

# class Trie:
#     def __init__(self, vocabulary: list[str]):
#         self.vocabulary = vocabulary
#         self.organized_vocabulary: dict[str, list[str]] = {}
#         self.children: dict[str, Trie] = {}

#         # for i in range(len(self.vocabulary)):
#         #     word = self.vocabulary[i]
#         #     if word:
#         #         self.vocabulary[i] = word[1:]
#         #         if word[0] not in self.organized_vocabulary.keys():
#         #             self.organized_vocabulary[word[0]] = []
#         #         self.organized_vocabulary[word[0]].append(self.vocabulary[i])
#         # for letter in self.organized_vocabulary.keys():
#         #     self.children[letter] = Trie(self.organized_vocabulary[letter])
    
#         for word in self.vocabulary:
#             self.insert(word)
    
#     # def __str__(self) -> str:
#     #     output = ""
#     #     for letter in self.children.keys():
#     #         output += letter
#     #         output += str(self.children[letter])
#     #         output += '\n'
#     #     return output

#     def insert(self, word: str):
#         if not word:
#             return
#         first_letter = word[0]
#         rest = word[1:]
#         if first_letter in self.children.keys():
#             self.children[first_letter].insert(rest)
#         else:
#             self.children[first_letter] = Trie([rest])
    

# test1 = Trie(["Apple", "Attack", "Appole", "Bark", "Bast", "Batch", "Car", "Cart", "Cartoon"])
# # test1 = Trie(["Car", "Cart", "Cartoon"])
# test1.view_tree()

# # class newTrie:
# #     def __init__(self, word: str) -> None:
# #         self.children: dict[str, newTrie] = {}

# #         self.insert(word)
    
# #     def find_prefix(self, prefix: str):
# #         #TODO: think about empty string
# #         if len(prefix) == 1:
# #             for letter in self.children.keys():
# #                 if letter == prefix:
# #                     return self.children[letter]
# #                 else:
# #                     return None
# #         first_letter = prefix[0]
# #         rest = prefix[1:]
# #         for letter in self.children.keys():
# #             if first_letter == letter:
# #                 return self.children[letter].find_prefix(rest)
# #         return None

# #     def insert(self, word: str):
# #         current_letter = word[0]
# #         while(currentTrie = self.find_prefix(current_letter)):

# TODO: Rewrite Trie using insertion instead of how I did it.
# TODOl Fully integrate the Base Class Tree with all the derivatives
# TODO: Implement the view tree function
# TODO: Ensure the prefix finder in Trie works (may need to implement end-of-word token)
# TODO: Fix Trie entirely