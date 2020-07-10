import os
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
    def file_size(file_path):
        get_file_size = os.path.getsize(file_path)
        if get_file_size >= 1000:
            data_size = int(get_file_size) // (1024 * 1024)
            return f'File size is {data_size}Kb'
        else:
            return f'File size is {get_file_size}Bytes'

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
            get_file_size = self.file_size(self.file_path)
            print('\t> ' + get_file_size)

            try:
                with open(self.file_path) as f:
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
                msg = f'{self.color_start}\t> Output successfully written to {os.path.dirname(os.path.abspath(csv_file))}{self.color_end}'
                return msg
        except IOError:
            print("I/O error")


    def to_json(self, dict, json_file=None):
        if json_file is None:
            output = self.json_file
        else:
            output = json_file
        with open(output, 'w') as fout:
            json.dump(dict , fout)
            msg = f'{self.color_start}\t> Output successfully written to {os.path.dirname(os.path.abspath(json_file))}{self.color_end}'
        return msg
