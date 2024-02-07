############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# List contents of a directory using subprocesses
# OK - 7 Feb 2024

import os
import sys
import subprocess
from time import perf_counter, perf_counter_ns

# Will identify the OS and return it as a string
# If unknown, None is returned
def identify_os() -> str | None:
    known = ['win32', 'linux', 'darwin']
    if sys.platform in known:
        return sys.platform
    else:
        return None


# Will build a command to list the contents of a directory
# Returns a string that can be used with subprocess.run
# Raises ValueError if the OS is unknown
def build_command(system: str, dir: str) -> str:
    if '"' in dir:
        print('Stop trying to do naughty things!')
        quit(1)
    
    match system:
        case 'win32':
            return f'cmd /c dir "{dir.replace('/', '\\')}" /a /o-s :-d | find "/"'
        case 'linux':
            return f'ls -l "{dir}" -S'
        case 'darwin':
            return f'ls -l "{dir}" -S'
        case _:
            raise ValueError(f'Unknown OS: {system}')


# Will spawn a subprocess
# Returns the contents of stdout as a string
def spawn(cmd: str) -> str:
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
        print('Check the directory is valid and try again.')
        quit(1)
    return result.stdout


# Sort the contents of the output
# Returns a list of directories/files
def process_output(system: str, dir: str, output: str) -> 'list[str]':
    lines = output.split('\n')
    match system:
        case 'win32':
            lines.pop()
            dirs = []
            files = []
            for line in lines:
                values = line.split()
                if '<JUNCTION>' in line:
                    continue
                elif '<DIR>' in line:
                    name = f'DIR  {' '.join(line.split()[3:])}'
                    dirs.append(name)
                else:
                    name = ' '.join(line.split()[3:])
                    files.append(name)
            return dirs + files
        case 'linux' | 'darwin':
            items = []
            lines.pop(0)
            for line in lines:
                items.append(line.split()[8:])
            return items
        case _:
            raise ValueError(f'Unknown OS: {system}')


# (Fallback) List the contents of a directory using os.listdir
def list_files(dir) -> 'list[str]':
    try:
        result = os.listdir(dir)
    except FileNotFoundError as e:
        print(f'Error: {e}')
        quit(1)
    return result


# Print a list of directories/files
def print_list(dirs: 'list[str]') -> None:
    print('-'*45)
    for i in range(len(dirs)):
        print(f'{i}   {dirs[i]}')
    print('-'*45)


def main() -> None:
    system = identify_os()
    dir = input('Enter a directory: ')
    if system is None:
        print(f'OS "{sys.platform}" is unknown, using os.listdir() ...')
        files = list_files(dir)
    else:
        print(f'Running on {system} ...')
        cmd = build_command(system, dir)
        print(f'Running {cmd} ...')
        start = perf_counter()
        output = spawn(cmd)
        stop = perf_counter()
        print(f'Execution time: {stop - start} ms')
        files = process_output(system, dir, output)
    print_list(files)


if __name__ == '__main__':
    main()
