# File handling

# External dependenices: I/O, file system (ext4, NTFS, FAT32*, APFS), storage space

# Operating System:
#     - Unix (ext4 , ext2)
#     - Android (Unix kernel, ext4)
#     - MacintOSH -> MacOS (Darwin) (Unix kernel, APFS)
#     - Windows OS (NTFS)
#     - Linux (Unix, ext4)
#     - iOS

# r, r+, a, a+, w, w+, x
# fh = open("./source/sample_text.txt", "r")
#  states:
#     - open
#     - operations
#     - close

# file_content = fh.read() #str
# file_content = fh.readline() #str
# file_content = fh.readlines()  # list

# print(file_content, "\n", len(file_content))

# fh.close()

# fh = open("./source/sample_text.txt", "w")
# fh.write("Hi this is good evening")
# fh.close()

# fh = open("./source/sample_text.txt", "a+")
# print(fh.tell())
# fh.seek(0)
# fh.write("Hi this is good evening")
# fh = open("./source/sample_text.txt", "a+")
# fh.seek(0)
# content = fh.readlines()
# print(content[-1])
# fh.close()


# import json, xml, csv

# dict_content = {"name": "python", "age": 26, "YOB": 1996}
# object_content = json.dumps(dict_content, indent=4)
# with open("./source/sample.json", "w+") as json_fh:
#     json_fh.write(object_content)
#     print(json_fh.read())

# with open("./source/sample.json", "r") as object_content:
#     dict_content = json.load(object_content)
#     print(dict_content)
#     print(type(dict_content))

# import pandas as pd

# dict -> dataframe -> csv

# dict_content = {"name": "python", "age": 26, "YOB": 1996}
# df = pd.DataFrame(dict_content.keys(), dict_content.values())
# df.to_csv('./source/sample.csv')

# dict_content = {"name": "python", "age": 26, "YOB": 1996}
# writer = open('./source/sample.csv', 'w')
# csv_writer = csv.writer(writer)
# csv_writer.writerow(dict_content.keys())
# csv_writer.writerow(dict_content.values())
# csv_writer.writerows([dict_content.keys()])

