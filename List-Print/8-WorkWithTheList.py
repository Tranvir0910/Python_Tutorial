n = int(input())\

list = []

for i in range(1,n+1):
  command = input()
  command_list = command.split()
  if command_list[0] == 'print':
    print(list)
  elif command_list[0] == 'append':
    list.append(int(command_list[1]))
  elif command_list[0] == 'insert':
    list.insert(int(command_list[1]), int(command_list[2]))
  elif command_list[0] == 'remove':
    list.remove(int(command_list[1]))
  elif command_list[0] == 'sort':
    list.sort()
  elif command_list[0] == 'pop':
    list.pop(len(list)-1)
  elif command_list[0] == 'reverse':
    list.sort(reverse=True)