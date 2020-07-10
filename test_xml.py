import xml.etree.ElementTree as et
import re   #regex

FILEPATHOCTT = 'D:\doc\work\OCF\CTT_2001.0.0\매트리스-openwrt-19231_[20200519].octt'

tree = et.parse(FILEPATHOCTT)
root = tree.getroot()

# find ctt failure from ocf test result file
re_p = re.compile('.*_Check_.*ended with result: FAILED')
re_result = set()
for nodeLog in root.iter('message'):
    nodeMessageText = nodeLog.text
    #print (nodeMessageText)
    
    re_m = re_p.match(nodeMessageText)
    if (re_m):
        #print(re.findall('CT.*_Check_[0-9]+', re_m.group()))
        re_result.add(re.findall('CT.*_Check_[0-9]+', re_m.group())[0])
for elem in re_result:
    print(elem)