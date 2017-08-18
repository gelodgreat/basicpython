import csv
import glob2, os


# with open('./FL_insurance_sample.csv', 'rU') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print (row['policyID'], row['statecode'], row['county'], row['eq_site_limit'])


# os.chdir("./")
# for file in glob2.glob("*.txt"):
#     print file


# list_of_detectedData = []
# with open(file) as f:
#     for line in f:
#         inner_list = [elt.strip() for elt in line.split(',')]
#         list_of_detectedData.append(inner_list)
#         print inner_list

class GeloReader(object):
    def txtReader(txt):
        os.chdir("./")
        # gets all data according to fileformat
        for file in glob2.glob("*.{}".format(txt)):
            # Open files that is in the file format
            with open(file) as myFiles:
                # Loops the lines in opened fles
                for line in myFiles:
                    # Splits the Data
                    inner_list = [elt.strip() for elt in line.split(',')]
                    # Prints data from the list
                    print inner_list
                    # Prints each data per line
                    # for x in inner_list:
                    #     print x

    print txtReader("txt")

    def csvReader(csvFormat):
        for file in glob2.glob("*.{}".format(csvFormat)):
            with open(file, 'rU') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print (
                            row['policyID'],
                            row['statecode'],
                            row['county'],
                            row['eq_site_limit']
                    )


    # print  csvReader("csv")
