def verify_email(email):
  if not email[0].isalpha():
    return False
  at = email.find("@")
  print(at)
  dot = email.rfind(".")
  print(dot)
  if at == -1 or dot == -1 or dot < at:
    return False
  if dot == len(email) - 1:
    return False
  return True

email = input()
if verify_email(email):
  print("Valid")
else:
  print("Invalid")