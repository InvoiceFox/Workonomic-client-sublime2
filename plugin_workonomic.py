import sublime
import sublime_plugin
import urllib
import urllib2
import threading
import re
import base64



class WorkonomicCommand(sublime_plugin.WindowCommand):
    def run(self, message=""):
        if message == "":
            self.window.show_input_panel("Goto Line:", "", self.on_done, None, None)
        else:
            self.on_done(message)

    def on_done(self, message):
        threads = []
        thread = WorkonomicApibotCall(message,10)
        threads.append(thread)
        thread.start()
        self.handle_threads(threads)




    def handle_threads(self, threads, offset=0, i=0, dir=1):
        next_threads = []
        for thread in threads:
            if thread.is_alive():
                next_threads.append(thread)
                continue
            if thread.result == False:
                continue
            offset = self.replace(thread)
        threads = next_threads

        if len(threads):
            # This animates a little activity indicator in the status area
            before = i % 8
            after = (7) - before
            if not after:
                dir = -1
            if not before:
                dir = 1
            i += dir
            #self.view.set_status('workonomic', 'workonomic [%s=%s]' % \
            #    (' ' * before, ' ' * after))

            sublime.set_timeout(lambda: self.handle_threads(threads, offset, i, dir), 100)
            return

    def replace(self, thread): ##TODO -- remove
        sublime.message_dialog(thread.result)

class WorkonomicApibotCall(threading.Thread):
    def __init__(self, message, timeout):
        self.APITOKEN = "--ENTER--YOUR--TOKEN--HERE--"
        self.message = message
        self.timeout = timeout
        self.result = None
        threading.Thread.__init__(self)

    def run(self):
        try:
            data = urllib.urlencode({'msg' : self.message})
            base64string = base64.encodestring('%s:%s' % (self.APITOKEN, "x")).replace('\n', '')
            request = urllib2.Request('http://workonomic.cc/APIBOT')
            request.add_header("Authorization", "Basic %s" % base64string)
            content = urllib2.urlopen(request, data=data).read()
            self.result = content
            print content
            return

        except (urllib2.HTTPError) as (e):
            err = '%s: HTTP error %s contacting API' % (__name__, str(e.code))
        except (urllib2.URLError) as (e):
            err = '%s: URL error %s contacting API' % (__name__, str(e.reason))

        sublime.error_message(err)
        self.result = False
