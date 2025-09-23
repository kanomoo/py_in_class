def read_data(filename):
    fin = open(filename,encoding="utf-8")
    datas = fin.readlines()
    fin.close()
    return(datas)

def main():
    scores = read_data("AllChapter\chapter 9\mydata.txt")
    print(scores)
    datas = read_data("AllChapter\chapter 9\mydata.txt")
    print(datas)

if __name__ == "__main__":
    main()