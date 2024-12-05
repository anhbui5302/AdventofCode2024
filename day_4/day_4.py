def main():
    with open("input.txt") as f:
        lines = f.readlines()
        # program = f.read()

    def day_four_part_one(lines: list[str]):
        def can_proceed(
            coords: tuple[int, int], direction: tuple[int, int], mat: list[list[str]]
        ) -> tuple[int, int] | None:
            new_coords = tuple(coord + offset for coord, offset in zip(coords, direction))
            return new_coords if 0 <= new_coords[0] < len(mat) and 0 <= new_coords[1] < len(mat[0]) else None

        def search(
            coords: tuple[int, int], direction: tuple[int, int], mat: list[list[str]], to_find: list[str]
        ) -> bool:
            if (new_coords := can_proceed(coords, direction, mat)) is not None and mat[new_coords[0]][
                new_coords[1]
            ] == to_find[0]:
                if len(to_find) == 1:
                    return True
                else:
                    return search(new_coords, direction, mat, to_find[1:])
            else:
                return False

        mat = [[char for char in line.strip()] for line in lines]
        to_find = ["M", "A", "S"]
        clockwise_directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        total = 0
        for x in range(len(mat)):
            for y in range(len(mat[x])):
                if mat[x][y] == "X":
                    for direction in clockwise_directions:
                        if search((x, y), direction, mat, to_find):
                            total += 1
        return total

    def day_four_part_two(lines: list[str]):
        def search_diagonals(coords: tuple[int, int], mat: list[list[str]], to_find: list[str]) -> bool:
            diagonal_directions = [(-1, -1), (1, -1)]

            for direction in diagonal_directions:
                new_coords = tuple(coord + offset for coord, offset in zip(coords, direction))

                found_char = mat[new_coords[0]][new_coords[1]]
                if found_char not in to_find:
                    return False

                other_char = to_find[1 - to_find.index(found_char)]
                opposite_direction = tuple(-offset for offset in direction)
                opposite_coords = tuple(coord + offset for coord, offset in zip(coords, opposite_direction))

                if mat[opposite_coords[0]][opposite_coords[1]] != other_char:
                    return False

            return True

        mat = [[char for char in line.strip()] for line in lines]
        to_find = ["M", "S"]
        total = 0
        for x in range(1, len(mat) - 1):
            for y in range(1, len(mat[x]) - 1):
                if mat[x][y] == "A":
                    if search_diagonals((x, y), mat, to_find):
                        total += 1
        return total

    print(day_four_part_two(lines))


if __name__ == "__main__":
    main()
