
import csv
from collections import Counter, OrderedDict
from operator import itemgetter

def main():

    header, data = load_csv_data()
    compile_data(header, data)


def load_csv_data():
    
    csv_file = '/home/cneiderer/ds/metis/metisgh/prework/dsp/python/faculty.csv'

    with open(csv_file) as csv_file:
        freader = csv.reader(csv_file)
    
        data = []
        for ridx, rdata in enumerate(freader):
            rdata = [col.strip() for col in rdata]
            if ridx == 0:
                header = rdata
            else:
                data.append(rdata)

    return (header, data)


def compile_data(header, data):
    
    faculty_dict = {}
    faculty_dict2 = {}

    degree_data = []
    title_data = []
    email_data = []
    domain_data = []
    fname_data = []
    lname_data = []
    for person in data:
        degree = person[header.index('degree')].split()
        degree_data += degree
        if len(degree) is 1:
            degree = degree[0]
    
        title = person[header.index('title')].replace(' Biostatistics', '').replace(' of', '').replace(' is', '')
        title_data.append(title)
    
        email = person[header.index('email')]
        email_data.append(email)
        domain_data.append(email.split('@')[1])

        name = person[header.index('name')].split()
        fname = name[0]
        fname_data.append(fname)
        lname = name[-1]
        lname_data.append(lname)
    
        # Q6, Create faculty dictionary
        key = name[-1]
        val = [degree, title, email]
        if key in faculty_dict:
            faculty_dict[key].append(val)
        else:
            faculty_dict[key] = val

        # Q7, Create faculty dictionary with better keys
        key = (fname, lname)
        if key in faculty_dict2:
            faculty_dict2[key].append(val)
        else:
            faculty_dict2[key] = val

    # Q1, Calculate degree frequencies
    deg_freq = Counter(degree_data)
    deg_freq['None'] = deg_freq.pop('0')
    print(deg_freq)

    # Q2, Calculate title frequencies
    title_freq = Counter(title_data)
    print(title_freq)

    # Q3, Print list of email addresses
    print(email_data)

    # Q5, Write list of email addresses to csv file
    with open('faculty_email_address.csv', 'w') as csv_file:
        fwriter = csv.writer(csv_file, delimiter='\n')
        fwriter.writerow(email_data)

    # Q4, Print list of unique email domains
    uniq_domains = set(domain_data)
    print(uniq_domains)

    def print_first_3_pairs(d):
        print({key: d[key] for key in list(d.keys())[:3]})

    # Q6,
    print_first_3_pairs(faculty_dict)

    # Q7,
    print_first_3_pairs(faculty_dict2)

    # Q8,
    print_first_3_pairs(OrderedDict((k, faculty_dict2.get(k)) for k in sorted(faculty_dict2.keys(), key=itemgetter(1, 0))))


if __name__ == "__main__":
    main()
