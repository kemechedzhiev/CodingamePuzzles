# TODO You are provided with a table which associates MIME types to file extensions. You are also given a list of
#  names of files to be transferred and for each one of these files, you must find the MIME type to be used.
#  The extension of a file is defined as the substring which follows the last occurrence, if any,
#  of the dot character within the file name. If the extension for a given file can be found
#  in the association table (case insensitive, e.g. TXT is treated the same way as txt), then
#  print the corresponding MIME type. If it is not possible to find the MIME type corresponding to a file,
#  or if the file does not have an extension, print UNKNOWN.
#  INPUT
#  Line 1: Number N of elements which make up the association table.
#  Line 2: Number Q of file names to be analyzed.
#  N following lines: One file extension per line and the corresponding MIME type (separated by a blank space).
#  Q following lines: One file name per line.
#  OUTPUT
#  For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type,
#  then display UNKNOWN.
# 4
# 7
# txt text/plain
# tiff image/vector
# css text/css
# png image/png
# example.TXT
# referecnce.txt
# strangename.tiff
# resolv.CSS
# matrix.TiFF
# lanDsCape.Png
# extract.cSs


def check_assertion_of_entries(dataset, association_table):
    for entry in dataset:
        if len(entry.split('.')) > 1:
            file_extension = entry.split('.')[-1]
        else:
            file_extension = entry[0]
        if file_extension.lower() in association_table.keys():
            print(association_table[file_extension.lower()])
        else:
            print('UNKNOWN')


if __name__ == '__main__':
    number_of_association_table_rows = int(input())
    number_of_filenames_to_analyze = int(input())
    association_table = dict()
    dataset = list()
    for i in range(number_of_association_table_rows):
        extension, mimetype = input().split()
        association_table[str(extension).lower()] = str(mimetype)
    for i in range(number_of_filenames_to_analyze):
        dataset.append(str(input()))
    check_assertion_of_entries(dataset, association_table)
