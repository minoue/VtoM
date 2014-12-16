# The base of this code is created by Justin Israel
# https://github.com/justinfx/MayaSublime
# Modifed by Michitaka Inoue

from telnetlib import Telnet
import textwrap
import os
import sys


class VimToMaya(object):

    def __init__(self, path, fileType):

        self.scriptPath = os.path.join(path, "tmpScript.py")
        with open(self.scriptPath) as tmpFile:
            text = tmpFile.read()

        self.script = '"""\n' + text + '"""'
        self.scriptRaw = text

        self.fileType = fileType

        self.PY_CMD_TEMPLATE = textwrap.dedent('''
            import traceback
            import __main__

            namespace = __main__.__dict__.get('_vim_SendToMaya_plugin')

            if not namespace:
                namespace = __main__.__dict__.copy()
                __main__.__dict__['_vim_SendToMaya_plugin'] = namespace

            namespace['__file__'] = {path!r}

            try:
                exec({cmd}, namespace, namespace)
            except:
                traceback.print_exc()
            ''')

    def run(self):
        if self.fileType == "python":
            try:
                connection = Telnet('127.0.0.1', 7002, timeout=3)
            except:
                print "Failed"
                return
            mCmd = self.PY_CMD_TEMPLATE.format(path=self.scriptPath, cmd=self.script)
        else:
            try:
                connection = Telnet('127.0.0.1', 7001, timeout=3)
            except:
                print "Failed"
            mCmd = self.scriptRaw

        system = sys.platform
        if system == "linux2":
            connection.write(mCmd)
        elif system == "darwin":
            connection.write(mCmd.encode(encoding='UTF-8'))
        else:
            connection.write(mCmd.encode(encoding='UTF-8'))
        connection.close()

        print self.fileType + " executed"

