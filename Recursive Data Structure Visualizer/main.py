from tree_structures import *

tester = BinaryTree(str)
root_node = tester.root
layer1_left = tester.insert(root_node, Node("John"))
layer1_right = tester.insert(root_node, Node("David"))

layer2_left = tester.insert(layer1_left, Node("John"))
layer2_right = tester.insert(layer1_left, Node("David"))

layer22_left = tester.insert(layer1_right, Node("John"))
layer22_right = tester.insert(layer1_right, Node("David"))

layer212_left = tester.insert(layer22_left, Node("John"))
layer212_right = tester.insert(layer22_left, Node("David"))

layer222_left = tester.insert(layer22_right, Node("John"))
layer222_right = tester.insert(layer22_right, Node("David"))

layer223_right = tester.insert(layer222_right, Node("John"))

tester.view_tree(root_node)
print("="*10 + "preorder" + "="*10)
tester.preorder(root_node)
print("="*10 + "inorder" + "="*10)
tester.inorder(root_node)
print("="*10 + "postorder" + "="*10)
tester.postorder(root_node)

test_trie = Trie()
test_root = test_trie.root

test_trie.insert_word(test_root, "car")
test_trie.insert_word(test_root, "cart")
test_trie.insert_word(test_root, "carton")
test_trie.insert_word(test_root, "cartoon")
test_trie.insert_word(test_root, "samantha")

test_trie.view_tree(test_root)
print(test_trie.get_children(test_root))
print(test_trie.print_prefix(test_root, "cart"))