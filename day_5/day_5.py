from collections import defaultdict


def main():
    with open("input.txt") as f:
        program = f.read()

    def day_five_part_one(rules: dict[int, list[int]], updates: list[list[int]]) -> int:
        total = 0
        for update in updates:
            valid = True
            for idx, num in enumerate(update):
                rule_intersection = set(update[idx + 1 :]) & set(rules[num])
                if num != update[-1] and rule_intersection != set(update[idx + 1 :]):
                    valid = False

            total += update[len(update) // 2] if valid else 0
        return total

    def day_five_part_two(rules: dict[int, list[int]], updates: list[list[int]]) -> int:
        # TODO: Optimize the bubble sort?
        total = 0
        for update in updates:
            is_invalid = False
            for _, _ in enumerate(update):
                swapped = False
                for idx_2 in range(len(update) - 1):
                    if update[idx_2] in rules[update[idx_2 + 1]]:
                        update[idx_2], update[idx_2 + 1] = update[idx_2 + 1], update[idx_2]
                        is_invalid = True
                        swapped = True
                if not swapped:
                    break
            if is_invalid:
                total += update[len(update) // 2]
        return total

    def process_rules(rules: str) -> dict[int, list[int]]:
        rules_dict = defaultdict(list)
        rules_list = rules.split("\n")
        for rule in rules_list:
            key, value = rule.split("|")
            rules_dict[int(key)].append(int(value))
        return rules_dict

    rules, updates = program.split("\n\n")
    rules = process_rules(rules)
    updates = [[int(num) for num in update.split(",")] for update in updates.split("\n")]

    print(day_five_part_one(rules, updates))
    print(day_five_part_two(rules, updates))


if __name__ == "__main__":
    main()
