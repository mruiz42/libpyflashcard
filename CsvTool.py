import csv
import sys

class CsvTool:
    def __init__(self, path: str, delim: str=','):
        self.delim = delim
        try:
            self.file = open(path, 'r')
        except FileNotFoundError as e:
            sys.exit("Error: " + path + " not found.")


    def get_data(self) -> tuple:
        reader = csv.reader(self.file, delimiter=self.delim)
        out_list = list()
        try:
            for row in reader:
                out_list.append(row)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (self.file.name, reader.line_num, e))
        return out_list

    def denisoski_to_csv(self, outfile: str):
        invalid_lines = list()
        valid_lines = list()
        of = open(outfile, 'w')
        for line in self.file:
            if line[0] == "#":
                invalid_lines.append(line)
                continue
            pos0 = line.find('[')
            pos1 = line.find(']', pos0)
            pos2 = line.find('/', pos1)
            pos3 = line.find('/', pos2+1)
            if pos0 == -1 or pos1 == -1 or pos2 == -1 or pos3 == -1:
                continue
            vocab = line[0:pos0-1]
            pronun = line[pos0+1:pos1]
            defin = line[pos2+1: pos3]
            defin = defin.replace(", ", ";")
            print(vocab, defin, pronun)
            new_line = vocab + self.delim + defin + self.delim + pronun + '\n'
            of.write(new_line)
        of.close()