import timeit
from collections import Counter


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    def day_one_part_two_counter(list_1: list[int], list_2: list[int]) -> int:
        # 0.00016914271 using counter
        total = 0
        num_sim_score_map = {}
        counts = Counter(list_2)

        for num in list_1:
            if num in num_sim_score_map:
                total += num_sim_score_map[num]
            elif count := counts.get(num, 0):
                sim_score = count * num
                num_sim_score_map[num] = sim_score
                total += sim_score

        return total

    def day_one_part_two(list_1: list[int], list_2: list[int]) -> int:
        # 0.01104793735598s
        total = 0

        for num in list_1:
            if count := list_2.count(num):
                total += num * count
        return total

    def day_one_part_one(list_1: list[int], list_2: list[int]) -> int:
        # 0.000122149797971s
        list_1.sort()
        list_2.sort()
        return sum([abs(item[0] - item[1]) for item in zip(list_1, list_2)])

    list_pairs = [[int(num) for num in line.strip("\n").split("   ")] for line in lines]
    list_1, list_2 = (list(i) for i in zip(*list_pairs))
    result = day_one_part_two(list_1, list_2)
    print(timeit.timeit("day_one_part_one(list_1, list_2)", globals=locals(), number=10000))


if __name__ == "__main__":
    main()
