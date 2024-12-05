import re


def main():
    with open("input.txt") as f:
        # lines = f.readlines()
        program = f.read()

    def day_three_part_one(lines: list[str]):
        pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")

        total = 0
        for line in lines:
            matches = re.findall(pattern, line)
            for match in matches:
                total += int(match[0]) * int(match[1])

        return total

    def day_three_part_two(program: str):
        pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
        do_pattern = re.compile(r"(do\(\)|don't\(\))")

        total = 0
        filtered_line = ""
        mini_lines = re.split(do_pattern, program)
        enabled = True
        for mini_line in mini_lines:
            if mini_line == "do()":
                enabled = True
            elif mini_line == "don't()":
                enabled = False
            else:
                filtered_line += mini_line if enabled else ""

        matches = re.findall(pattern, filtered_line)
        for match in matches:
            total += int(match[0]) * int(match[1])

        return total

    # print(timeit.timeit("day_three_part_two(lines)", globals=locals(), number=10000))
    print(day_three_part_two(program))


if __name__ == "__main__":
    main()
