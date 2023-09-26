############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Menu system library
# OK - 26 Sep 2023

from typing import Any, Callable

MenuItem = tuple[str, Callable]

# Returns the selected option (0) and the function's response (1) as a tuple.
def prompt_menu(menu_title: str, items: list[MenuItem]) -> tuple[MenuItem, Any]:
    print(menu_title)
    print('-' * 25)
    for i in range(len(items)):
        item = items[i]
        print(f'{i+1}.  {item[0]}')
    print('-' * 25)
    
    result = input('Enter an option: ')
    try:
        result = int(result)
    except ValueError:
        print('That is not a number!')
        return prompt_menu(menu_title, items)
    
    if result < 1 or result > len(items):
        print('That is not a valid option!')
        return prompt_menu(menu_title, items)
    
    item = items[result - 1]
    return (item, item[1]())
