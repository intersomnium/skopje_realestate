from constants import translation_dict

def translate_func(item_to_translate):
    table  = str.maketrans(translation_dict)
    return item_to_translate.translate(table)