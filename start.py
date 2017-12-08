import  time;
from support import getSame;
# import util.math;
from util.math import getNowTime;
import fileUtil.filecontrol;
print("hello, world");
if 1==1:
    print("true");
else:
    print("false");
tar=10;
while(tar>0):
    print(tar);
    tar=tar-1;
ticker = time.asctime( time.localtime(time.time()) );
print(ticker);
list1={1,2,3,4,5,6,7};
list2={1,5};
getSame(list1,list2);
getNowTime();
fileUtil.filecontrol.showFile("d:/test.txt");
