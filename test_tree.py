import time
import red_black_set_mod





if __name__ == '__main__':

    # for i in range(9):
    #     tree.add(i)
    # print(tree)
    # tree.to_dot()

    begin = time.time()

    tree = red_black_set_mod.RedBlackTree()
    for line in range(100000):
        tree.add(line)
    end = time.time()

    print ((end - begin) * 1000)
    #
    # tree.check()
    #
    # # delete
    # for i, line in enumerate(lines):
    #     if i % 3 == 0:
    #         tree.delete(line)
    #
    # tree.check()