"""
Zadanie 14. Problem wież w Hanoi (treść oczywista)
"""
# przekladamy z slupka a na slupek b


# def Hanoi(n, from_, to_, reserv_):
#     if n == 0:
#         return
#     Hanoi(n-1, a, c, b)
#     Hanoi(n-1, c, b, a)



# def Hanoi()

A = [3, 2, 1]
B = []
C = []


def hanoi(n, source, target, auxiliary):
    if n == 0:
        return
    # Move n - 1 disks from source to auxiliary, so they are out of the way
    hanoi(n - 1, source, auxiliary, target)

    # Move the nth disk from source to target
    target.append(source.pop())

    # Display our progress
    print(A, B, C, '##############', sep='\n')

    # Move the n - 1 disks that we left on auxiliary onto target
    hanoi(n - 1, auxiliary, target, source)


# Initiate call from source A to target C with auxiliary B
hanoi(3, A, B, C)
