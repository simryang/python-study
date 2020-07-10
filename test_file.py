import xml.etree.ElementTree as et
import re   #regex

FILEPATHOCTT = 'D:\doc\work\OCF\CTT_2001.0.0\매트리스-openwrt-19231_[20200519].octt'
if False:
    with open(FILEPATHOCTT, 'r', encoding='utf-8') as cttFile:
        content = cttFile.read()
        print(content)
#print(content)



tree = et.parse(FILEPATHOCTT)
root = tree.getroot()