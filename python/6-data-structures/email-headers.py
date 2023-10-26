############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Parse email usernames from an email header
# OK - 18/10/23

# read the lines of a file
def read_file(name: str) -> list[str]:
    file = open(name, "r")
    lines = file.readlines()
    return lines


# get the username from an email address
def get_username_from_email(email: str) -> str:
    email = email.strip()
    index = email.find("@")
    return email[:index]


def main():
    lines = read_file("email-header.txt")
    kv = {}
    for line in lines:
        line = line.strip()
        if line.startswith("-"):
            continue
        [key, value] = line.split(": ")
        kv[key.strip()] = value.strip()
    
    for key in kv:
        value = kv[key]
        if "@" in value:
            username = get_username_from_email(value)
        else:
            continue;
        print(f"{key}: {username}")
    

if __name__ == "__main__":
    main()
