from src.parse_file_list import parse_file_list_str


file_list = [
    'total 505728',
    '-rwxrwxrwx@  1 balintpolgar  staff     19624 18 Oct  2016 1.jpg',
    '-rwxrwxrwx@  1 balintpolgar  staff     15083 18 Oct  2016 10432036_643343245754208_672456833_n.jpg',
    '-rwxrwxrwx@  1 balintpolgar  staff    141904  8 Aug  2016 12440751_10208538717256466_6584432540764139509_o.jpg',
    '-rwxrwxrwx@  1 balintpolgar  staff    184369 22 Aug  2016 13923859_1745105679094981_5201829126290799206_o.jpg',
    '-rwxrwxrwx@  1 balintpolgar  staff    654149 24 Aug  2016 14124397_1751844915087724_4789268920827133171_o.jpg',
    '-rwxrwxrwx@  1 balintpolgar  staff      7645 24 May  2017 1442707800b_type_diagram.jpg',
    '-rwxrwxrwx@  1 balintpolgar  staff     23698 18 Aug  2016 150px-Eevee.png',
    '-rwxrwxrwx@  1 balintpolgar  staff    116795  1 Feb  2017 200px-Card_back-Classic.png',
    '-rwxrwxrwx@  1 balintpolgar  staff  18345906 10 May  2017 20170510_110102.mp4',
    '-rwxrwxrwx@  1 balintpolgar  staff     54586  9 Feb  2017 205652_101041653239442_60562_n.jpeg',
    '-rwxrwxrwx@  1 balintpolgar  staff     53511 11 Aug  2016 250px-133Eevee.png',
]

file_list_incorrect = [
    'total 505728',
    '-rwxrwxrwx@  1 balintpolgar  staff     x19624 18 Oct  2016 1.jpg',
    '-rwxrwxrwx@  1 balintpolgar  staff     19624 18 Oct  2016 1.jpg',
]


def test_successful_parse():
    parsed_files = parse_file_list_str(file_list)
    # first line is a summary, not matching regular expression
    assert len(parsed_files) == len(file_list) - 1
    assert file_list[1].endswith(parsed_files[0].get('file_name'))
    assert file_list[-1].startswith(parsed_files[-1].get('permissions'))


def test_successful_parse_empty_folder():
    parsed_files = parse_file_list_str([])
    assert len(parsed_files) == 0


def test_unsuccessful_parse_lines_dont_match_regex():
    parsed_files = parse_file_list_str(file_list_incorrect)
    # first line is a summary, not matching regular expression
    # also the second line has a corrupt file size
    assert len(parsed_files) == len(file_list_incorrect) - 2
