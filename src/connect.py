import subprocess


def connect_and_run_list_command(host, path_to_directory):
    response = subprocess.run(['ssh', host, f'ls -l {path_to_directory}'], capture_output=True)
    if response.returncode != 0:
        raise ConnectionError(f'Connection unsuccessful: {response.stderr}')

    return response.stdout.decode('utf-8').split('\n')


# def connect_and_run_list_command(host, path_to_directory):
#     if host == 'n1':
#         return [
#             'total 505728',
#             '-rwxrwxrwx@  1 balintpolgar  staff     19624 18 Oct  2016 1.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff     15083 18 Oct  2016 10432036_643343245754208_672456833_n.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff    141904  8 Aug  2016 12440751_10208538717256466_6584432540764139509_o.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff    184369 22 Aug  2016 13923859_1745105679094981_5201829126290799206_o.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff    654149 24 Aug  2016 14124397_1751844915087724_4789268920827133171_o.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff      7645 24 May  2017 1442707800b_type_diagram.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff     23698 18 Aug  2016 150px-Eevee.png',
#             '-rwxrwxrwx@  1 balintpolgar  staff    116795  1 Feb  2017 200px-Card_back-Classic.png',
#             '-rwxrwxrwx@  1 balintpolgar  staff  18345906 10 May  2017 20170510_110102.mp4',
#             '-rwxrwxrwx@  1 balintpolgar  staff     54586  9 Feb  2017 205652_101041653239442_60562_n.jpeg',
#             '-rwxrwxrwx@  1 balintpolgar  staff     53511 11 Aug  2016 250px-133Eevee.png',
#         ]
#     if host == 'n2':
#         return [
#             'total 505728',
#             '-rwxrwxrwx@  1 balintpolgar  staff     19624 18 Oct  2016 1.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff     15083 18 Oct  2016 10432036_643343245754208_672456833_n.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff    141904  8 Aug  2016 12440751_10208538717256466_6584432540764139509_o.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff    184369 22 Aug  2016 13923859_1745105679094981_5201829126290799206_o.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff    654149 24 Aug  2016 14124397_1751844915087724_4789268920827133171_o.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff      7645 24 May  2017 1442707800b_type_diagram.jpg',
#             '-rwxrwxrwx@  1 balintpolgar  staff     23698 18 Aug  2016 150px-Eevee.png',
#             '-rwxrwxrwx@  1 balintpolgar  staff    116795  1 Feb  2017 200px-Card_back-Classic.png',
#             '-rwxrwxrwx@  1 balintpolgar  staff  18345906 10 May  2017 20170510_110102.mp4',
#             '-rwxrwxrwx@  1 balintpolgar  staff     54586  9 Feb  2017 205652_101041653239442_60562_n.jpeg',
#             '-rwxrwxrwx@  1 balintpolgar  staff     53510 11 Aug  2016 250px-133Eevee.png',
#         ]
