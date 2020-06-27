def cakes(recipe, available):
    available_proportions = []
    for ingredient in recipe.keys():
        available_ingredient = available[ingredient] if ingredient in available else 0
        proportion = int(available_ingredient / recipe[ingredient])
        available_proportions.append(proportion)
    return min(available_proportions)

    
print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))