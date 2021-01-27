
import schedule
import time
import datetime
import threading
import signal


class Backup_Thread(threading.Thread):
    def __init__(self):
        self.on_stop = threading.Event()
        self.thread = None

    def start(self):
        if self.thread and self.thread.is_alive(): return
        print("=== 스레드 시작")
        # if self.thread: return
        self.thread = threading.Thread(target=self.loop_backup)
        # self.thread.daemon = True
        self.thread.start()
        # self.thread.join()

    def stop(self):
        print("=== 스레드 중지")
        if not self.thread: return
        # self.on_stop.set()
        # self.thread = None

    def loop_backup(self):
        print("=== 백업 시작")
        for i in range(4):
            print(i)
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

print("main thread start")
schedule.every(2).seconds.do(_backup_thread.start)
while True:
    prev_t and self.on_stop.wait(5)
     prev_t = time.monotonic()
    # schedule.run_pending()
    _backup_thread.start()
    # print(f"남은 시간 : {schedule.idle_seconds()}")
    # time.sleep(1)

print("main thread end")
