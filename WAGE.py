import os

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("WAGE").keyx()
       __import__("WAGE").login()
   except Exception as a:
       exit(str(a))
