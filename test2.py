import schedule
import time
import datetime
import threading
import signal


class Backup_Thread():
    def __init__(self):
        self.on_stop = threading.Event()
        self.thread = None

    def start(self):
        # print(threading.enumerate())
        if self.thread and self.thread.is_alive(): return
        print("=== 스레드 시작")
        print(threading.current_thread().getName())
        self.thread = threading.Thread(target=self.loop_backup)
        self.thread.start()
        # self.thread.join()

    def stop(self):
        if not self.thread: return
        print("=== 스레드 중지")
        # print(threading.current_thread().getName())
        self.on_stop.set()
        # self.thread = None

    def loop_backup(self):
        print("=== 백업 시작")
        print(threading.current_thread().getName())
        for i in range(4):
            print(i)
            time.sleep(1)
        print("=== 백업 끝")
        self.thread = None


# BACKUP_SOCK_PATH = AAV_DIR + '/backups.sock'  #########
# proc_manager = multiprocessing.managers.BaseManager(
#     address= BACKUP_SOCK_PATH, authkey=b'')
_backup_thread = Backup_Thread()


# force_rm(BACKUP_SOCK_PATH)
# _server = proc_manager.get_server()


def on_signal(code, frame):
    # _server.stop_event_set()
    _backup_thread.stop()
signal.signal(signal.SIGTERM, on_signal)
signal.signal(signal.SIGINT, on_signal)
# _backup_thread.start()
# _server.serve_forever()



print("----- main thread start ----- ")

## B스레드 
def subThread():
    schedule.every(10).seconds.do(_backup_thread.start)  
    while True:
        schedule.run_pending()

sThread = threading.Thread(target=subThread)
sThread.daemon = True # (종료시 서브 스레드가 살아있음, 백업진행 중이던 스레드가 바로 종료되버림  )
sThread.start()

print("1. B스레드 생존여부")
print(sThread.is_alive())

cnt = 0
while True:
    cnt+=1
    print(cnt)
    if _backup_thread.on_stop.wait(3): 
        print("====brake=====")
        # print(threading.current_thread())
        break
    # _backup_thread.on_stop.wait(5)
    # print(f"남은 시간 : {schedule.idle_seconds()}")
    # time.sleep(1)

print("----- main thread end ----- ")

print("2. B스레드 생존여부")
print(sThread.is_alive())
print(threading.enumerate())