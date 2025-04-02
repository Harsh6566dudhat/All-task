sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_size = len(sample_list) // 3 


def manual_reverse(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):  
        reversed_lst.append(lst[i])
    return reversed_lst
for i in range(0, len(sample_list), chunk_size):
    chunk = sample_list[i:i + chunk_size]  
    print(f"Chunk {i // chunk_size + 1} {chunk}")
    reversed_chunk = manual_reverse(chunk)  
    print(f"After reversing it {reversed_chunk}")