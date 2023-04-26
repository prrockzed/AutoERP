import subprocess
import sys


package = "selenium"
subprocess.check_call([sys.executable, "-m", "pip", "install", package])


file = open("yourInfo.txt", "w")
file.write(input("Your roll number: ") + "\n")
file.write(input("Your password: ") + "\n")
file.write(input("Your security question 1: ") + "\n")
file.write(input("Your answer 1: ") + "\n")
file.write(input("Your security question 2: ") + "\n")
file.write(input("Your answer 2: ") + "\n")
file.write(input("Your security question 3: ") + "\n")
file.write(input("Your answer 3: ") + "\n")
file.close()
