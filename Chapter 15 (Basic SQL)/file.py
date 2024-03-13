import re

fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
    line = line.rstrip()
    orgs = re.findall(r"^.*@(\S+ )", line)
    # orgs = re.findall(r"^From .*@(\S+)", line)
    orgs = re.findall("@([\w.]+)", line)
    for org in orgs:
        print(org)
