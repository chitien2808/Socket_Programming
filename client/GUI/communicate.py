import queue

ipHost = ''
command = ''
processDone = False
status_connection = 0  #0 : disconnect, 1 : connecting, 2 : connected
src_screen = None
blackListCommand = ["saveimage"]
queue_to_main = queue.Queue()
keylogger_txt = None
frameRunningApp = None 
frameProcess = None
status = ""
root_kill = self_kill = None
root_start = self_start = None
kill_id = start_id = None

def init():
    global ipHost, command, status_connection, src_screen, queue_to_main, keylogger_txt
    global frameRunningApp, frameProcess, status, root_kill, self_kill, root_start, self_start
    global kill_id, start_id
    ipHost = ''
    command = ''
    status_connection = 0
    src_screen = None
    queue_to_main = queue.Queue()
    keylogger_txt = None
    frameRunningApp = None 
    frameProcess = None
    status = None
    root_kill = self_kill = None
    root_start = self_start = None
    kill_id = start_id = 0

