############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Queue of customers
# OK - 26 Oct 2023

queue: list[str] = []

def add_to_queue(name: str):
    queue.append(name)
    print(f'  {name} : added to queue')

def list_queue():
    for name in queue:
        print(f'  {name}')

def next_customer():
    print(f'  {queue.pop(0)} : next customer')

def prompt():
    action = input('Type customer name, "next" or "list": ')
    
    if action == 'next':
        next_customer()
    elif action == 'list':
        list_queue()
    else:
        add_to_queue(action)
    
    prompt()

def main():
    prompt()

if __name__ == '__main__':
    main()
