import os
from textwrap import dedent
from utils import print_utils as p
from utils import generator as g

if __name__ == '__main__':
  # Clear the terminal for a clean working space
  os.system('clear')
  gen = g.Generator()

  p.print_section_divider('README Generator - Inputs', 'purple');
  p.print_label('Enter the details that you want to create the README file with, all fields are required', 'white')
  
  gen.set_user_input_details()
  gen.set_license()
  gen.set_install_steps()

  p.print_section_divider('README Generator - Outputs', 'purple');
  p.print_label('Are these details correct?', 'white')
  
  # Prints the users outputs for review
  p.print_readme_output(gen.title, gen.desc, gen.steps, gen.usage, gen.license_, gen.author, gen.contact)

  if gen.confirm_details():
    gen.set_file_name()
    gen.generate_markdown()

    p.print_label(f'Writing to output/{gen.file_name}', 'red')
    gen.output_file()
  else:
    p.new_line()
    p.print_label('Exiting', 'red')
