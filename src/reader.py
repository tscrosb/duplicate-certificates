import json

def json_reader(file_name):
    for row in open(file_name, "r"):
        yield row        
                            
if __name__=='__main__':
    
    # row_count = 0

    json_gen = json_reader("ctl_records_sample.jsonlines")
    lines_per_file = 400000
    smallfile = None

    for lineno, line in enumerate(json_gen):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.jsonlines'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()

    