def search_replace_word(input_word_search, input_word_replace):
    input_word_search = input_word_search.lower()
    input_word_replace = input_word_replace.lower()
    search = 0

    with open('input_dz.txt', encoding='utf-8') as f:

        text = f.read()
        text = text.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ')
        words = text.split()

        for i in range(len(words)):
            if words[i].lower() == input_word_search:
                search += 1
                words[i] = input_word_replace
    print(search)

    with open('output_dz.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(words))
        f.write(f'Это слово встречается в тексте {search} раз')

input_word_search = input('Введите слово для поиска: ')
input_word_replace = input('Введите слово для замены: ')

search_replace_word(input_word_search, input_word_replace)

