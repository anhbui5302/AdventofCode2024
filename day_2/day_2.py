import timeit
from itertools import combinations


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    def check_remaining_levels(levels: list[int]) -> bool:
        remove_level_combinations = list(combinations(levels, len(levels) - 1))
        for remaining_levels in remove_level_combinations:
            if not (
                all(i < j for i, j in zip(remaining_levels, remaining_levels[1:]))
                or all(i > j for i, j in zip(remaining_levels, remaining_levels[1:]))
            ):
                continue
            if not all(1 <= abs(i - j) <= 3 for i, j in zip(remaining_levels, remaining_levels[1:])):
                continue
            return True

    def day_two_part_one(lines: list[str]) -> int:
        # 0.002728797296004s
        levels_list = [[int(num) for num in line.strip("\n").split(" ")] for line in lines]
        count = 0
        for levels in levels_list:
            if not (all(i < j for i, j in zip(levels, levels[1:])) or all(i > j for i, j in zip(levels, levels[1:]))):
                continue
            if not all(1 <= abs(i - j) <= 3 for i, j in zip(levels, levels[1:])):
                continue
            count += 1
        return count

    def day_two_part_two(lines: list[str]) -> int:
        # 0.008884299097000621s
        levels_list = [[int(num) for num in line.strip("\n").split(" ")] for line in lines]
        count = 0
        for levels in levels_list:
            if not (all(i < j for i, j in zip(levels, levels[1:])) or all(i > j for i, j in zip(levels, levels[1:]))):
                if not check_remaining_levels(levels):
                    continue
            if not all(1 <= abs(i - j) <= 3 for i, j in zip(levels, levels[1:])):
                if not check_remaining_levels(levels):
                    continue
            count += 1
        return count

    print(timeit.timeit("day_two_part_two(lines)", globals=locals(), number=1000))
    # print(day_two_part_two(lines))


if __name__ == "__main__":
    main()
