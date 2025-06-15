from typing import Any, Optional
import sys

MIDDLE_BRANCH = '\u251c\u2500\u2500' 
LAST_BRANCH = '\u2514\u2500\u2500' 
VERTICAL_LINE = "│   "
INDENT_SPACE = "    "

class Node:
    def __init__(self, value: Optional[Any] = None):
        self.__value = value
    
    def __str__(self):
        return str(self.__value) if self.__value is not None else ""
    
    def __bool__(self):
        return bool(self.__value)
    
    @property
    def value(self):
        return self.__value

    # def set_value(self, value: Any):
    #     if type(value ==  None):
    #         raise ValueError("Can not set node to value type: None")
    #     self.__value = value

class Tree:
    def __init__(self, max_no_of_children: int = sys.maxsize, type: type = int, value: Optional[Any] = None) -> None:
        self._root = Node(value)
        self.type = type
        self.MAX_NO_OF_CHILDREN = max_no_of_children
        self.nodes: dict[Node, tuple[Node, list[Node], Node]] = dict({})
        self.nodes[self._root] = (self._root, [], Node(None))
    
    @property
    def root(self) -> Node:
        return self._root

    def parent(self, node: Node) -> Node:
        return self.nodes[node][2]
    
    def children(self, node: Node) -> list[Node]:
        return self.nodes[node][1]

    def insert(self, parent_node: Node, node: Node):
        if type(node.value) != self.type:
            raise TypeError(f"Type of node should be {self.type}")
        
        if parent_node not in self.nodes:
            raise KeyError(f"Key Error: {parent_node} not in {self.nodes}")
        
        if len(self.children(parent_node)) == self.MAX_NO_OF_CHILDREN:
            raise IndexError(f"This node has reached it's maximum number of children: f{self.MAX_NO_OF_CHILDREN}")
        
        self.nodes[node] = (node, [], parent_node)
        self.nodes[parent_node][1].append(node)

        return node
    
    def view_tree(self, node: Node, indent: str = ""):
        node_list = self.children(node)
        num_size = len(node_list)
        for i, child in enumerate(node_list):
            if i != num_size - 1:
                current_branch = MIDDLE_BRANCH
                next_indent = indent + VERTICAL_LINE
            else:
                current_branch = LAST_BRANCH
                next_indent = indent + INDENT_SPACE
            print(f"{indent}{current_branch} {child}")
            self.view_tree(child, next_indent)

class BinaryTree(Tree):
    def __init__(self, data_type: type = int):
        super().__init__(max_no_of_children=2, type=data_type)

    def left_child(self, node: Node) -> Node | None:
        if len(self.children(node)) >= 1:
            return self.children(node)[0]
        else:
            return None
    
    def right_child(self, node: Node) -> Node | None:
        if len(self.children(node)) > 1:
            return self.children(node)[1]
        else:
            return None
    
    def preorder(self, node: Node):
        left_child = self.left_child(node)
        right_child = self.right_child(node)
        if node:
            print(node)
        if left_child:
            self.preorder(left_child)
        if right_child:
            self.preorder(right_child)

    def inorder(self, node: Node):
        left_child = self.left_child(node)
        right_child = self.right_child(node)
        if left_child:
            self.inorder(left_child)
        if node:
            print(node)
        if right_child:
            self.inorder(right_child)
    
    def postorder(self, node: Node):
        left_child = self.left_child(node)
        right_child = self.right_child(node)
        if left_child:
            self.postorder(left_child)
        if right_child:
            self.postorder(right_child)
        if node:
            print(node)


class Trie(Tree):
    def __init__(self):
        super().__init__(type=str, value="")
    
    def insert_word(self, node: Node, word: str):
        if word:
            for char in word:
                node_char  = Node(char)
                for child in self.children(node):
                    if child.value == char:
                        self.insert_word(child, word[1:])
                    else:
                        print("no match")
                        self.insert(node, node_char)
                        self.insert_word(node_char, word[1:])
        else:
            self.insert(node, Node('*'))

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
# TODO: Enforce types for the Node class
# TODO: Implement the view tree function
# TODO: Ensure the prefix finder in Trie works (may need to implement end-of-word token)
# TODO: Fix Trie entirely