#!/tools/bin/python
# Program to convert yml file to python dictionary

import yaml
#Creating a file containing variable dict which can be used by downstream files importing pydict.py module
fh = open("pydict.py",'w')
fh.write("dict={")
with open("yamlfile.yml", 'r') as stream:
    try:
        #using load_all instead of load if the yml file contains more than 1 document which is represented by "---"
        docs = yaml.load_all(stream)
    except yaml.YAMLError as exc:
        print(exc)
    #Each document thus created is a dictionary.
    for doc in docs:
        for k,v in doc.items():
            # writing the (k,v) in the dictionary format
            fh.write('\'' + k '\':' + str(v) + ',')
    #Moving 1byte from the end of file it remove the "," at the the end of dictionary.
    fh.seek(-1,2)
    fh.write("}")
    fh.close()
            
