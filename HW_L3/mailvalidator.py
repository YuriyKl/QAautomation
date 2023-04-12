#!/usr/bin/python3

mail_for_valid = (input("Input email for validation:"))

res1 =mail_for_valid.count("@")
res2 =mail_for_valid.count(".")
print(res1)
print(res2)
if res1==1 and res2 == 1:
    if not mail_for_valid.startswith("@") and not mail_for_valid.endswith("."):
        for i in mail_for_valid:
                if mail_for_valid.index(i) == "@" and mail_for_valid.index(i) > mail_for_valid.index(i) == ".":
                    print(f"Entered mail address {mail_for_valid} is valid")
                else:
                    print(f"Entered mail address {mail_for_valid} is not correct")



# if res1==1 and res2 == 1:
#     if not mail_for_valid.startswith("@") and not mail_for_valid.endswith("."):
#         for i in mail_for_valid:
#                 if mail_for_valid.index(i) == "@" and mail_for_valid.index(i) > mail_for_valid.index(i) == ".":
#                     print(f"Entered mail address {mail_for_valid} is valid")
#                 else:
#                     print(f"Entered mail address {mail_for_valid} is not correct")
#
#
#
