import re
import csv
import sys
import getopt
import os

def convert_actors():
    with open('actors.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('actors.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Name','Title','Year','TV Series','Season No','Episode No','Character As'])
            found_position = False
            for line in f_in:
                line = line.rstrip()
                if found_position == False:
                    if line.lower() == 'the actors list':
                        for i in range(4):
                            next(f_in)

                        found_position = True

                elif line:
                    if line[0] not in [' ', '\t']:
                        last_valid_name = None
                    row = []

                    #name, title, year
                    m = re.search("(.*?)\t+(.*)\s\((\d+).*?\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            last_valid_name = m.group(1)
                        elif last_valid_name == None:
                            continue

                        row.extend([last_valid_name, m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        #character as in square bracket
                        m2 = re.search("\[(.*)\]", line)
                        if m2:
                            row.append(m2.group(1))
                        else:
                            row.append( "")

                        f_out.writerow( row)


def convert_costume_designers():
    with open('costume-designers.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('costume-designers.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Name','Title,Year','TV Series','Season No','Episode No','Character As'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'the costume designers list':
                        for i in range(4):
                            next(f_in)

                        foundposition = True

                elif line:
                    if line[0] not in [' ', '\t']:
                        last_valid_name = None
                    row = []
                    #name, title, year
                    m = re.search("(.*?)\t+(.*)\s\((\d+).*?\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            last_valid_name = m.group(1)
                        elif last_valid_name == None:
                            continue

                        row.extend([last_valid_name, m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        #character as
                        m2 = re.search("\(as\s(.*)\)", line)
                        if m2:
                            row.append(m2.group(1))
                        else:
                            row.append("")

                        f_out.writerow(row)



def convert_actresses():
    with open('actresses.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('actresses.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Name','Title,Year','TV Series','Season No','Episode No','Character As','Billed No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'the actresses list':
                        for i in range(4):
                            next(f_in)

                        foundposition = True

                elif line:
                    if line[0] not in [' ', '\t']:
                        last_valid_name = None
                    row = []
                    #name, title, year
                    m = re.search("(.*?)\t+(.*)\s\((\d+).*?\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            last_valid_name = m.group(1)
                        elif last_valid_name == None:
                            continue

                        row.extend([last_valid_name, m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        #character as in square bracket
                        m2 = re.search("\[(.*)\]", line)
                        if m2:
                            row.append(m2.group(1))
                        else:
                            row.append("")

                        #billed no <#>
                        m3 = re.search("\<(\d+)\>", line)
                        if m3:
                            row.append(m3.group(1))
                        else:
                            row.append("")

                        f_out.writerow( row)




def convert_certificates():
    with open('certificates.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('certificates.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Country','Rating','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'certificates list':
                        for i in range(2):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, country, rating
                    m = re.search('(.*)\s\((\d+)\).*\t+(\w+)\:(\w+)', line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3), m.group(4)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)




def convert_cinematographers():
    with open('cinematographers.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('cinematographers.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Name','Title','Year','TV Series','Season No','Episode No','Character As'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'the cinematographers list':
                        for i in range(4):
                            next(f_in)

                        foundposition = True

                elif line:
                    if line[0] not in [' ', '\t']:
                        last_valid_name = None
                    row = []
                    #name, title, year
                    m = re.search("(.*?)\t+(.*)\s\((\d+).*?\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            last_valid_name = m.group(1)
                        elif last_valid_name == None:
                            continue

                        row.extend([last_valid_name, m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["" "", ""])

                        #character as in round bracket
                        m2 = re.search("\d+\).*\((.+)\)$", line)
                        if m2:
                            row.append(m2.group(1))
                        else:
                            row.append("")

                        f_out.writerow( row)




def convert_composers():
    with open('composers.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('composers.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Name','Title','Year','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'the composers list':
                        for i in range(4):
                            next(f_in)

                        foundposition = True

                elif line:
                    if line[0] not in [' ', '\t']:
                        last_valid_name = None
                    row = []
                    #name, title, year
                    m = re.search("(.*?)\t+(.*)\s\((\d+).*?\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            last_valid_name = m.group(1)
                        elif last_valid_name == None:
                            continue

                        row.extend([last_valid_name, m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)





def convert_countries():
    with open('countries.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('countries.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Country','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'countries list':
                        for i in range(1):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, country
                    m = re.search("(.*)\s\((\d+).*?\).*\t+(.+)$", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_directors():
    with open('directors.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('directors.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Name','Title','Year','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'the directors list':
                        for i in range(4):
                            next(f_in)

                        foundposition = True

                elif line:
                    if line[0] not in [' ', '\t']:
                        last_valid_name = None
                    row = []
                    #name, title, year
                    m = re.search("(.*?)\t+(.*)\s\((\d+).*?\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            last_valid_name = m.group(1)
                        elif last_valid_name == None:
                            continue

                        row.extend([last_valid_name, m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_distributors():
    with open('distributors.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('distributors.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Distributor','Country','Media','TV Series','Season No','Episode No','Country','Media'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'distributors list':
                        for i in range(1):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, distributor
                    m = re.search("(.*)\s\((\d+)\).*\t+(.+)\t+\(\d+\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        #country, media
                        #"#LawstinWoods" (2013) {The Arrival (#1.1)}             Dailymotion [us]        (2014) (worldwide) (video)


                        m2 = re.search(".*\s\(\d+\)\s.*\t+.*\(\d+\)\s+\((.*)\)\s\((.*)\)", line)
                        if m2:
                            row.extend([m2.group(1), m2.group(2)])
                        else:
                            row.extend(["", ""])

                        f_out.writerow( row)



def convert_editors():
    with open('editors.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('editors.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Name','Title','Year','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'the editors list':
                        for i in range(4):
                            next(f_in)

                        foundposition = True

                elif line:
                    if line[0] not in [' ', '\t']:
                        last_valid_name = None
                    row = []
                    #name, title, year
                    m = re.search("(.*?)\t+(.*)\s\((\d+).*?\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            last_valid_name = m.group(1)
                        elif last_valid_name == None:
                            continue

                        row.extend([last_valid_name, m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)




def convert_language():
    with open('language.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('language.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Language','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'language list':
                        for i in range(1):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, country
                    m = re.search("(.*)\s\((\d+).*?\).*\t+(.+)$", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_locations():
    with open('locations.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('locations.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Location','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'locations list':
                        for i in range(1):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, country
                    m = re.search("(.*)\s\((\d+)\)\s.*\s.*\t+(.+)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_movies():
    with open('movies.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('movies.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'movies list':
                        for i in range(2):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, country
                    m = re.search("(.*)\s\((\d+)\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_producers():
    with open('producers.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('producers.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Name','Title','Year','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'the producers list':
                        for i in range(4):
                            next(f_in)

                        foundposition = True

                elif line:
                    if line[0] not in [' ', '\t']:
                        last_valid_name = None
                    row = []
                    #name, title, year
                    m = re.search("(.*?)\t+(.*)\s\((\d+).*?\)\s+", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            last_valid_name = m.group(1)
                        elif last_valid_name == None:
                            continue

                        row.extend([last_valid_name, m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_production_companies():
    with open('production-companies.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('production-companies.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Production Company','Country','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'production companies list':
                        for i in range(1):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, country
                    m = re.search("(.*)\s\((\d+)\).*\t+(.*)\s\[(.*)\]$", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3), m.group(4)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_production_designers():
    with open('production-designers.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('production-designers.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Name','Title','Year','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'the production designers list':
                        for i in range(4):
                            next(f_in)

                        foundposition = True

                elif line:
                    if line[0] not in [' ', '\t']:
                        last_valid_name = None
                    row = []
                    #name, title, year
                    m = re.search("(.*?)\t+(.*)\s\((\d+).*?\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            last_valid_name = m.group(1)
                        elif last_valid_name == None:
                            continue

                        row.extend([last_valid_name, m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_ratings():
    with open('ratings.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('ratings.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['New Distribution','Votes','Rank','Title','Year','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'top 250 movies (25000+ votes)':
                        for i in range(15):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #New distribution, votes, rank, title, year
                    m = re.search("\s+(.*)\s\s(.*)\s\s(.*)\s\s(.*)\s\((\d+)\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_release_dates():
    with open('release-dates.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('release-dates.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Country','Release Date','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'release dates list':
                        for i in range(1):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, country, date
                    m = re.search("(.*)\s\((\d+)\).*\t+(.*?)\:(\d+\s\w+\s\d+)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3), m.group(4)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_sound_mix():
    with open('sound-mix.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('sound-mix.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Sound Mix','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'sound-mix list':
                        for i in range(1):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, country
                    m = re.search("(.*)\s\((\d+)\).*\t+(\w+)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_special_effects_companies():
    with open('special-effects-companies.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('special-effects-companies.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Company','Country','Type of effect','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'special effects companies list':
                        for i in range(1):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, company, country, type of effect
                    m = re.search("(.*)\s\((\d+)\).*\t+(.+)\s\[(\w+)\]\s\((.+)\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_technical():
    with open('technical.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('technical.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Technical','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'technical list':
                        for i in range(4):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, technical
                    m = re.search("(.*)\s\((\d+)\).*\t+(.*)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



def convert_writers():
    with open('writers.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('writers.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Name','Title','Year','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == 'the writers list':
                        for i in range(4):
                            next(f_in)

                        foundposition = True

                elif line:
                    if line[0] not in [' ', '\t']:
                        last_valid_name = None

                    row = []
                    #name, title, year, as
                    m = re.search("(.*?)\t+(.*)\s\((\d+).*?\)", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            last_valid_name = m.group(1)
                        elif last_valid_name == None:
                            continue

                        row.extend([last_valid_name, m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)


def convert_genres():
    with open('genres.list', 'r', encoding= 'ISO-8859-1') as f_in:
        with open('genres.csv', 'w') as f_outfile:
            f_out = csv.writer(f_outfile)
            f_out.writerow(['Title','Year','Genre','TV Series','Season No','Episode No'])
            foundposition = False
            for line in f_in:
                line = line.rstrip()
                if foundposition == False:
                    if line.lower() == '8: the genres list':
                        for i in range(2):
                            next(f_in)

                        foundposition = True

                elif line:
                    row = []
                    #title, year, country
                    m = re.search("(.*)\s\((\d+).*?\).*\t+(.+)$", line)

                    if m is None:
                        if line == re.search("^-+$", line):
                            break
                    else:
                        if m.group(1):
                            row.extend([m.group(1), m.group(2), m.group(3)])

                        #TV series name, season no and episode no
                        m1 = re.search("\{(.*?)\s?\(\#(\d+)\.(\d+)\)\}", line)
                        if m1:
                            row.extend([m1.group(1), m1.group(2), m1.group(3)])
                        else:
                            row.extend(["", "", ""])

                        f_out.writerow( row)



imdb_dict = {
    'actors.list': convert_actors,
    'costume-designers.list': convert_costume_designers,
    'actresses.list' : convert_actresses,
    'certificates.list' : convert_certificates,
    'cinematographers.list' : convert_cinematographers,
    'composers.list' : convert_composers,
    'countries.list' : convert_countries,
    'directors.list' : convert_directors,
    'distributors.list' : convert_distributors,
    'editors.list' : convert_editors,
    'languages.list' : convert_language,
    'locations.list' : convert_locations,
    'movies.list' : convert_movies,
    'producers.list' : convert_producers,
    'production-companies.list' : convert_production_companies,
    'production-designers.list' : convert_production_designers,
    'ratings.list' : convert_ratings,
    'release-dates.list' : convert_release_dates,
    'sound-mix.list' : convert_sound_mix,
    'special-effects-companies.list' : convert_special_effects_companies,
    'technical.list' : convert_technical,
    'writers.list' : convert_writers,
    'genres.list' : convert_genres
}

def usage():
    print ('Usage: ')
    print ('To process specific files')
    print(sys.argv[0] + '[-d <basedir>]' + 'listfile1 listfile2....')
    print ('To process all files')
    print(sys.argv[0] + '[-d <basedir>]' + '-a')


def main():
    imdb_directory = "."
    convert_all_files = False

    try:
        optlist, filelist = getopt.getopt(sys.argv[1:], 'had:')
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for filename in filelist:
        if filename not in imdb_dict:
            print("Invalid file name")
            usage()
            sys.exit(2)


    for opt, arg in optlist:
        if opt == '-h':
            usage()
            sys.exit(2)
        elif opt == '-a' and filelist == []:
            convert_all_files = True
        elif opt == "-d":
            imdb_directory = arg
        else:
            usage()
            sys.exit(2)


    os.chdir(imdb_directory)
    if convert_all_files:
        for filename, fn in imdb_dict.items():
            print( "Processing " + filename + "...", end="", flush=True)
            fn()
            print( " done")
    else:
        for filename in filelist:
            fn = imdb_dict[filename]
            print( "Processing " + filename + "...", end="", flush=True)
            fn()
            print( " done")


if __name__ == "__main__":
    main()