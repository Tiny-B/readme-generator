import os
from textwrap import dedent
from utils import print_utils as p
from utils import input_utils as i

file_name = ''
num_install_steps = 0;
instructions = []
questions = [
          {"type": "input", "name": "title", "message": "Project Title:\n", "validate": i.check_input},
          {"type": "input", "name": "desc", "message": "Project Description:\n", "validate": i.check_input},
          {"type": "input", "name": "usage", "message": "Usage Information:\n", "validate": i.check_input},
          {"type": "input", "name": "author", "message": "Author:\n", "validate": i.check_input},
          {"type": "input", "name": "contact", "message": "Contact Information:\n", "validate": i.check_input},
        ]
license_choices=[
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
        ]

if __name__ == '__main__':
  # Clear the terminal for a clean working space
  os.system('clear')
  p.print_section_divider('README Generator - Inputs', 'purple');
  p.new_line()

  p.print_label('Enter the details that you want to create the README file with, all fields are required', 'white')
  p.new_line()
  
  answers = i.ask_questions(questions);

  license_ = i.selection("License:", license_choices)
  
  # Must be a number or it will throw error and ask again
  num_install_steps = i.get_number('How many install instruction steps do you wish to add?\n')
  
  while (len(instructions) < num_install_steps):
    new_instruction = input(f'Enter install instruction {len(instructions) + 1}:\n')
    instructions.append(new_instruction)

  p.new_line()
  p.print_section_divider('README Generator - Outputs', 'purple');
  p.new_line()

  p.print_label('Are these details correct?', 'white')
  p.new_line()
  
  p.print_input('Project Title:', answers['title'], 'yellow', 'blue')
  p.print_input('Project Description:', answers['desc'], 'yellow', 'blue')
  for step in instructions:
    p.print_input('Installation Step:', step, 'yellow', 'blue')
  p.print_input('Usage Information:', answers['usage'], 'yellow', 'blue')
  p.print_input('License:', license_, 'yellow', 'blue')
  p.print_input('Author:', answers['author'], 'yellow', 'blue')
  p.print_input('Contact Information:', answers['contact'], 'yellow', 'blue')
  p.new_line()

  # Simple yes or no prompt to double check the details are correct
  is_details_correct =  i.get_confirmation('Create README with these details?')
  
  if is_details_correct:
    # give the user a choice to name the file
    prompt_for_file_name = i.ask_questions([{"type": "input", "name": "file_name", "message": "Give the file a name:\n", "validate": i.check_input}])
    file_name = f'{prompt_for_file_name["file_name"]}.md'

    p.print_label(f'Writing to output/{file_name}', 'red')

    install_steps_text = ''
    for step in instructions:
      install_steps_text += f"""
`{step}`
"""
    table = dedent(f"""\
| ㄟ(≧◇≦)ㄏ | (*^_^*) |
| --- | --- |
| License: | {license_} |
| Author:  | {answers['author']} |
| Contact: | {answers['contact']} |

    """)

    content = f"""
# {answers['title']}

## Project Description

{answers['desc']}

## Installation steps

{install_steps_text}

## Usage Information

{answers['usage']}

{table}
""" 

    with open(f'output/{file_name}', "a") as file:
        file.write(content)

  else:
    p.new_line()
    p.print_label('Exiting', 'red')
