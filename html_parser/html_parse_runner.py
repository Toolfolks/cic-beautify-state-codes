import os
from parser_base import ParserBase

class HtmlParseRunner:

    @staticmethod
    def start_parser(state_key):
        parser_base = ParserBase()
        parser_base.start(state_key)

if __name__ == '__main__':
    # Hard-coded values
    state_key = "MS"
    release_number = "release78"
    release_date = "2020.07.08"

    # Setting environment variables with hard-coded values
    os.environ.setdefault('release_number', release_number)
    os.environ.setdefault('release_date', release_date)

    # Calling the start_parser method with the hard-coded state_key
    HtmlParseRunner.start_parser(state_key)
