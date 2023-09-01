def read_matrix(fileName):
    with open(fileName, 'r') as f:
        l = [[int(num) for num in line.split(' ')] for line in f]
    return l
 