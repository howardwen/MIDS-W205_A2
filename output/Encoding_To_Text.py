__author__ = 'HowardW'


import json


# This file converts tweets stored in Json and compiles it into a .text file
def main():
    f = open("NBA_Warriors.txt", "w")
    count = 0
    # This loops over the chunks of Json file
    for i in range(1,23):
        with open("tweets-"+str(i)+".json") as data_file:
            jsonfile = json.load(data_file)
            for line in jsonfile:
                data = line["text"]
                if "#Warriors" in data:
                    count += 1
                    f.write(data.encode("utf-8")+'\n')
    print count
    f.close()

if __name__ == '__main__':
    main()