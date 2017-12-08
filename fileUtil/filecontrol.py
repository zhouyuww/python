import sys,os,codecs

def showFile(path):
      tar = codecs.open(path, 'rU', 'utf-8');
      position = tar.tell();
      print(position);
      # tmp = tar.readline();
      # str = tar.readlines(position);
      print(tar.read());
      tar.write("11111111");
      try:
         print(1/0);
      except  (ValueError):

      # while str:
      #     print(str);
      #     print('\n');
      #     position=position+1;
      #     str = tar.read(position);