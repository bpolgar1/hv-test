import re

import src.constants as constants


def parse_file_list_str(file_list):
    file_information = []

    for file_line in file_list:
        if parsed_line := re.findall(constants.ls_line_regex, file_line):
            parsed_line = parsed_line[0]
            file_information.append({
                'permissions': parsed_line[0],
                'links': parsed_line[1],
                'user_name': parsed_line[2],
                'group': parsed_line[3],
                'size': parsed_line[4],
                'modified_date': f'{parsed_line[5]} {parsed_line[6]}',
                'file_name': parsed_line[7],
            })

    return file_information

