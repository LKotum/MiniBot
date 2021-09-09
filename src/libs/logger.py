import time
import os

LN = '\n'


def check_format(format):
    list_of_formats = ["%X", "%x", "%X, %x", "%x, %X"]
    if format in list_of_formats:
        return True
    else:
        return False


class logger:
    def __init__(self, **kwargs):
        self.timer = {}
        self.default_info = 'A'
        self.default_path = './debug.log'
        if(kwargs.get('format') == None):
            self.format = "%X"
        else:
            check = check_format(kwargs['format'])
            print(check, kwargs['format'])
            if check:
                self.format = kwargs['format']
            else:
                self.format = "%X"

        if(kwargs.get('time_print') == (None or False)):
            self.time_print = False
        elif(kwargs.get('time_print') == True):
            self.time_print = True
        else:
            self.time_print = False

        if(kwargs.get('debug_mode') == (None or False)):
            self.debug = False
        elif(kwargs.get('debug_mode') == True):
            self.debug = True
        else:
            self.debug = False

        if(kwargs.get('log_mode') == (None or False)):
            self.log = False
        elif(kwargs.get('log_mode') == True):
            self.log = True
        else:
            self.log = False

        if(kwargs.get('path_to_log') == None):
            self.path_to_log = self.default_path
        else:
            self.path_to_log = kwargs['path_to_log']

        if(self.log == True):
            check = os.path.isfile(self.path_to_log)
            if(check == True):
                print("[INFO] Log exist: True")
            else:
                try:
                    print("[INFO] Log exist: Fasle")
                    log = open(self.path_to_log, 'w')
                    log.write('####[LOGGING]####' + LN)
                    log.close()
                except:
                    print("[ERROR] Incorrect path")
                    self.path_to_log = self.default_path
                    log = open(self.path_to_log, 'w')
                    log.write('####[LOGGING]####' + LN)
                    log.close()
            log = open(self.path_to_log, 'a')
            log.close()

    def out(self, text, t='i'):
        out = True
        add = ""
        if(t == 'i'):
            add = "INFO"
        elif(t == 'e'):
            add = "ERROR"
        elif(t == 'd'):
            if(self.debug == True):
                add = "DEBUG"
            elif(self.debug == False):
                out = False
        else:
            add = "..."
        if(self.time_print == True):
            add += " > " + time.strftime(self.format, time.localtime())
        if(out == True):
            print("["+add+"] "+text)
        if(self.log == True):
            log = open(self.path_to_log, 'a')
            log.write("["+add+"] "+text+LN)
            log.close()

    def debug_mode(self, unit=False):
        if(unit == (True or False)):
            self.debug = unit
        else:
            print("[ERROR] True or Fasle")

    def log_mode(self, unit=False):
        if(unit == True):
            self.log = unit
            check = os.path.isfile(self.path_to_log)
            if(check == True):
                print("[INFO] Log exist: True")
            else:
                try:
                    print("[INFO] Log exist: Fasle")
                    log = open(self.path_to_log, 'w')
                    log.write('####[LOGGING]####' + LN)
                    log.close()
                except:
                    print("[ERROR] Incorrect path")
                    self.path_to_log = self.default_path
                    log = open(self.path_to_log, 'w')
                    log.write('####[LOGGING]####' + LN)
                    log.close()
            log = open(self.path_to_log, 'a')
            log.close()

        elif(unit == False):
            self.log = unit
        else:
            print("[ERROR] True or Fasle")

    def path_log(self, path='./debug.log'):
        self.path_to_log = path
        check = os.path.isfile(self.path_to_log)
        if(check == True):
            print("[INFO] Log exist: True")
        else:
            try:
                print("[INFO] Log exist: Fasle")
                log = open(self.path_to_log, 'w')
                log.write('####[LOGGING]####' + LN)
                log.close()
            except:
                print("[ERROR] Incorrect path")
                self.path_to_log = self.default_path
                log = open(self.path_to_log, 'w')
                log.write('####[LOGGING]####' + LN)
                log.close()
        log = open(self.path_to_log, 'a')
        log.close()

    def time(self, unit=False):
        if(unit == (True or False)):
            self.time_print = unit
        else:
            print("[ERROR] True or Fasle")

    def change_format(self, format):
        check = check_format(format)
        if(check == True):
            self.format = format
        else:
            print("[INFO] Set default format")
            self.format = "%X"

    def start(self, name):
        if(self.timer.get(name) == None):
            self.timer[name] = time.monotonic()
            print("[INFO] Start timer: " + name)
            if(self.log == True):
                log = open(self.path_to_log, 'a')
                log.write("[INFO] Start timer: " + name + LN)
                log.close()
        else:
            self.timer[name] = time.monotonic()
            print("[INFO] Restart timer: " + name + LN)
            if(self.log == True):
                log = open(self.path_to_log, 'a')
                log.write("[INFO] Restart timer: " + name + LN)
                log.close()

    def stop(self, name):
        if(self.timer.get(name) == None):
            print("[INFO] No timer: " + name)
            if(self.log == True):
                log = open(self.path_to_log, 'a')
                log.write("[INFO] No timer: " + name + LN)
                log.close()
        else:
            print("[INFO] Stop timer: " + name)
            print(" > Work time: {:>.3f}".format(
                time.monotonic()-self.timer[name]) + " seconds")
            if(self.log == True):
                log = open(self.path_to_log, 'a')
                log.write("[INFO] Stop timer: " + name + LN)
                log.write(" > Work time: {:>.3f}".format(
                    time.monotonic()-self.timer[name]) + " seconds" + LN)
                log.close()
            del self.timer[name]

    def check(self, name):
        if(self.timer.get(name) == None):
            print("[INFO] No timer: " + name)
            if(self.log == True):
                log = open(self.path_to_log, 'a')
                log.write("[INFO] No timer: " + name + LN)
                log.close()
        else:
            print("[INFO] Time timer: " + name)
            print(" > Check time: {:>.3f}".format(
                time.monotonic()-self.timer[name]) + " seconds")
            if(self.log == True):
                log = open(self.path_to_log, 'a')
                log.write("[INFO] Time timer: " + name + LN)
                log.write(" > Check time: {:>.3f}".format(
                    time.monotonic()-self.timer[name]) + " seconds" + LN)
                log.close()

    def clean_log(self):
        check = os.path.isfile(self.path_to_log)
        if(check == True):
            print("[INFO] Log exist: True")
        else:
            try:
                print("[INFO] Log exist: Fasle")
                log = open(self.path_to_log, 'w')
                log.write('####[LOGGING]####' + LN)
                log.close()
            except:
                print("[ERROR] Incorrect path")
                self.path_to_log = self.default_path
                log = open(self.path_to_log, 'w')
                log.write('####[LOGGING]####' + LN)
                log.close()
        log = open(self.path_to_log, 'w')
        log.write('####[LOGGING]####' + LN)
        log.close()
