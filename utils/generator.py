from textwrap import dedent
from utils import input_utils as i

class Generator:
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
  num_install_steps = 0;
  instructions = []
  markdown_content =  ''

  def __init__(self, title = '', desc = '', steps = [], usage = '', license_ = '', author = '', contact = '', file_name = ''):
    self.title = title
    self.desc = desc
    self.steps = steps
    self. usage = usage
    self.license_ = license_
    self.author = author
    self.contact = contact
    self.file_name = file_name

  # Checks to see if input is blank using the validate key, returns error and asks again if blank
  def set_user_input_details(self):
    answers = i.ask_questions(self.questions);
    self.title = answers['title']
    self.desc = answers['desc']
    self.usage = answers['usage']
    self.author = answers['author']
    self.contact = answers['contact']

  def set_license(self):
    self.license_ = i.selection("License:", self.license_choices)

  # Must be a number or it will throw error and ask again
  def set_install_steps(self):
    self.num_install_steps = i.get_number('How many install instruction steps do you wish to add?\n')
    self.steps = i.get_array_inputs(self.num_install_steps, 'Enter install instruction:')

  # Simple yes or no prompt to double check the details are correct
  def confirm_details(self):
    is_details_correct =  i.get_confirmation('Create README with these details?')
    return is_details_correct
  
  # Have the user name the file
  def set_file_name(self):
    prompt_for_file_name = i.ask_questions([{"type": "input", "name": "file_name", "message": "Give the file a name:\n", "validate": i.check_input}])
    self.file_name = f'{prompt_for_file_name["file_name"]}.md'

  def generate_markdown(self):
    install_steps_text = ''
    for step in self.steps:
      install_steps_text += f"""
`{step}`
"""
    # Remove the indentation otherwise the table wont render
    table = dedent(f"""\
| ㄟ(≧◇≦)ㄏ | (*^_^*) |
| --- | --- |
| License: | {self.license_} |
| Author:  | {self.author} |
| Contact: | {self.contact} |

""")

    self.markdown_content = f"""
# {self.title}

## Project Description

{self.desc}

## Installation steps

{install_steps_text}

## Usage Information

{self.usage}

---

{table}
""" 

  # Output into a dedicated folder for clarity and separation
  def output_file(self):
    with open(f'output/{self.file_name}', "a") as file:
        file.write(self.markdown_content)
