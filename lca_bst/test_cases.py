from lca_bst import TreeNode, lowest_common_ancestor

def test_lca():
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    p = root.left
    q = root.right
    assert lowest_common_ancestor(root, p, q).val == 6
    print("All tests passed.")

if __name__ == "__main__":
    test_lca()