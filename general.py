import os

def create_directory(directory):

    if not os.path.exists(directory):
        print('making directory ' + directory)
        os.mkdir(directory)


def create_files(project_name, base_url):

    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,'crawled.txt')

    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Make a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add to existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')



# clear file
def clear(path):
    open(path, 'w').close()





def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results



def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")





















