def run():
    my_list = [1, "hello", True, 5.8]
    my_dict = {
        "firstna":"Brandon",
        "lastname": "Olaya"
    }

    super_lista = [
        {"firstna":"Brandon","lastname": "Olaya"},
        {"firstna":"Edwin","lastname": "Perrita"},
        {"firstna":"Ivan","lastname": "Lokita"},
        {"firstna":"Valentin","lastname": "Cracksito"},
    ]

    super_dict = {
        "animales": ['dogs', 'cats', 'lions', 'turtles'],
        "numbers": [1, 2, 3, 4, 5, 6],
        "floating_nums": [0.1, 4.5, 8.6]
    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')

if __name__ == '__main__':
    run()