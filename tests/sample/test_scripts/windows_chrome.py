import mechanize
import time

class Transaction(object):
    # def __init__(self):
        # do per-user user setup here
        # this gets called once on user creation
        # pass

    def run(self):
        # create a Browser instance
        br = mechanize.Browser()
        # don't bother with robots.txt
        br.set_handle_robots(False)
        # add a custom header so wikipedia allows our requests
        br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]

        # start the timer
        start_timer = time.time()
        # submit the request
        link = open('link.txt').read()
        resp = br.open(link)
        resp.read()
        # stop the timer
        latency = time.time() - start_timer

        # store the custom timer
        self.custom_timers['Load_Front_Page'] = latency

        # verify responses are valid
        assert (resp.code == 200), 'Bad Response: HTTP %s' % resp.code