def error_msg():
    print('Invalid input. Please try again.')

def check_input_str(question, expected_input, name):
    """
    This function checks whether the input string is in the expected format.
    """
    ye = True
    while ye:
        print(question)
        user_input = (f'{name}\'s input: ')
        user_input = user_input.strip().upper()
        if user_input not in expected_input:
          error_msg()
        else:
          ye = False
        return user_input

def check_input_num(question, expected_input, name):
    """
    This function checks whether the input number is in the expected format.
    """
    ye = True
    while ye:
      print(question)
      user_input = (f'{name}\'s input: ')
      user_input = user_input.strip()
      if not user_input.isdecimal():
          error_msg()
      elif user_input not in expected_input():
          error_msg()
      elif user_input in ['', ' ']:
          error_msg()
      else:
          ye = False
    return user_input

def check_blankinput(question):
    """
    This function is for open-ended questions that don't require a specific answer.
    """
    ye = True
    while ye:
        print(question)
        user_input = (f'Player\'s input: ')
        if user_input in ['', ' ']:
            error_msg()
        else:
            ye = False
    return user_input