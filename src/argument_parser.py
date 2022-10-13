import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Solutions pulls and compares file information from hosts\' shared folder')
    parser.add_argument(
        '-h1',
        '--host_1',
        help='Hostname or IP address of 1st host',
        required=True,
        type=str,
        metavar='host_1'
    )
    parser.add_argument(
        '-p1',
        '--path_1',
        help='Path to 1st host\'s folder',
        required=True,
        type=str,
        metavar='path_1'
    )
    parser.add_argument(
        '-h2',
        '--host_2',
        help='Hostname or IP address of 2nd host',
        required=True,
        type=str,
        metavar='host_2'
    )
    parser.add_argument(
        '-p2',
        '--path_2',
        help='Path to 2nd host\'s folder',
        required=True,
        type=str,
        metavar='path_2'
    )

    return parser.parse_args()
