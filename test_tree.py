import red_black_set_mod





if __name__ == '__main__':
    tree = red_black_set_mod.RedBlackTree()

    # for i in range(9):
    #     tree.add(i)
    # print(tree)
    # tree.to_dot()

    with open("nums10000.txt", 'r') as f:
        lines = [line.strip('\n') for line in f.readlines()]
    for line in lines:
        tree.add(line)
        tree.add(line)
    #
    # tree.check()
    #
    # # delete
    # for i, line in enumerate(lines):
    #     if i % 3 == 0:
    #         tree.delete(line)
    #
    # tree.check()