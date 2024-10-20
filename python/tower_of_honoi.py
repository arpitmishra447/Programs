def tower_of_hanoi_1(n, source, target, aux):
    print(f"Move {n} from {source} to {target}")
def tower_of_hanoi(n, src, target, aux):
    if n == 1:
        tower_of_hanoi_1(n, src, target, aux)
    else:
        tower_of_hanoi(n-1, src, aux, target)
        tower_of_hanoi_1(n, src, target, aux)
        tower_of_hanoi(n-1, aux, target, src)