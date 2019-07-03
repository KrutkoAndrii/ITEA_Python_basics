''' Cтворити файл test1.txt. Текст для файла треба взяти за
 наступним посиланням Code Lay-out (весь розділ з усіма підрозділами
 і тільки цей розділ). Необхідно знайти і вивести 5 найпопулярніших слів в
 цьому тексті. Результат потрібно  записати в файл test1_result.txt. '''
import re


def get_sorted_dictionary(point_to_file):
    finding_words = {}
    for line in point_to_file:
        line_clean = re.compile('[^a-zA-Z ]')
        line = line_clean.sub(' ', line)
        for word in line.split():
            finding_words[word.lower()] = finding_words.get(word, 0) + 1
    sorted_dictionary_words = sorted(finding_words.items(),
                                     key=lambda kv: kv[1])
    return sorted_dictionary_words[-5:]


if __name__ == "__main__":
    with open('test1.txt', 'r') as file_input:
        sorted_words = get_sorted_dictionary(file_input)
    file_input.close()
    with open('test1_result.txt', 'w') as file_output:
        for key, val in sorted_words:
            print(key+'\t', val)
            file_output.write('{}\t: {}\n'.format(key, val))
    file_output.close()
