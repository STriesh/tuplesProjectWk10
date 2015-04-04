__author__ = 'Siada Innab-Triesh'

# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day
# for each of the messages. You can pull the hour out
# from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.
# Note that the autograder does not have support
# for the sorted() function.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

split_line = list()
time = list()
hour_of_day=" "
Distribution_hours={}
Distribution_list=list()

for line in handle:
    split_line = line.split(" ")
    # print split_line
    # print len(split_line)
    # print split_line[:1]
    for word in split_line:
        if word == "From":
            # print line, " ", word
            time=split_line[6]
            # print (time, line)
            hour_of_day=time.split(":")[0]
            # print hour_of_day
            if hour_of_day in Distribution_hours:
                Distribution_hours[hour_of_day] += 1
            else:
                Distribution_hours[hour_of_day] = 1

# print Distribution_hours
# print sorted(Distribution_hours.items())


for key, value in  sorted(Distribution_hours.items()):
    temp = [key,value]
    Distribution_list.append(temp)

#
# print Distribution_list

for item in Distribution_list:
    print str(item[0]), item[1]


