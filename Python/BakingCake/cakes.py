def cakes(recipe, available):
    # First check to make sure that we have a ingredients available to make the recipe
    if set(recipe.keys()) > set(available.keys()): return 0
    
    # Figure out the limiting ingredient
    results = {}
    for ka in available:
        for kr in recipe:
            if ka == kr: results[ka] = (available[ka] / recipe[kr])
    return min(results.itervalues())