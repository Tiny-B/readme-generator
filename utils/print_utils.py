from rich.console import Console

console = Console()

def print_section_divider(title, color):
  console.rule(f"[bold {color}]{title}")

def print_label(label, col):
  console.print(
        f"[bold {col}]{label}"
        )

def print_input(label, input, label_col, input_col):
  console.print(
    f"[bold {label_col}]{label} [{input_col}]{input}[{input_col}]"
  )