from rich.console import Console

console = Console()

def print_section_divider(title, color):
  new_line()
  console.rule(f"[bold {color}]{title}")
  new_line()

def print_label(label, col):
  console.print(
        f"[bold {col}]{label}"
        )
  new_line()

def print_input(label, input, label_col, input_col):
  console.print(
    f"[bold {label_col}]{label} [{input_col}]{input}[{input_col}]"
  )

def print_readme_output(title, desc, steps, usage, license, author, contact):
  print_input('Project Title:', title, 'yellow', 'blue')
  print_input('Project Description:', desc, 'yellow', 'blue')
  for step in steps:
    print_input('Installation Step:', step, 'yellow', 'blue')
  print_input('Usage Information:', usage, 'yellow', 'blue')
  print_input('License:', license, 'yellow', 'blue')
  print_input('Author:', author, 'yellow', 'blue')
  print_input('Contact Information:', contact, 'yellow', 'blue')
  new_line()

def new_line():
  print('\n')