import sys

def func_keys(x):
    return(x[1])

def sort_file(filename):

    with open(filename, 'r') as fp:
        data = []
        print("<<"*10, "reading from file", ">>"*10)
        for line in fp:
            content = line.strip().split()
            content[1] = int(content[1])
            data.append(content)
        # sorted_data = sorted(data, key = lambda x:x[1]) # using lambda for key
        sorted_data = sorted(data, key = func_keys)
        print(sorted_data)
    fp.close()
    with open('results.txt', 'w') as fp:
        print("<<"*10, "writing to file", ">>"*10)
        for item in sorted_data:
            item[1] = str(item[1])
            fp.write(' '.join(item))
            fp.write('\n')
    fp.close()
    # lines = [value.strip() for value in line]
    # print(lines)
    # # for item in lines:



def main():
    args = sys.argv[1:]

    if not args:
        print('Enter filename')
        sys.exit(1)

    sort_file(args[-1])

if __name__ == '__main__':
    main()