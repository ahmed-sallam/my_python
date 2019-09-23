import os

print('Welcome in my First App with Python.\n')
print("""\
Please choose from the following:
1- Get folder size.
""")

choice = int(input('Enter your choice: '))
print ('I received ', choice)
    
def getFolderSize(start_path = '.'):
    total_size = 0
    n_files=0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            # if not os.path.islink(fp):
            #     total_size += os.path.getsize(fp)   
            if  os.path.isfile(fp):
                total_size += os.path.getsize(fp)
                n_files += 1
    print(n_files, 'files')
    return total_size


if choice == 1:
  path=input('Enter path or press "enter" for root path ')
  sizeInBytes = getFolderSize(path)
  formatedSize=""
  if sizeInBytes >= (1024*1024*1024):
     formatedSize= str(round(sizeInBytes/(1024*1024*1024) , 2)) + " GB"
  elif sizeInBytes >= (1024*1024):
    formatedSize= str(round(sizeInBytes/(1024*1024) , 2)) + " MB"
  elif sizeInBytes >= 1024:
    formatedSize = str(round(sizeInBytes/1024 , 2)) + " KB"
  else:
    formatedSize = str(round(sizeInBytes, 2)) + " Bytes"

  print(formatedSize)
  
