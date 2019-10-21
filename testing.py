"""Script to test parse_cinema module"""

import cinema_parse

PARSER = cinema_parse.CinemaParser()

PARSER.extract_raw_content()
PARSER.print_raw_content()
print(PARSER.film_list())
print(PARSER.nearest_session('Facebook'))
