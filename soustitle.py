from pathlib import Path
import json
import csv


class Subtitle:
    ''' 
        Simple subtitle parser.
        Accepts either subtitle file or string, 
        then returns a dictionary of parsed srt strings
    '''

    def __init__(self, srt_file=None, srt_string=None):
        self.file_path = srt_file
        self.srt_string = srt_string
        self.csv_file = 'output.csv'
        self.json_file = 'output.json'
        self.color_start = '\33[32m'
        self.color_end  = '\33[32m'


    @staticmethod
    def size_in_bytes(size):
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0

    @staticmethod
    def file_size(file_path):
        get_file_size = Path(file_path).stat().st_size
        if Path.is_file(file_path):
            return size_in_bytes(get_file_size)

    @staticmethod
    def format_time_delta(time_delta):
        return time_delta.strip().replace(',', ':')

    def parser(self, file_str=None):
        subtitle_string = []
        try:
            if file_str is None:
                subtitle_line = [line.split("\r\n") for line in self.srt_string.split("\n\n")]
            else:
                subtitle_line = [line.split("\r\n") for line in file_str.split("\n\n")]

            for item in subtitle_line:
                subtitle_list = [sub_list.split('\n') for sub_list in item]
                each_subtitle = [sub for each_subtitle in subtitle_list for sub in each_subtitle]
                split_time = each_subtitle[1].split(' --> ')
                subtitle_string.append({
                    'start_time'   : self.format_time_delta(split_time[0].strip()),
                    'end_time'     : self.format_time_delta(split_time[1].strip()),
                    'subtitle_text': ' '.join(subs.strip() for subs in each_subtitle[2:len(each_subtitle)])
                })
            return subtitle_string
        except ValueError as verr:
            print(f'File format error {verr}')

    def open(self):
        # maybe I don't have to be too strict with the file ext
        if self.file_path.endswith(".srt"):
            try:
                p = Path(self.file_path)
                with p.open(mode='r') as f:
                    file_stream = f.read()
                    return self.parser(file_stream)
            except FileNotFoundError as f_error:
                print(f_error)


    def to_csv(self, dict_list, csv_file=None):
        if csv_file is None:
            output = self.csv_file
        else:
            output = csv_file
        try:
            with open(output, 'w') as f:
                writer = csv.DictWriter(f, dict_list[0].keys())
                writer.writeheader()
                for item in dict_list:
                    writer.writerow(item)
                get_file_size = self.file_size(output)
                msg = f'{self.color_start}\t> {get_file_size} successfully written to {Path(output).resolve()}{self.color_end}'
                return msg
        except IOError:
            print("I/O error")


    def to_json(self, dict, json_file=None):
        if json_file is None:
            output = self.json_file
        else:
            output = json_file
        try:
            with open(output, 'w') as fout:
                json.dump(dict , fout)
                get_file_size = self.file_size(output)
                msg = f'{self.color_start}\t> {get_file_size} successfully written to {Path(output).resolve()}{self.color_end}'
                return msg
        except IOError:
            print("I/O error")
