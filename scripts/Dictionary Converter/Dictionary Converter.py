origin =r"""
"""

import os
import sys
import fnmatch

# Const
gboard_format = r"# Gboard Dictionary version:1"
gboard_macro = "dictionary.txt"

OpenKey_format = r";Compatible OpenKey Macro Data file for UniKey*** version=1 ***"
OpenKey_macro = "OpenKeyMacro.txt"

EVKey_format = r"<<Đây là dòng làm dấu Unicode, không được sửa hoặc xoá dòng này>>"
EVKey_macro = "evkmacro.txt"

UniKey_format = r";DO NOT DELETE THIS LINE*** version=1 ***"
UniKey_macro = "ukmacro.txt"

raw_format = "#raw_key#"
raw_macro = "raw_dictionary.txt"

latex_format = ["\\", "^", "_"]

def convert_to_raw_format(origin,gboard_format,EVKey_format,OpenKey_format,UniKey_format):
	if gboard_format in origin:
		raw = origin.replace(gboard_format,raw_format).replace("	\n","\n").replace("	","#sep#")
	elif EVKey_format in origin:
		raw = origin.replace(EVKey_format,raw_format).replace("	","#sep#")
	elif OpenKey_format in origin:
		raw = origin.replace(":","#sep#")
	elif UniKey_format in origin:
		raw = origin.replace(UniKey_format,raw_format).replace(":","#sep#")
	elif raw_format in origin:
		raw = origin
	else:
		raw = "Không hợp lệ!"
		temp = "Ấn Enter để thoát chương trình..."
		exit
	return raw

def convert_to_gboard_format(raw,raw_format,gboard_format):
	converted_raw = raw.replace(raw_format,gboard_format).replace("\n","	\n").replace("#sep#","	").replace("#raw_key\n","#raw_key")
	return converted_raw

def convert_to_EVKey_format(raw,raw_format,EVKey_format):
	converted_raw = raw.replace(raw_format,EVKey_format).replace("#sep#","f||")
	return converted_raw

def convert_to_OpenKey_format(raw,raw_format,OpenKey_format):
	converted_raw = raw.replace(raw_format,OpenKey_format).replace("#sep#","f:")
	return converted_raw

def convert_to_UniKey_format(raw,raw_format,UniKey_format):
	converted_raw = raw.replace(raw_format,UniKey_format).replace("#sep#","f:")
	return converted_raw

def RemoveLatext(raw):
	modified_content = ""
	for i in raw.splitlines():
		if not (i.startswith("\\") or i.startswith("^") or i.startswith("_") or i.startswith("-")):
			modified_content+= i + "\n"
	converted_dictionary = modified_content
	return converted_dictionary

if origin == ( "\n" or "" ):
	print("Phát hiện không nhập dictionary vào biến trước đó. Vui lòng chọn file .txt trong directory hiện tại!\n")
	list_dir = [f for f in os.listdir() if f.endswith('.txt')]
	for index, file in enumerate(list_dir):
		print(f"{index+1}: {file}")
	chosen_index = int(input("\nNhập số thứ tự file bạn muốn chọn: "))
	with open(list_dir[chosen_index-1], 'r', encoding='utf-8') as file:
		origin = file.read()

print('format: GBoard (G), OpenKey (O), EVKey (E), UniKey (U)')
format_selection = input('Chọn format muốn chuyển đổi sang: ').upper()
ask_for_removelatext = input('Chạy Remove Latext [Y/N]: ').upper()
ask_for_print_out_raw_dictonary = input('In ra raw dictionary [Y/N]: ').upper()
ask_for_create_raw_dictonary_as_file = input('Tạo file raw dictionary trong directory hiện tại [Y/N]: ').upper()
ask_for_print_out_converted_dictonary = input('In ra converted dictionary [Y/N]: ').upper()
ask_for_create_converted_dictionary_as_file = input('Tạo file macro trong directory hiện tại [Y/N]: ').upper()

temp = input('\nFile cần tạo:\n\nGBoard: `dictionary.txt` và nén lại thành .zip\nOpenKey: `OpenKeyMacro.txt`\nEVKey: `evkmacro.txt`\nUniKey: `ukmacro.txt`\n\nNhấn Enter để tiếp tục...\n')

raw = convert_to_raw_format(origin,gboard_format,EVKey_format,OpenKey_format,UniKey_format)

if format_selection == "G":
	converted_raw = convert_to_gboard_format(raw,raw_format,gboard_format)
	macro_file_name = gboard_macro
elif format_selection == "O":
	converted_raw = convert_to_OpenKey_format(raw,raw_format,OpenKey_format)
	macro_file_name = OpenKey_macro
elif format_selection == "E":
	print(r"Đối với EVKey, bạn chỉ có thể in ra màn hình converted dictionary vì nếu dùng tạo file, nó sẽ lỗi (Vì chứa kí tự đặc biệt)")
	temp = input("Ấn Enter để tiếp tục...\n")
	converted_raw = convert_to_EVKey_format(raw,raw_format,EVKey_format)
	macro_file_name = EVKey_macro
elif format_selection == "U":
	converted_raw = convert_to_UniKey_format(raw,raw_format,UniKey_format)
	macro_file_name = UniKey_macro
else:
	temp = input("Bước chọn format không hợp lệ! Ấn Enter để kết thúc...")
	exit()

if ask_for_print_out_raw_dictonary == "Y":
	print(raw)
	temp = input("Nhấn Enter để tiếp tục...\n")

if ask_for_create_raw_dictonary_as_file == "Y":
	if os.path.exists(raw_macro):
		ask_for_overwrite_or_not = input('File raw macro đã hiện có tại đường dẫn hiện tại, có muốn ghi đè [Y/N]: ').upper()
		if ask_for_overwrite_or_not == "Y":
			with open(raw_macro, 'w', encoding="utf-8") as file:
				file.write(raw)
			print("File raw macro đã được tạo ^^")
		else:
			print("Đã huỷ ghi đè!")
			ask_for_print_out_macro = input("Có muốn in ra raw macro không [Y/N]: ").upper()
			if ask_for_print_out_macro == "Y":
				print(raw)
	else:
		with open(macro_file_name, 'w', encoding="utf-8") as file:
			file.write(raw)
			print("File raw macro đã được tạo ^^")

if ask_for_removelatext == "Y":
	converted_dictionary = RemoveLatext(converted_raw)
else:
	converted_dictionary = converted_raw

if ask_for_print_out_converted_dictonary == "Y":
	print(converted_dictionary)
	temp = input("Nhấn Enter để tiếp tục...\n")

if ask_for_create_converted_dictionary_as_file == "Y":
	if os.path.exists(macro_file_name):
		ask_for_overwrite_or_not = input('File macro đã hiện có tại đường dẫn hiện tại, có muốn ghi đè [Y/N]: ').upper()
		if ask_for_overwrite_or_not == "Y":
			with open(macro_file_name, 'w', encoding="utf-8") as file:
				file.write(converted_dictionary)
			print("File macro đã được tạo ^^")
		else:
			print("Đã huỷ ghi đè!")
			ask_for_print_out_macro = input("Có muốn in ra macro không [Y/N]: ").upper()
			if ask_for_print_out_macro == "Y":
				print(raw)
	else:
		with open(macro_file_name, 'w', encoding="utf-8") as file:
			file.write(converted_dictionary)
			print("File macro đã được tạo ^^")