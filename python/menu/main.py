############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Menu system library
# OK - 26 Sep 2023

MenuItem = tuple[str, callable]

def prompt_menu(menu_title: str, items_list: list[MenuItem]) -> tuple[str, any]:
    print(menu_title)
    print('-' * 25)
    for i in range(len(items_list)):
        item = items_list[i]
        print(f'{i+1}.  {item[0]}')
    print('-' * 25)
    
    result = input('Enter an option: ')
    try:
        result = int(result)
    except ValueError:
        print('That is not a number!')
        return prompt_menu(menu_title, items_list)
    
    if result < 1 or result > len(items_list):
        print('That is not a valid option!')
        return prompt_menu(menu_title, items_list)
    
    item = items_list[result - 1]
    return (result, item[1]())
