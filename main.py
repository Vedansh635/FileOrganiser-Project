import os

def organisefile(file_path,file_type):
   listoffiles = os.listdir(file_path)
   count = 1
   for files in listoffiles:
      os.rename(f'{file_path}\\{files}',f'{file_path}\\{count}.{file_type}')
      count+=1
organisefile('test_folder','txt')
