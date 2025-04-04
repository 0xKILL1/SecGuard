import subprocess, argparse, json, re, os

parser = argparse.ArgumentParser()
parser.add_argument("--repo", help="The URL of the github repository to test", required=True)
parser.add_argument("--output", help="Name of the rapport JSON file", required=False)
arg = parser.parse_args()

def check(file):
    if not os.path.exists(file):
        return file
    else:
        i=1
        base,ext=os.path.splitext(file)
        while os.path.exists(f"{base}_{i}{ext}"):
            i+=1
        return(f"{file}_{i}.json")

def write(data):
    with open(output,'w') as f:
        json.dump(data,f,indent=2)

def valid_repo(repository):
    if re.match(r"^https?:\/\/(www\.)?github\.com\/[\w-]+(\/[\w.-]+)?\/?$",repository) is None:
        print("The URL doesnt correspond")
        exit(1)
    else:
        return(repository)

def valid_output(name):
    if re.match(r"^(.*?)(\.json)?$",name) is None:
        print("The name doesnt correspond")
        exit(1)
    else:
        return(re.match(r"^(.*?)(\.json)?$",name).group(1)+".json",name)
    
if not arg.repo:
    print("Please give the github URL")
    exit(1)
else:
    repo=valid_repo(arg.repo)

if not arg.output:
    resu=check("Rapport.json")
    output=valid_output(resu)
else:
    output=valid_output(arg.output)

