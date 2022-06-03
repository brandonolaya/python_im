import random
import os

print("""
                                    Hola Hijo de PUTA 
                                        Welcome to
        ##    ##     ##     ##     ##    #######  ##       ##     ##     ##    ##
        ##    ##    #  #    ###    ##   ##        ###     ###    #  #    ###   ##
        ########   ######   ####   ##   ##  ###   ####   ####   ######   ####  ## 
        ##    ##  ##    ##  ##  ## ##   ##    ##  ## ##### ##  ##    ##  ## ## ##
        ##    ##  ##    ##  ##   ####    ######   ##  ###  ##  ##    ##  ##  ####  GAME
                                    I hope you lose bitch  
""")

def read_data(filepath):
    """read data.txt and agree and list "word"
    """
    words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for word in f:
            words.append(word.strip().upper())
    return words
    
def run():
    data = read_data(filepath="./archivos/data.txt")
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}

    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    
    while True:
        #clear only consoles
        os.system("cls") 
        print("""
                                    Hola Hijo de PUTA 
                                        Welcome to
        ##    ##     ##     ##     ##    #######  ##       ##     ##     ##    ##
        ##    ##    #  #    ###    ##   ##        ###     ###    #  #    ###   ##
        ########   ######   ####   ##   ##  ###   ####   ####   ######   ####  ## 
        ##    ##  ##    ##  ##  ## ##   ##    ##  ## ##### ##  ##    ##  ## ## ##
        ##    ##  ##    ##  ##   ####    ######   ##  ###  ##  ##    ##  ##  ####  GAME
                                    I hope you lose bitch  
        """)
        print("¡Adivina la palabra!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        
        if "_" not in chosen_word_list_underscores:
            os.system("cls") 
            print("""
                      ###       ###    #####     ###     ###     
                       ###     ###   ###   ###   ###     ###    
                        ###   ###   ###     ###  ###     ###               
                         ### ###    ###     ###  ###     ###    
                          #####     ###     ###  ###     ###    
                           ###      ###     ###  ###     ###    
                           ###      ###     ###  ###     ###    
                           ###       ###   ###    ###   ###     
                           ###         #####        #####       

                  ###        #####        ###  ###  ###       ###    ###
                  ###        #####        ###  ###  #####     ###    ###
                   ###      ### ###      ###   ###  ### ###   ###    ###
                    ###    ###   ###    ###    ###  ###  ###  ###    ###
                     ###  ###     ###  ###     ###  ###   ### ###    
                      ######       ######      ###  ###    ######     #
            """)
            print(f'The word is: {chosen_word}')
            break

if __name__ == '__main__':
    run()