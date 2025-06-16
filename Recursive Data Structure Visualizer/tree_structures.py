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
    
    @property
    def value(self):
        return self.__value

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
            node_char  = Node(word[0])
            child_node = next((node for node in self.children(node) if node.value == node_char.value), None)
            if child_node:
                self.insert_word(child_node, word[1:])
            else:
                self.insert(node, node_char)
                self.insert_word(node_char, word[1:])
        else:
            self.insert(node, Node('*'))
    
    def get_children(self, node: Node) -> list[str]:
        output: list[str] = []
        for child in self.children(node):
            if child.value:
                child_output:list[str] = []
                child_suffixes = self.get_children(child)
                for suffix in child_suffixes:
                    child_output.append(child.value + suffix)
                if child_output:
                    output += child_output
                else:
                    output.append("")
        return output

    def find_prefix(self, node: Node, prefix: str):
        if len(prefix) == 1:
            char = prefix
            child = next((child for child in self.children(node) if child.value == char), None)
            if child:
                return child
            else:
                raise StopIteration("Node not present")

        elif len(prefix) == 0:
            raise StopIteration("Node not present")

        else:
            char = prefix[0]
            child = next((child for child in self.children(node) if child.value == char), None)
            if child:
                output = self.find_prefix(child, prefix[1:])
                if type(output) == Node:
                    return output
            else:
                raise StopIteration("Node not present")

    def print_prefix(self, node: Node, prefix: str):
        target_node = self.find_prefix(node, prefix)
        if type(target_node) == Node:
            output:list[str] = []
            for value in self.get_children(target_node):
                output.append(prefix + value)
            return output