class Meta_platon_protagor:
    directory = '/home/vladislav/var/platon-protagor-fb2'
    filepaths_output_pwb = '/tmp/protagor.txt'
    workpagename = 'Протагор (Платон, Добиаш).pdf'
    range_pages_metric = [
        [-3, 7, 80, False],
    ]
    parse_from_fb2_file = True
    wrap_to_VARtpl = True
    deyatification = True
    colontitul_on_top = True
    colontitul_center_only = False
    do_precorrection = True

class Meta_platon_timeykritiy1883:
    directory = '/home/vladislav/var/platon-timeykritiy1883-fb2'
    filepaths_output_pwb = '/tmp/timeykritiy.txt'
    workpagename = 'Тимей и Критий (Платон, Малеванский).pdf'
    range_pages_metric = [
        [-5, 7, 243, False],
        [-243, 245, 279, False],
        [-279, 281, 307, False],
    ]
    parse_from_fb2_file = True
    wrap_to_VARtpl = True
    deyatification = True
    colontitul_on_top = True
    colontitul_center_only = True
    do_precorrection = True

class Meta_platon_zakoni:
    directory = '/home/vladislav/var/platon-zakoni-fb2'
    filepaths_output_pwb = '/tmp/zakoni.txt'
    workpagename = 'Платоновы разговоры о законах (Платон, Оболенский).pdf'
    range_pages_metric = [
        [-6, 7, 10, True],  # римские цифры
        [-10, 11, 565, False],
    ]
    parse_from_fb2_file = True
    wrap_to_VARtpl = True
    deyatification = True
    colontitul_on_top = True
    colontitul_center_only = True
    do_precorrection = True


class Meta_platon_fedon:
    directory = '/home/vladislav/var/platon-fedon-fb2'
    filepaths_output_pwb = '/tmp/fedon.txt'
    workpagename = 'Федон (Платон, Лебедев).pdf'
    range_pages_metric = [
        [-1, 7, 157, False],
    ]
    parse_from_fb2_file = True
    deyatification = True
    colontitul_center_only = True
    wrap_to_VARtpl = True
    do_precorrection = True


class Meta_platon_pir:
    slug = 'pir'
    # directory = f'/home/vladislav/var/platon-{slug}-fb2'
    directory = f'/home/vladislav/var/platon-{slug}-fb2-fr12'
    filepaths_output_pwb = f'/tmp/{slug}.txt'
    workpagename = 'Пир (Платон, Городецкий).pdf'
    range_pages_metric = [
        [-8, 9, 109, False],
    ]
    parse_from_fb2_file = True
    deyatification = True
    colontitul_center_only = False
    colontitul_on_top = False
    wrap_to_VARtpl = True
    do_precorrection = True

# meta_works = [
#     dict(
#         directory='/home/vladislav/var/platon-fedon-fb2',
#         filepaths_output_pwb='/tmp/fedon.txt',
#         workpagename='Федон (Платон, Лебедев).pdf',
#         range_pages_metric=[
#             [-1, 7, 157],
#         ],
#         deyatification=True,
#         parse_from_fb2_file=True,
#         colontitul_center_only=True,
#         wrap_to_VARtpl=True,
#         do_precorrection=True,
#     ),
#
#     dict(
#         slug='pir',
#         directory=f'/home/vladislav/var/platon-pir-fb2',
#         filepaths_output_pwb=f'/tmp/pir.txt',
#         workpagename='Пир (Платон, Городецкий).pdf',
#         range_pages_metric=[
#             [-1, 7, 157],
#         ],
#         deyatification=True,
#         parse_from_fb2_file=True,
#         colontitul_center_only=False,
#         colontitul_on_top=False,
#         wrap_to_VARtpl=True,
#         do_precorrection=True,
#     )
# ]
# m = Dict2class(meta_works[1])
