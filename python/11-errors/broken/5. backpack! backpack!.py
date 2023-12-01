#Backpack
backpack = []
stop = False
while not stop:
  print ("What do you want to do? add <item> | remove <item> | stop")
  usertext = input ("add|remove|stop>> ")
  #parse the text to a list. item [0] is the command, [1] is the item.
  parsed_text = usertext.split(" ", 1)
  if (parsed_text[0].lower() == "add"):
    if not len(parsed_text) == 2:
      print ("Invalid usage! Use it like this: add <item>")
      continue
    backpack.append(parsed_text[1])
    print (f"You've added a {parsed_text[1]} to your backpack.")
  if (parsed_text[0].lower() == "remove"):
    if not len(parsed_text) == 2:
      print ("Invalid usage! Use it like this: remove <item>")
      continue
    if not parsed_text[1] in backpack:
      print (f"You don't have a {parsed_text[1]} in your backpack!")
      continue
    backpack.remove(parsed_text[1])
    print (f"You have removed the {parsed_text[1]} from your backpack.")
  if (parsed_text[0].lower() == "stop"):
    stop = True
    print("\n(╯°□°）╯︵ ┻━┻\n")
    continue
  print ("Your backpack contains:")
  print (backpack)
