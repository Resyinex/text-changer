import os
from docx import Document


input_directory_path = ''
output_directory_path = ''
output_word_document = Document()


def file_finder(directory_path):
    """Going through files in directory
    and returning the names or paths of necessary type of files as list"""
    input_dir_content = os.listdir(directory_path)
    list_of_txts = []
    list_of_dirs = []
    for content in input_dir_content:
        content_path = directory_path + '/' + content
        if content.endswith('.txt'):
            list_of_txts.append(content_path)
        elif os.path.isdir(content_path):
            list_of_dirs.append(content)
    return list_of_txts, list_of_dirs


def txt_corrector(txt_input_path):
    """Opening .txt file and changing unnecessary elements,
    than returns changed text as str"""
    with open(r"%s" % txt_input_path, "r") as input_txt:
        input_text = input_txt.read()
        correcting_input = input_text.replace("\n", " ")
        return correcting_input


def txt_saver(text, txt_output_path):
    """Opening .txt and write down all given text with separation at the end"""
    with open(r"%s/output text.txt" % txt_output_path, "a") as output_txt:
        output_txt.write("%s \n\n------------------------------------------------------------------------------"
                         "------------------------------------------------------------\n\n"
                         % text)
    print("Saved text in %s" % txt_output_path)


def main_loop(input_dir_path, output_dir_path):
    txt_list, dir_list = file_finder(input_dir_path)
    for txt_path in txt_list:
        corrected_txt = txt_corrector(txt_path)
        txt_saver(corrected_txt, output_dir_path)
        with open(r"%s/output text.txt" % output_dir_path) as text_for_doc:  # saving text as word document
            for line in text_for_doc:
                output_word_document.add_paragraph(line)
    for directory in dir_list:
        new_input_dir_path = input_dir_path + '/' + directory
        new_output_dir_path = output_dir_path + '/' + directory
        if os.path.isdir(new_output_dir_path) is False:  # checking if there is directory for txt file
            os.makedirs(new_output_dir_path)
        main_loop(new_input_dir_path, new_output_dir_path)
    output_word_document.save("%s/output doc file.docx" % output_dir_path)
    print("saved doc")


if __name__ == '__main__':
    main_loop(input_directory_path, output_directory_path)
