import json

def json_reader(file_name):
    for row in open(file_name, "r"):
        yield row
                         
if __name__=='__main__':
    
    row_count = 0

    json_gen = json_reader("small_file_400000.jsonlines")

    sorted_file = None
    arr = []

    for row in json_gen:
        json_line = json.loads(row)
        arr.append(json_line)

    def extract_fingerprint(json):
        try:
            # Also convert to int since update_time will be string.  When comparing
            # strings, "10" is smaller than "2".
            return json['data']['leaf_cert']['fingerprint']
        except KeyError:
            return 0

    arr.sort(key=extract_fingerprint)