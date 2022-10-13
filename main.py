from src.argument_parser import parse_arguments
from src.connect import connect_and_run_list_command
from src.parse_file_list import parse_file_list_str
from src.compare_files import compare_files


if __name__ == "__main__":
    args = parse_arguments()

    n1_files = connect_and_run_list_command(args.host_1, args.path_1)
    n2_files = connect_and_run_list_command(args.host_2, args.path_2)

    n1_parsed = parse_file_list_str(n1_files)
    n2_parsed = parse_file_list_str(n2_files)

    outcome = compare_files(n1_parsed, n2_parsed)

    print(outcome)
    print(n1_parsed)
    print(n2_parsed)

    exit(0 if outcome else 1)
