from multiprocessing import Pool

from src.argument_parser import parse_arguments
from src.connect import connect_and_run_list_command
from src.parse_file_list import parse_file_list_str
from src.compare_files import compare_files


def get_and_parse_list_of_files(host, path):
    file_list = connect_and_run_list_command(host, path)
    return parse_file_list_str(file_list)


if __name__ == "__main__":
    args = parse_arguments()

    pool = Pool()
    n1_parsed = pool.apply_async(get_and_parse_list_of_files, (args.host_1, args.path_1)).get()
    n2_parsed = pool.apply_async(get_and_parse_list_of_files, (args.host_2, args.path_2)).get()
    pool.close()

    outcome = compare_files(n1_parsed, n2_parsed)
    exit(0 if outcome else 1)
