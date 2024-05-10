# password
The simplest utility for creating random passwords.

Install:
1. Compile the code using pyinstaller:
   pip install pyinstaller
   pyinstaller --onefile password.py
2. Place the executable file in /usr/local/bin/ to access it from the command shell:
   sudo mv password /usr/local/bin/

Using:
Just type "password" passing the desired length as an argument or without it.

Example:
In: password
Out: oEhW03ESwLgtUHu

In: password 20
Out: fGRGgNq92UaiMjyGr8gg
