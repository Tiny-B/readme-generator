from InquirerPy import prompt, inquirer
from rich.table import Table
import os
from time import sleep
from utils import print_utils as p

instructions = []
questions = [
          {"type": "input", "name": "title", "message": "Project Title:\n"},
          {"type": "input", "name": "desc", "message": "Project Description:\n"},
          {"type": "input", "name": "usage", "message": "Usage Information:\n"},
          {"type": "input", "name": "author", "message": "Author:\n"},
          {"type": "input", "name": "contact", "message": "Contact Information:\n"},
        ]

if __name__ == '__main__':
  os.system('clear')
  p.print_section_divider('README Generator.', 'purple');
  
  answers = prompt(questions)

  license = inquirer.select(
        message="License:",
        choices=[
            ("No license"),
            ("Academic Free License v3.0"),
            ("Apache license 2.0"),
            ("Artistic license 2.0"),
            ("Boost Software License 1.0"),
            ("BSD 2-clause Simplified license"),
            ("BSD 3-clause New or Revised license"),
            ("BSD 3-clause Clear license"),
            ("BSD 4-clause Original or Old license"),
            ("BSD Zero-Clause license"),
            ("Creative Commons license family"),
            ("Creative Commons Zero v1.0 Universal"),
            ("Creative Commons Attribution 4.0"),
            ("Creative Commons Attribution ShareAlike 4.0"),
            ("Do What The F*ck You Want To Public License"),
            ("Educational Community License v2.0"),
            ("Eclipse Public License 1.0"),
            ("Eclipse Public License 2.0"),
            ("European Union Public License 1.1"),
            ("GNU Affero General Public License v3.0"),
            ("GNU General Public License family"),
            ("GNU General Public License v2.0"),
            ("GNU General Public License v3.0"),
            ("GNU Lesser General Public License family"),
            ("GNU Lesser General Public License v2.1"),
            ("GNU Lesser General Public License v3.0"),
            ("ISC"),
            ("LaTeX Project Public License v1.3c"),
            ("Microsoft Public License"),
            ("MIT"),
            ("Mozilla Public License 2.0"),
            ("Open Software License 3.0"),
            ("PostgreSQL License"),
            ("SIL Open Font License 1.1"),
            ("University of Illinois/NCSA Open Source License"),
            ("The Unlicense"),
            ("zLib License"),
        ],
        instruction="(Select with up & down arrow keys.)",
    ).execute()
  
  while True:
    try:
        num_install_ins = int(input('How many install instruction steps do you wish to add?\n'))
    except ValueError:
        p.print_label('Number of install steps MUST be a integer!', 'red')
    else:
        break               
  
  while (len(instructions) < num_install_ins):
    new_instruction = input(f'Enter install instruction {len(instructions) + 1}:\n')
    instructions.append(new_instruction)

  print('\n')
  p.print_section_divider('Input.', 'purple');
  
  p.print_input('Project Title:', answers['title'], 'yellow', 'blue')
  p.print_input('Project Description:', answers['desc'], 'yellow', 'blue')
  for step in instructions:
    p.print_input('Installation Step:', step, 'yellow', 'blue')
  p.print_input('Usage Information:', answers['usage'], 'yellow', 'blue')
  p.print_input('License:', license, 'yellow', 'blue')
  p.print_input('Author:', answers['author'], 'yellow', 'blue')
  p.print_input('Contact Information:', answers['contact'], 'yellow', 'blue')

  is_details_correct =  inquirer.confirm(
        message=f'Are these details correct?',
        default=True,
        instruction="(y/n)",
    ).execute()
  
  if is_details_correct:
    p.print_label('Writing to README.md file', 'red')

    install_steps_text = ''
    for step in instructions:
      install_steps_text += f"""
`{step}`
"""
    content = f"""
# {answers['title']}

## Project Description
{answers['desc']}

## Installation steps

{install_steps_text}

## Usage Information
{answers['usage']}

### License: {license}
### Author: {answers['author']}
### Contact: {answers['contact']}
""" 

    with open('README.md', "a") as file:
        file.write(content)

  else:
    p.print_label('exiting', 'red')
  
