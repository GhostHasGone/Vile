def display_title():
    red = "\033[91m"
    reset = "\033[0m"
    white = "\033[37m"

    title_art = f"""
{white}===================================================================================================================
{red}██    ██ ██ ██      ███████{white}               ████████ ██   ██ ███████      ██████   █████  ███    ███ ███████ 
{red}██    ██ ██ ██      ██{white}                       ██    ██   ██ ██          ██       ██   ██ ████  ████ ██      
{red}██    ██ ██ ██      █████{white}       █████        ██    ███████ █████       ██   ███ ███████ ██ ████ ██ █████   
 {red}██  ██  ██ ██      ██{white}                       ██    ██   ██ ██          ██    ██ ██   ██ ██  ██  ██ ██      
  {red}████   ██ ███████ ███████{white}                  ██    ██   ██ ███████      ██████  ██   ██ ██      ██ ███████ 
{white}=========================================== Victory Is Lost Eternally =============================================={reset}                                                                                                                                                                                         
"""

    print(title_art)
