# imports

# global variables
dataList = []

# Sourcecode___________
# read in file and populae the list
with open('Files/data.csv', 'r') as dataFile:
    dataFile.readline()
    for line in dataFile:
        dataList.append(line.strip().split(','))

# loop through the list and write data to file
with open('Files/Phonism.txt', 'w') as dataFile:
    dataFile.write('<YealinkIPPhoneDirectory>\n')

    # loop through the list
    for item in dataList:
        dataFile.write('    <DirectoryEntry>\n')
        dataFile.write('        <Name>' + item[0] + '</Name>\n')
        dataFile.write('        <Telephone>' + item[1] + '</Telephone>\n')
        dataFile.write('    </DirectoryEntry>\n')

    dataFile.write('</YealinkIPPhoneDirectory>\n')