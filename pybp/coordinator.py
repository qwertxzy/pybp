print("Coordinator script:")

while True:
  usr_input = input(">")

  match usr_input.split():
    case ["exit"]:
      print("Exiting.")
      quit()
    case ["help"]:
      print_help()
    case ["createplan"]:
      create_execution_plan()
    case ["editplan"]:
      edit_execution_plan()
    case ["showplan", path]:
      show_execution_plan(path)
    case _:
      print(f"Unknown command {usr_input}, to see a list of possible actions, type 'help'")


############
# Commands #
############

def print_help():
  print("I am a help message.")

def create_execution_plan():
  pass

def edit_execution_plan():
  pass

def show_execution_plan(path):
  pass