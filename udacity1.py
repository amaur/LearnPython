import os,csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    d=['Title','UK Chart Position', 'Label', 'Released', 'US Chart Position','RIAA Certification', 'BPI Certification']
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        counter =0
        for line in f:
			if(counter ==10):
				break
			fields = line.split(",")
			entry ={}
			
			for i, value in enumerate(fields):
				entry[header[i].strip()]= value.strip()
			data.append(entry)
			counter +=1
	return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
#test()
print(parse_file(DATAFILE))
