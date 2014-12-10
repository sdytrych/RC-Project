#!/usr/bin/python

import re
import sys
from datetime import datetime
import calender


class timestamp:
    def __init__(self, month, day, year, hour, minute, second):
            self.month, self.day, self.year, self.hour, self.minute, self.second = month, day, year, hour, minute, second




read_file = open("parse_file", "r")
output_file = open("output", "w")

alliance = 0
count = 0
start_time = ''
end_time = ''

output_file.write("[center]")

print "%s\n" % sys.argv[2]
print "%s\n" % sys.argv[4]

start_12hour = sys.argv[4]
start_3day = sys.argv[2]

cur_date = datetime.today()


print "%d/%d/%d %d:%d:%d" % (cur_date.month, cur_date.day, cur_date.year, cur_date.hour, cur_date.minute, cur_date.second)

if cur_date.hour > 12:
    end_12hour = timestamp(cur_date.month, cur_date.day, cur_date.year, cur_date.hour-12, cur_date.minute, cur_date.second)
    print "%d/%d/%d %d:%d:%d" % (end_12hour.month, end_12hour.day, end_12hour.year, end_12hour.hour, end_12hour.minute, end_12hour.second)
else:
    if cur_date.day == 1:
        if cur_date.month == 1:
            end_12hour = timestamp(12, 31, cur_date.year-1, cur_date.hour+12, cur_date.minute, cur_date.second)
        else:
            end_12hour = timestamp(cur_date.month-1, calender.monthrange(cur_date.year, cur_date.month-1)[1], cur_date.year, cur_date.hour+12, cur_date.minute, cur_date.second)
    else:
        end_12hour = timestamp(

        


for line in read_file:
    datestamp = re.search(r'((\d{1})|(\d{2}))/((\d{1})|(\d{2}))/(\d{4}) ((\d{1})|(\d{2})):(\d{2}):(\d{2}) [AP]M', line)
    if "Display Nation" in line:
        nation_id = (re.search(r'(\d{6})|(\d{7})', line)).group()
        nation_name = (re.search(r'>(.*)<', line)).group(1)
    elif "Ruler:" in line:
        ruler_name = (re.search(r'"Ruler: (.*)">', line)).group(1)
    elif re.search(r'"Alliance: (.*)">', line) is not None:
        alliance = 1
    elif (datestamp is not None) and "Server Time:" not in line:
        if alliance == 0:
            print "%s - %s - %s - %s" % (nation_name, ruler_name, nation_id, datestamp.group())
            output_file.write("[url=http://www.cybernations.net/send_message.asp?Nation_ID=%s]%s[/url]\n" % (nation_id, nation_name))
        else:
            alliance = 0

        if count == 0:
            start_time = datestamp.group()
        elif count == 39:
            end_time = datestamp.group()
            output_file.write("\nStart: %s - End: %s\n" % (start_time, end_time))
        count += 1
output_file.write("[/center]")
read_file.close()
output_file.close()

