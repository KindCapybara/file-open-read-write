from pprint import pprint
import os


def open_file():
    name_open_file = 'recipes.txt'
    file_directory = os.path.join(os.getcwd(), name_open_file)
    key_list = ['ingredient_name', 'quantity', 'measure']
    cook_book = {}

    with open(file_directory, encoding='utf-8') as file:
        for data in file:
            ingredient_list = []
            dish_name = data
            amount_ingredients = int(file.readline())
            for ingredients in range(amount_ingredients):
                parse_str = str(file.readline().strip()).split('|')
                ingrid_dict = {key_list[i]: parse_str[i] for i in range(len(key_list))}
                ingredient_list.append(ingrid_dict)
            file.readline()
            cook_book[dish_name.strip()] = ingredient_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_file()
    ingred_dict = {}
    for dish_name in dishes:
        if dish_name in cook_book.keys():
            for ingred in cook_book[dish_name]:
                ingredient = ingred['ingredient_name']
                quantity = int(ingred['quantity']) * person_count
                measure = ingred['measure']
                if ingredient not in ingred_dict.keys():
                    ingred_dict[ingredient] = {'quantity': quantity, 'measure': measure}
                else:
                    ingred_dict[ingredient]['quantity'] += quantity
        else:
            print(f'Блюдо {dish_name} не найдено')
    return ingred_dict


def get_result_file():
    path = os.getcwd()
    files_dir_name = 'tree_files'
    file_directory = os.path.join(path, files_dir_name)
    files_list = os.listdir(file_directory)
    file_len = {}

    for file in files_list:
        with open(os.path.join(file_directory, file), encoding='utf-8') as file_to_read:
            quantity = len(file_to_read.readlines())
            if quantity not in file_len.keys():
                file_len[quantity] = file
            else:
                file_len[quantity].append(file)
            sort_file_len = sorted(file_len.keys())
            sorted_file_dict = {i: file_len[i] for i in sort_file_len}

    with open(os.path.join(file_directory, 'result.txt'), 'w', encoding='utf-8') as result:
        for quantity_ln, file_nm in sorted_file_dict.items():
            result.write(str(file_nm) + '\n')
            result.write(str(quantity_ln) + '\n')
            with open(os.path.join(file_directory, file_nm), encoding='utf-8') as read_file:
                for i in range(quantity_ln):
                    result.write(read_file.readline())
            result.write('\n')


# Задание 1
pprint(open_file(), sort_dicts=False)

# Задание 2
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Фахитос'], 2))

# Задание 3
get_result_file()
