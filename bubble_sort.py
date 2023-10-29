def sort(sequence):
    for _ in sequence:
        for index in range(len(sequence) - 1):
            next_index = index + 1
            if sequence[index] > sequence[next_index]:
                sequence[index], sequence[next_index] = sequence[next_index], sequence[index]

    return sequence


sequence_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f"Bubble sort - {sort(sequence_to_sort)}")