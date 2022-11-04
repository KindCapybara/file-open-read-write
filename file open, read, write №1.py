with open('recipes.txt', 'rt', encoding='utf_8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        quantity_of_ingredients = int(file.readline())
        ingredient = []
        for i in range(quantity_of_ingredients):
            ingrid = file.readline().split(' | ')
            ingredient_name, quantity, measure = ingrid
            ingredient.append({'ingredient_name': ingredient_name,
                                'quantity': quantity, 
                                'measure': measure})
        file.readline()
        cook_book[dish_name] = ingredient
print(cook_book)