import time;

def getNowTime():
       nowTime  = time.time();
       print("nowTime:",nowTime);
       print("nowTime asctime",time.asctime(time.localtime(time.time())));