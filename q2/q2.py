import os,shutil

directory = "save_our_heroes​"
parent = "./data/"
path = os.path.join(parent,directory)

if os.path.exists(path) and os.path.isdir(path):
    shutil.rmtree(path)
    
os.mkdir(path)


lines = open("./data/compromised_agents.txt").readlines()
lines[-1] = lines[-1].rstrip() +"\n"
open("./data/compromised_agents.txt",'w').writelines(lines)

with open("./data/compromised_agents.txt") as fp:
	Lines = fp.readlines() 
	for line in Lines:
		for filename in os.listdir("./data/top_secret_data"):
			if not filename.startswith('.'):
				path1 = "./data/top_secret_data/" + filename
				with open(path1) as file1:
					totallines = file1.readlines()
					if line in totallines:
						shutil.copy(path1,"./data/save_our_heroes​/")
						break
						
						
#References:
#https://www.geeksforgeeks.org/create-a-directory-in-python/
#https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
#https://stackoverflow.com/questions/327985/how-do-i-modify-the-last-line-of-a-file
