from datetime import datetime


issueNumber = []
openingTime = []
closingTime = []
i=0
with open("Issues_Time.txt", "r") as f:
    for line in f:
        if i==0:
            line = line.replace('\n', '')
            issueNumber.append(line)
            i=1
        elif i==1:
            line = line.replace('\n', '')
            opening = line
            opening = opening.replace(',', '')
            openlist = opening.split(' ')
            openingTime.append(openlist)
            i=2
        elif i==2:
            line = line.replace('\n', '')
            closing = line
            closing = closing.replace(',', '')
            closelist = closing.split(' ')
            closingTime.append(closelist)
            i=3
        else:
            i=0

months = {}
months["Jan"] = '1'
months["Feb"] = '2'
months["Mar"] = '3'
months["Apr"] = '4'
months["May"] = '5'
months["Jun"] = '6'
months["Jul"] = '7'
months["Aug"] = '8'
months["Sep"] = '9'
months["Oct"] = '10'
months["Nov"] = '11'
months["Dec"] = '12'

timeDiff = []
date_format = "%m-%d-%Y %H:%M:%S"
avgtimediff = 0
for i in range(0, len(issueNumber)):
    opening = openingTime[i]
    closing = closingTime[i]
    colon = opening[3].find(':')
    hrs = opening[3][:colon]
    if opening[4] == 'PM' and int(hrs) != 12:
        hrs = int(hrs) + 12
        opening[3] = str(hrs) + opening[3][colon:]
    elif closing[4] == 'AM' and int(hrs) == 12:
        hrs = int(hrs) - 12
        opening[3] = str(hrs) + opening[3][colon:]
    openingt = months[opening[0]] + '-' + opening[1] + '-' + opening[2] + ' ' + opening[3] + ':00'
    colon = closing[3].find(':')
    hrs = closing[3][:colon]
    if closing[4] == 'PM' and int(hrs) != 12:
        hrs = int(hrs) + 12
        closing[3] = str(hrs) + closing[3][colon:]
    elif closing[4] == 'AM' and int(hrs) == 12:
        hrs = int(hrs) - 12
        closing[3] = str(hrs) + closing[3][colon:]
    closingt = months[closing[0]] + '-' + closing[1] + '-' + closing[2] + ' ' + closing[3] + ':00'
    time1 = datetime.strptime(openingt, date_format)
    time2 = datetime.strptime(closingt, date_format)
    diff = time2 - time1
    daystaken = diff.days
    totaltime = diff.days * 24 * 60 * 60 + diff.seconds
    timeDiff.append(totaltime)
    avgtimediff = avgtimediff + totaltime
 

print(timeDiff)
print(avgtimediff/len(issueNumber))
        
        
