# KHAI BÁO BIẾN

original_sub = r""""""

punctuation_for_add_punctuation_at_the_end_of_line = "."

modified_subtitle_name_file = "modified_subtitle.srt"
punctuation = [",", ".", "!", "?",  ":", ";", "(", "[", "{"]
punctuation_that_need_upper_the_next_character = [".", "!", "?", ":", ";", "(", "[", "{"] # No comma
punctuation_for_fix_first_character_is_punctuation = [",", "!", "?",  ":", ";"] # No dot, (, [, {
punctuation_for_remove_space_before_punctuation = [",", ".", "!", "?",  ":", ";"] # No [, (, {

# IMPORT LIBRARY

import os, sys

# DEF SUB FUNCTIONS

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def check_if_it_is_ellipsis(line, index):
    if line[index:index+1] == ".." or line[index:index+2] == "...":
        check = True
    return check

def check_if_it_is_subtitle_line_base_on_exact_format(arr):
    arr_of_subtitle_line_index = []
    line_index = 2
    while line_index in range(0,len(arr)):
        line = arr[line_index]
        if line == "":
            line_index += 2
        else:
            arr_of_subtitle_line_index.append(line_index)
        line_index += 1
    return arr_of_subtitle_line_index

def check_if_it_is_subtitle_line_base_on_compare(arr):
    arr_of_subtitle_line_index = []
    for line_index in range(0,len(arr)):
        line = arr[line_index]
        if line != "" and "-->" not in line:
            try:
                check_able_to_be_int = int(line)
            except:
                arr_of_subtitle_line_index.append(line_index)
    return arr_of_subtitle_line_index

# DEF MAIN FUNCTIONS

def fix_odd_space_at_the_beginning_and_the_end_of_sentence(arr, subtitle_index_arr):
    modified_arr = []
    for line_index in range(0,len(arr)):
        line = arr[line_index]
        if line_index in subtitle_index_arr:
            while line[0] == " ":
                line = line[1:len(line)]
            while line[-1] == " ":
                line = line[:-1]
        modified_arr.append(line)
    return modified_arr

def fix_first_character_is_punctuation(arr, subtitle_index_arr):
    modified_arr = []
    for line_index in range(0,len(arr)):
        line = arr[line_index]
        if line_index in subtitle_index_arr:
            while line[0] in punctuation_for_fix_first_character_is_punctuation:
                line = line[1:]
        modified_arr.append(line)
    return modified_arr

def add_space_after_punctuation(arr, subtitle_index_arr):
    modified_arr = []
    for line_index in range(0,len(arr)):
        line = arr[line_index]
        if line_index in subtitle_index_arr:
            line = line.replace(",", ", ").replace(".", ". ").replace("!", "! ").replace("?", "? ").replace(":", ": ").replace(";", "; ")
            while line[-1] == " ":
                line = line[:-1]
        modified_arr.append(line)
    return modified_arr

def remove_double_space(arr, subtitle_index_arr):
    modified_arr = []
    for line_index in range(0,len(arr)):
        line = arr[line_index]
        if line_index in subtitle_index_arr:
            while "  " in line:
                line = line.replace("  ", " ")
        modified_arr.append(line)
    return modified_arr

def upper_the_first_character_of_the_line(arr, subtitle_index_arr):
    modified_arr = []
    for line_index in range(0,len(arr)):
        line = arr[line_index]
        if line_index in subtitle_index_arr:
            line = line.capitalize()
        modified_arr.append(line)
    return modified_arr

def upper_the_first_character_of_sentence(arr, subtitle_index_arr):
    modified_arr = []
    for line_index in range(0,len(arr)):
        line = arr[line_index]
        if line_index in subtitle_index_arr:
            for character_index in range(0,len(line)):
                if line[character_index] in punctuation_that_need_upper_the_next_character:
                    try:
                        line = line[:character_index+1]
                        if line[character_index+1] != " ":
                            line += line[character_index+1].upper()
                            line += line[character_index+2]
                        else:
                            line += line[character_index+1]
                            line += line[character_index+2].upper()
                        line += line[character_index + 3:]
                    except:
                        pass
        modified_arr.append(line)
    return modified_arr

def add_punctuation_at_the_end_of_line(arr, subtitle_index_arr):
    modified_arr = []
    for line_index in range(0,len(arr)):
        line = arr[line_index]
        if line_index in subtitle_index_arr:
            if line[-1] not in punctuation:
                line += "."
        modified_arr.append(line)
    return modified_arr

def remove_space_before_punctuation(arr, subtitle_index_arr):
    modified_arr = []
    check_change = False
    for line_index in range(0,len(arr)):
        line = arr[line_index]
        if line_index in subtitle_index_arr:
            for character_index in range(0,len(line)):
                character = line[character_index]
                if character in punctuation_for_remove_space_before_punctuation:
                    check_change = True
                    while line[character_index-1] == " ":
                        line = line[:character_index-1] + "©" + line[character_index:] # © here is just for mark to be remove later
        if check_change == True:
            line = line.replace("©", "")
            check_change = False
        modified_arr.append(line)
    return modified_arr

# Split subtile variable into tuple (arr)

