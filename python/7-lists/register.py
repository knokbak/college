############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Register of students
# OK - 26 Oct 2023

students = ['Person1', 'Person2', 'Person3']
present_students = []
absent_students = []

def prompt_student(name: str):
    action = input(f'{name} : [P]resent or [A]bsent: ')
    if action[0].upper() == 'P':
        present_students.append(name)
    elif action[0].upper() == 'A':
        absent_students.append(name)
    else:
        print('Invalid input!')
        prompt_student(name)

def main():
    for name in students:
        prompt_student(name)
    
    present_students.sort()
    absent_students.sort()

    for name in present_students:
        print(f'{name} : Present')
    
    for name in absent_students:
        print(f'{name} : Absent')

if __name__ == '__main__':
    main()
