from InquirerPy import prompt, inquirer
from utils import print_utils as p

def check_input(input):
    return len(input.strip()) > 0 or p.print_label('Cannot be blank!', 'red')

def check_num(prompt):
    return int(input(prompt))

def ask_questions(questions):
    return prompt(questions)

def selection(prompt, choices):
    return inquirer.select(
        message=prompt,
        choices=choices,
        instruction="(Select with up & down arrow keys.)",
    ).execute()

def get_array_inputs(num_elements, prompt):
      input_array = []
      while (len(input_array) < num_elements):
        new_element = input(f'{prompt} {len(input_array) + 1}:\n')
        input_array.append(new_element)
      return input_array

def get_confirmation(question):
    return inquirer.confirm(
        message=question,
        default=True,
        instruction="(y/n)",
    ).execute()

def get_number(prompt):
      num = 0
      while True:
        try:
            num = check_num(prompt)
        except ValueError:
            p.print_label('MUST be an integer!', 'red')
        else:
            break
      return num