import pytest
from unittest.mock import patch
from subprocess import CompletedProcess

from src.connect import connect_and_run_list_command

n1_return_value = """total 505728
-rwxrwxrwx@  1 balintpolgar  staff     19624 18 Oct  2016 1.jpg
-rwxrwxrwx@  1 balintpolgar  staff     15083 18 Oct  2016 10432036_643343245754208_672456833_n.jpg
-rwxrwxrwx@  1 balintpolgar  staff    141904  8 Aug  2016 12440751_10208538717256466_6584432540764139509_o.jpg
-rwxrwxrwx@  1 balintpolgar  staff    184369 22 Aug  2016 13923859_1745105679094981_5201829126290799206_o.jpg
-rwxrwxrwx@  1 balintpolgar  staff    654149 24 Aug  2016 14124397_1751844915087724_4789268920827133171_o.jpg
-rwxrwxrwx@  1 balintpolgar  staff      7645 24 May  2017 1442707800b_type_diagram.jpg
-rwxrwxrwx@  1 balintpolgar  staff     23698 18 Aug  2016 150px-Eevee.png
-rwxrwxrwx@  1 balintpolgar  staff    116795  1 Feb  2017 200px-Card_back-Classic.png
-rwxrwxrwx@  1 balintpolgar  staff  18345906 10 May  2017 20170510_110102.mp4
-rwxrwxrwx@  1 balintpolgar  staff     54586  9 Feb  2017 205652_101041653239442_60562_n.jpeg
-rwxrwxrwx@  1 balintpolgar  staff     53511 11 Aug  2016 250px-133Eevee.png"""


def test_unsuccessful_connection():
    with pytest.raises(ConnectionError):
        connect_and_run_list_command('n1', '/mnt/share1/test')


@patch('subprocess.run', return_value=CompletedProcess('', 0, n1_return_value.encode('utf-8')))
def test_successful_connection(mock_return_value):
    assert connect_and_run_list_command('n1', '/mnt/share1/test') == n1_return_value.split('\n')
