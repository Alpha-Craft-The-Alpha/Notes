# Important!!! This code is raw and unfinished!

import os
from time import sleep
from getch import getch
from replit import db

passwordLettersEncode = {"a" : "ad§s", "A" : "jd/", "b" : "3gf%", "B" : "4gf%", "c" : "d4f§", "C" : "#3*\\", "d" : "wx=8", "D" : "§h$7", "e" : "3f§", "E" : "?=@", "f" : "h;d", "F" : "Fd:;G&", "g" : "~hr", "G" : "pgr3", "h" : "l:!", "H" : "ht§F", "i" : "Rgh7", "I" : "#'rG", "j" : "-2_R", "J" : "fRk§", "k" : "?&g/", "K" : "G$ga4", "l" : "Ut/F", "L" : "!iN7", "m" : "+p8G*", "M" : "oR~p", "n" : "dj(e", "N" : "q~rr%", "o" : "]7%b", "O" : "s,E;1", "p" : "´dSr", "P" : "8)~[", "q" : "hrT4~f", "Q" : "?~r!1", "r" : "gS&'", "R" : "#-~#", "s" : "sM;gT", "S" : "cOl:5", "t" : "cOF7]", "T" : "t7rD", "u" : "r#uF", "U" : "Pu5R", "v" : "Wk§~", "V" : "dEx7", "w" : "syM##", "W" : "HR~t_", "x" : "63fT-h", "X" : "<kI~", "y" : "*nEx:-", "Y" : "ts/e%", "z" : "JSu%T$", "Z" : "gR5%n", " " : "drF@", "!" : "f/h", "\"" : "jDn3" }

# Function for flushing the console
def Flush(additional=""):
  os.system("clear")
  print("=============")
  print("----Notes----")
  print("=============")
  print(additional, end="") # Add \n for newline

# Function for printing out text smoothly
def Print(text = "Hello World!", delay=0.03, nL=True):
  for c in text:
    print(c, end="", flush=True); sleep(delay)
  if nL:
    print()

# Function for encoding passwords
def Encode(password):
  global passwordLettersEncode
  encoded = ""
  for c in password:
    encoded += passwordLettersEncode[c]
  return encoded

# Function for checking passwords
def CheckPassword(username, password):
  global db
  encoded = Encode(password)
  if encoded == db["accountInfo"][username]:
    return True
  else:
    return False

def WriteUser(username, password):
  global db
  data = db["accountInfo"]
  if username not in list(data.keys()):
    data[username] = Encode(password)
    db["accountInfo"] = data

"""Print("=============")
Print("----Notes----")
Print("=============")
sleep(1)

Print("Welcome to \"Notes\"!"); sleep(1)
Print("\"Notes is\" a data based note system, for YOUR notes."); sleep(1)
Print("Your account is locked by a password which YOU choose."); sleep(1)
Print("It's best not to use any of your real passwords.", nL=False); sleep(1)
Print("Press \"e\" to cancel any key input."); sleep(1)
Print(" [Press any key to continue!]", nL=False)
getch()
print()"""

def StartUI():
  Flush("\n")
  Print("Sign in[i] or sign up[u]: ", nL=False)
  while True:
    sign = getch()
    if sign == "i":
      Print("Sign in"); sleep(1)
      Flush("\n")
      SignIn()
      break
    elif sign == "u":
      Print("Sign up"), sleep(1)
      Flush("\n")
      SignUp()
      break
    else:
      Flush("\nSign in[i] or sign up[u]: ")
      continue

def SignIn():
  global db
  in_ = None
  cont = True
  while cont:
    Print("Username: ", nL=False)
    username = input()
    if username in list(dict(db["accountInfo"]).keys()):
      Print("Password: ", nL=False)
      password = input()
      if CheckPassword(username, password):
        Print("Correct! To be continued!")
        exit()
        key = None
        Flush("\n")
        Print("Wrong password or user!", nL=False); sleep(0.5)
        Print(" Try again[a] or cancel[e]: ", nL=False); sleep(0.5)
        while True:
          if key != None:
            Flush("\nWrong password or user! Try again[a] or cancel[e]: ")
          key = getch()
          if key == "a":
            break
          elif key == "e":
            cont = False
            break
          else:
            Print("Invalid input!"); sleep(0.5)
            Print("Try again!"); sleep(0.5)
            continue
        Flush("\n")
        continue
    else:
      Flush("\n")
      Print("This user doesn't exist.", nL=False); sleep(0.5)
      Print(" Try again[a] or create new account[c]: ", nL=False)
      while True:
        if in_ != None:
          Flush("\nThis user doesn't exist. Try again[a] or create new account[c]: ")
        in_ = getch()
        if in_ == "a":
          Flush("\n")
          break
        elif in_ == "c":
          Print("To be continued...")
          exit()
        elif in_ == "e":
          cont = False
          break
        else:
          continue

def SignUp():
  global passwordLettersEncode
  while True:
    Print("Username: ", nL=False)
    username = input()
    if username == "":
      Print("It's empty!", nL=False); sleep(0.5)
      Print(" Try again!", nL=False); sleep(0.5)
      Flush("\n")
      continue
    else:
      break
  
  while True:
    Flush("\n")
    Print("Password: ", nL=False); sleep(0.5)
    password = input()
    if password != "":
      for c in password:
        if c in passwordLettersEncode:
          continue
        else:
          pass

#  Print("Password: ", nL=False)
#  password = input()

def NotesUI():
  pass

def Settings():
  pass

def Main():
	while True:
		StartUI()

if __name__ == "__main__":
  Main()