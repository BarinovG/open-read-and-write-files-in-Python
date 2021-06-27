from pprint import pprint

def cook_book_dict(file_name):
    cook_book = {}
    with open(f'{file_name}', encoding='utf-8') as f:
        cook_list = [line.strip() for line in f]
        for i, c in enumerate(cook_list):
            if c.isdigit():
                cook_book[cook_list[i - 1]] = []
                for receipt in cook_list[i + 1:i + int(c) + 1]:
                    ingredient_name = receipt.split('|')[0]
                    quantity = int(receipt.split('|')[1])
                    measure = receipt.split('|')[2]
                    cook_book[cook_list[i - 1]].append(
                        {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
    return cook_book

def print_cook_book(cook_book):
    for key in cook_book:
        print(key)
        for ingredient in cook_book[key]:
            print(f'\t{ingredient}')

# print_cook_book('cook_book.txt')

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_dict = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingridients in cook_book[dish]:
                ingridients['quantity'] *= person_count
                if ingridients['ingredient_name'] not in shop_dict:
                    shop_dict[ingridients['ingredient_name']] = {'quantity' : int(ingridients['quantity']), 'measure' : ingridients['measure']}
                elif ingridients['ingredient_name'] in shop_dict:
                    ingridients['quantity'] += int(ingridients['quantity'])
                    shop_dict[ingridients['ingredient_name']] = {'quantity' : int(ingridients['quantity']), 'measure' : ingridients['measure']}
    return shop_dict

pprint(get_shop_list_by_dishes(cook_book_dict('cook_book.txt'), ['Омлет', 'Фахитос', 'asd'], 3))



