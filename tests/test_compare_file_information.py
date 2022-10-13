from src.compare_files import compare_files


file_information_1 = [
    {
        'permissions': '-rw-r--r--',
        'size': '12345',
        'file_name': 'example_file_name.txt',
    },
    {
        'permissions': '-rwxrwxrwx',
        'size': '22345',
        'file_name': 'example_file_name.png',
    },
]

file_information_2 = [
    {
        'permissions': '-rw-r--r--',
        'size': '623423',
        'file_name': 'example_file_name.txt',
    },
    {
        'permissions': '-rwxrwxrwx',
        'size': '22345',
        'file_name': 'example_file_name.jpeg',
    },
]


def test_successful_compare():
    assert compare_files(
        [
            {
                'permissions': '-rw-r--r--',
                'size': '12345',
                'file_name': 'example_file_name.txt',
            },
            {
                'permissions': '-rwxrwxrwx',
                'size': '22345',
                'file_name': 'example_file_name.png',
            },
        ],
        [
            {
                'permissions': '-rw-r--r--',
                'size': '12345',
                'file_name': 'example_file_name.txt',
            },
            {
                'permissions': '-rwxrwxrwx',
                'size': '22345',
                'file_name': 'example_file_name.png',
            },
        ]
    )


def test_unsuccessful_compare_sizes_dont_match():
    assert not compare_files(
        [
            {
                'permissions': '-rw-r--r--',
                'size': '12345',
                'file_name': 'example_file_name.txt',
            },
            {
                'permissions': '-rwxrwxrwx',
                'size': '22345',
                'file_name': 'example_file_name.png',
            },
        ],
        [
            {
                'permissions': '-rw-r--r--',
                'size': '1',
                'file_name': 'example_file_name.txt',
            },
            {
                'permissions': '-rwxrwxrwx',
                'size': '1',
                'file_name': 'example_file_name.png',
            },
        ]
    )


def test_unsuccessful_compare_extensions_dont_match():
    assert not compare_files(
        [
            {
                'permissions': '-rw-r--r--',
                'size': '12345',
                'file_name': 'example_file_name.txt',
            },
            {
                'permissions': '-rwxrwxrwx',
                'size': '22345',
                'file_name': 'example_file_name.png',
            },
        ],
        [
            {
                'permissions': '-rw-r--r--',
                'size': '1',
                'file_name': 'example_file_name.rtf',
            },
            {
                'permissions': '-rwxrwxrwx',
                'size': '1',
                'file_name': 'example_file_name.gif',
            },
        ]
    )


def test_unsuccessful_compare_different_files():
    assert not compare_files(file_information_1, file_information_2)
