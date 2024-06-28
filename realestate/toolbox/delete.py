class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

# 定义AVL树类
class AVLTree:
    def __init__(self):
        self.root = None

    def delete(self, root, key):
        # 1. 删除的节点没有子节点
        if not root:
            return root
        
        # 2. 删除的节点有一个子节点
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        # 注意：如果节点被删除，可能需要平衡树
        else:
            # 2.1 删除的节点有一个左子节点
            if not root.right:
                return root.left
            # 2.2 删除的节点有一个右子节点
            elif not root.left:
                return root.right
            # 2.3 删除的节点有两个子节点
            else:
                # 找到右子树的最左节点，即前驱节点
                root.key = self.find_min(root.right).key
                # 删除右子树的最左节点
                root.right = self.delete(root.right, root.key)

        # 更新节点的高度
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        # 计算平衡因子
        balance = self.get_balance(root)

        # 如果平衡因子大于1或小于-1，则需要旋转
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current