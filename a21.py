import fileinput


def main(inp):
    print("task1", task1(parse_input(inp)))
    print("task2", task2(parse_input(inp)))


def parse_input(inp):
    res = []
    for row in inp:
        ingredients, allergens = row.strip(")").split(" (contains ")
        res.append((ingredients.split(" "), allergens.split(", ")))
    return res


def task1(notes):
    allergen_posible = {}
    for ingredients, allergens in notes:
        for a in allergens:
            if a in allergen_posible:
                allergen_posible[a].intersection_update(ingredients)
            else:
                allergen_posible[a] = set(ingredients)
    allergen_posible_ingredients = set()
    for ingredients in allergen_posible.values():
        allergen_posible_ingredients.update(ingredients)

    c = 0
    for ingredients, _ in notes:
        for i in ingredients:
            if i not in allergen_posible_ingredients:
                c += 1
    return c


def task2(notes):
    allergen_posible = {}
    for ingredients, allergens in notes:
        for a in allergens:
            if a in allergen_posible:
                allergen_posible[a].intersection_update(ingredients)
            else:
                allergen_posible[a] = set(ingredients)
    allergen_posible_ingredients = set()
    for ingredients in allergen_posible.values():
        allergen_posible_ingredients.update(ingredients)

    res = {}
    while True:
        for allergen, ingredients in allergen_posible.items():
            if len(ingredients) == 1:
                break
        else:
            break
        ingredient = ingredients.pop()
        res[ingredient] = allergen
        for i in allergen_posible.values():
            i.discard(ingredient)
    res = list(res.items())
    res.sort(key=lambda x: x[1])
    return ",".join(i[0] for i in res)


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
