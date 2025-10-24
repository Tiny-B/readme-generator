from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
import os

console = Console()

if __name__ == '__main__':
  os.system('clear')
  console.rule("[bold Purple]README Generator.")

  questions = [
    {"type": "input", "name": "title", "message": "Project Title:\n"},
    {"type": "input", "name": "desc", "message": "Project Description:\n"},
    {"type": "input", "name": "usage", "message": "Usage Information:\n"},
  ]
  answers = prompt(questions)
  
  
  while True:
    try:
        num_install_ins = int(input('How many install instruction steps do you wish to add?\n'))
    except ValueError:
        console.print(
        f"[bold red]Number of install steps MUST be a integer!"
        )
    else:
        break               

  

  print('\n')
  console.print(
    f"[bold yellow]Project Title: [blue]{answers['title']}[blue]"
  )
  console.print(
    f"[bold yellow]Project Description: [blue]{answers['desc']}[blue]"
  )
  console.print(
    f"[bold yellow]Usage Information: [blue]{answers['usage']}[blue]"
  )
  console.print(
    f"[bold yellow]Number of install steps: [blue]{num_install_ins}[blue]"
  )