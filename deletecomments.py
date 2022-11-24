

import os
def deleteComments(path):
    try:
        my_file = open(path, 'r')
        data=my_file.read()
        clean=""
        commentscount=0
        for i in data.split('\n'):
            if i[0]=="#":
                clean+=i
                clean+='\n'
                commentscount+=1
            else:
                pass
        name=os.path.basename(path)
        with open("clean-"+name,"w") as c:
            c.write(clean)
            c.close()
        my_file.close()
        return commentscount
              
        
                
        
        
    except:
        print("An error occurred with accessing the files")
        return path
        
print(deleteComments("comments.txt"))


