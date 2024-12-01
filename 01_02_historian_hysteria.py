from collections import defaultdict
from typing import List, Tuple


def process_input(input: bytes) -> List[Tuple[int, int]]:
    list1 = []
    list2 = []
    for line in input.split("\n"):
        elems = line.split()
        list1.append(int(elems[0]))
        list2.append(int(elems[1]))
    return list1, list2


def measure_distance(list1, list2) -> int:
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    result = 0
    for a,b in zip(sorted_list1, sorted_list2):
        result += abs(a -b)
    return result

def measure_similarity(list1, list2) -> int:
    count_per_element = defaultdict(lambda: 0)
    result = 0
    for elem in list2:
        count_per_element[elem] += 1
    for elem in list1:
        result += elem * count_per_element[elem]
    return result

if __name__ == "__main__":
    in_file = "01_input.txt"
    with open(in_file) as f:
        list1, list2 = process_input(f.read())
    distance = measure_distance(list1, list2)
    similarity = measure_similarity(list1, list2)
    print("Distance is: %s" % distance)
    print("Similarity is: %s" % similarity)
