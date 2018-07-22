# -*- coding: utf-8 -*-

import codecs
import re

if __name__ == "__main__":
    news_files = codecs.open('source.txt', 'r', encoding='utf8')
    news_list = news_files.readlines()
    out_file = codecs.open('name_label.txt', 'w', encoding='utf8')
    # content = ''
    for line in news_list:
        #result = re.search("({{person_name.*?}})", line)
        result = re.findall("({{person_name.*?}})", line)
        for result_list in result:
            result_list = result_list.split(":")[1]
            result_list = result_list.split("}")[0]
            out_file.write(result_list.strip())
        #out_file.write(result.group())




    out_file.close()