class Tree:
    def __init__(self, layers_list: list):
        self.branches_list = [
            [1 if i == '+' else 0 for i in layer]
            for layer in layers_list
        ]

    def to_string(self):
        return [
            ''.join(['+' if i == 1 else '.' for i in layer])
            for layer in self.branches_list
        ]

    def even_year(self):
        self.branches_list = [
            [i + 1 for i in layer] for layer in self.branches_list
        ]

    def odd_year(self, rows: int, cols: int):
        coords_elems_to_destroy = []
        for i, layer in enumerate(self.branches_list):
            for j, branch in enumerate(layer):
                if branch >= 3:
                    coords_elems_to_destroy.append((i, j))

        temp_coords = []
        for coord in coords_elems_to_destroy:
            i, j = coord[0], coord[1]
            for shift in [1, -1]:
                if 0 <= i + shift <= rows - 1:
                    temp_coords.append(
                        (i + shift, j)
                    )
                if 0 <= j + shift <= cols - 1:
                    temp_coords.append(
                        (i, j + shift)
                    )
        coords_elems_to_destroy.extend(temp_coords)
        coords_elems_to_destroy = set(coords_elems_to_destroy)

        for coord in coords_elems_to_destroy:
            i, j = coord[0], coord[1]
            self.branches_list[i][j] = 0


def TreeOfLife(rows: int, cols: int, years: int, layers_list: list) -> list:
    tree = Tree(layers_list)
    for year in range(years):
        if year % 2 == 0:
            tree.even_year()
        if year % 2 != 0:
            tree.odd_year(rows, cols)
    return tree.to_string()
