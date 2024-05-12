def different(sequence):
    new_seq = set(sequence)
    new_seq = list(new_seq)
    return len(sequence) == len(new_seq)   
    
sequence = [1, 2, 3, 4, 5]
print(different(sequence))