arr_of_subtitle = original_sub.splitlines()

# CHOOSE TYPE FOR FOMART

ask_which_type_will_the_program_should_run = input("Bạn muốn chạy tool kiểu nào [1, 2] (Default 1): ")

if ask_which_type_will_the_program_should_run == "1" or ask_which_type_will_the_program_should_run == "":
    arr_of_subtitle_line_index = check_if_it_is_subtitle_line_base_on_exact_format(arr_of_subtitle)
elif ask_which_type_will_the_program_should_run == "2":
    arr_of_subtitle_line_index = check_if_it_is_subtitle_line_base_on_compare(arr_of_subtitle)
else:
    print("Error")
    exit

# REMOVE ODD SPACE AT THE BEGINNING & THE END OF THE SETENCE 

ask_fix_odd_space_at_the_beginning_and_the_end_of_sentence = input("Fix thừa khoảng cách đầu + cuối câu [Y/N] (Default Y): ").upper()

if ask_fix_odd_space_at_the_beginning_and_the_end_of_sentence == "Y" or ask_fix_odd_space_at_the_beginning_and_the_end_of_sentence == "":
    arr_of_subtitle = fix_odd_space_at_the_beginning_and_the_end_of_sentence(arr_of_subtitle, arr_of_subtitle_line_index)

# FIX FIRST CHARACTER IS PUNCTUATION

ask_fix_first_character_is_punctuation = input("Xoá dấu câu đứng đầu line [Y/N] (Default Y): ").upper()

if ask_fix_first_character_is_punctuation == "Y" or ask_fix_first_character_is_punctuation == "":
    arr_of_subtitle = fix_first_character_is_punctuation(arr_of_subtitle, arr_of_subtitle_line_index)

# REMOVE DOUBLE SPACE

ask_remove_double_space = input("Xoá double space [Y/N] (Default Y): ").upper()

if ask_remove_double_space == "Y" or ask_remove_double_space == "":
    arr_of_subtitle = remove_double_space(arr_of_subtitle, arr_of_subtitle_line_index)

# ADD SPACE AFTER PUNCTUATION

ask_add_space_after_punctuation = input("Fix không cách đầu câu [Y/N] (Default Y): ").upper()

if ask_add_space_after_punctuation == "Y" or ask_add_space_after_punctuation == "":
    arr_of_subtitle = add_space_after_punctuation(arr_of_subtitle, arr_of_subtitle_line_index)

# REMOVE SPACE BEFORE PUNCTUATION

ask_remove_space_before_punctuation = input("Xoá khoảng cách trước các dấu câu [Y/N] (Default Y): ").upper()

if ask_remove_space_before_punctuation == "Y" or ask_remove_space_before_punctuation == "":
    arr_of_subtitle = remove_space_before_punctuation(arr_of_subtitle, arr_of_subtitle_line_index)

# UPPER THE FIRST CHARACTER OF THE LINE

ask_upper_the_first_character_of_the_line = input("Viết hoa chữ cái đầu tiên của mỗi dòng sub [Y/N] (Default N): ").upper()

if ask_upper_the_first_character_of_the_line == "Y":
    arr_of_subtitle = upper_the_first_character_of_the_line(arr_of_subtitle, arr_of_subtitle_line_index)

# UPPER THE FIRST CHARACTER OF THE SENTENCE

ask_upper_the_first_character_of_sentence = input("Viết hoa chữ cái đầu tiên mỗi câu [Y/N] (Default Y): ").upper()

if ask_upper_the_first_character_of_sentence == "Y" or ask_upper_the_first_character_of_sentence == "":
    arr_of_subtitle = upper_the_first_character_of_sentence(arr_of_subtitle, arr_of_subtitle_line_index)

# ADD PUNCTUATION AT THE END OF SENTENCE

ask_add_punctuation_at_the_end_of_line = input("Thêm dấu cuối câu cho những câu không có dấu cuối câu [Y/N] (Default N): ").upper()

if ask_add_punctuation_at_the_end_of_line == "Y":
    arr_of_subtitle = add_punctuation_at_the_end_of_line(arr_of_subtitle, arr_of_subtitle_line_index)

# Merge final subtitle
final_sub = "\n".join(arr_of_subtitle)

# ASK PRINT FINAL SUB

ask_print_final_sub = input("In subtitle đã modfied [Y/N] (Default N): ").upper()

if ask_print_final_sub == "Y":
    print(final_sub)

# ASK CREATE FINAL SUB FILE 

ask_create_final_sub_file = input("Tạo file subtitle đã chỉnh [Y/N] (Default Y): ").upper()

if ask_create_final_sub_file == "Y" or ask_create_final_sub_file == "":
    if os.path.exists(modified_subtitle_name_file):
        user_input = input("Đã phát hiện file sub bị thay đổi, có muốn xoá và tạo lại? [Y/N] (Default Y): ").upper()
        if user_input == "Y" or user_input == "":
            os.remove(modified_subtitle_name_file)
        else:
            print("Đã huỷ")
            exit
    with open(modified_subtitle_name_file, 'w', encoding="utf-8") as file:
        file.write(final_sub)