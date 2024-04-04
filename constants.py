months = {
    "јан.": "01",
    "фев.": "02",
    "мар.": "03",
    "апр.": "04",
    "мај": "05",
    "јун.": "06",
    "јул.": "07",
    "авг.": "08",
    "септ.": "09",
    "окт.": "10",
    "ноем.": "11",
    "дек.": "12"
}

translation_dict = {'а':'a','А':'A','б':'b','Б':'B', 'в':'v','В':'V', 'г':'g','Г':'G', 'д':'d','Д':'D',
     'ѓ':'gj','Ѓ':'Gj', 'е':'e', 'Е':'E', 'ж':'zh', 'Ж':'Zh', 'з':'z', 'З':'Z', 'ѕ': 'dz','Ѕ': 'Dz', 'и':'i', 'И':'I',
     'ј':'j','Ј':'J', 'к':'k','К':'K', 'л':'l', 'Л':'L', 'љ':'lj', 'Љ':'Lj', 'м':'m', 'М':'M',
     'н':'n', 'Н':'N', 'њ':'nj', 'Њ':'Nj', 'о':'o', 'О':'O', 'п':'p','П':'P', 'р':'r', 'Р':'R',
     'с':'s', 'С':'S', 'т':'t', 'Т':'T', 'ќ':'kj', 'Ќ':'Kj', 'у':'u', 'У':'U', 'ф':'f', 'Ф':'F',
     'х':'h', 'Х':'H', 'ц':'c', 'Ц':'C', 'ч':'ch','Ч':'Ch', 'џ':'dj', 'Џ':'Dj', 'ш':'sh', 'Ш':'Sh'}


metadata_fixed = {'data':
                    {'column-format': {'PPP': {'type': 'number'},
                                      'Opstina': {'type': 'text'}
                                       },
                    },
                 'visualize': {'dark-mode-invert': True,
                               'highlighted-series': [],
                               'highlighted-values': [],
                               'sharing': {'enabled': False},
                               'labels': {'max': 1, 'type': 'places', 'places': [], 'enabled': False},
                               'basemap': 'north-macedonia-municipalities',
                               'legends': {'color':
                                                   {'size': 170,
                                                     'title': 'PPP',
                                                     'labels': 'ranges',
                                                     'enabled': True,
                                                     'offsetX': 10,
                                                     'offsetY': 10,
                                                     'reverse': False,
                                                     'labelMax': 'high',
                                                     'labelMin': 'low',
                                                     'position': 'above',
                                                     'hideItems': [],
                                                     'showTitle': True,
                                                     'interactive': True,
                                                     'labelCenter': 'medium',
                                                     'labelFormat': '0,0.[00]',
                                                     'orientation': 'horizontal',
                                                     'customLabels': []
                                                   }
                                          },
                               'tooltip': {'body': '{{ ppp }}',
                                            'title': '{{ opstina }}',
                                            'sticky': True,
                                            'enabled': True
                                          },
                               'zoomable': True,
                               'max-height': 650,
                               'map-padding': 0,
                               'map-type-set': True,
                               'chart-type-set': True,
                               'min-label-zoom': 1,
                               'zoom-button-pos': 'br',
                               'map-label-format': '0,0.[00]',
                               'text-annotations': [],
                               'range-annotations': [],
                               'hide-empty-regions': True,
                               'avoid-label-overlap': True
                              },
                  'axes': {'keys': 'Opstina', 'values': 'PPP'}
                 }