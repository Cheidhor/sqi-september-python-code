
import re

user_email = input('enter email:')

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

match = re.search(pattern, user_email)

if match:
    print('your email is ', match.group())
else:
    print('not valid')