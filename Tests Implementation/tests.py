"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""
import user47_YvFUcz3b88_26 as cookie
class TestSuite:
    """
    Create a suite of tests similar to unittest
    """
    def __init__(self):
        """
        Creates a test suite object
        """
        self.total_tests = 0
        self.failures = 0
    
    def run_test(self, computed, expected, message = ""):
        """
        Compare computed and expected
        If not equal, print message, computed, expected
        """
        self.total_tests += 1
        if computed != expected:
            msg_computed = " Computed: " + str(computed)
            msg_expected = " Expected: " + str(expected)
            print message
            print msg_computed
            print msg_expected
            print
            self.failures += 1
    
    def report_results(self):
        """
        Report back summary of successes and failures
        from run_test()
        """
        msg = "Ran " + str(self.total_tests) + " tests. "
        msg += str(self.failures) + " failures."
        print msg

suite = TestSuite()
clicker = cookie.ClickerState()
#Implement test for get_cookies method
suite.run_test(clicker.get_cookies(), .0, "Test #1: get_cookies()")
suite.run_test(clicker.get_cps(), 1.0, "Test #2: get_cps()")
suite.run_test(clicker.get_time(), .0, "Test #3: get_time()")
suite.run_test(clicker.get_history(), [(0, None, 0 ,0)], "Test #4: get_history")

suite.run_test(clicker.time_until(0), .0, "Test #5a: time_until(0) with 0 cookies")
clicker.cookies_cur_num = 23.0
suite.run_test(clicker.time_until(123), 100.0, "Test #5b: time_until(123) with 23 cookies")
suite.run_test(clicker.time_until(20), .0, "Test #5c: time_until(20) with 23 cookies")

# wait() pseudo tests. I have no idea how to implement expected value for _str_ and don't get a test pseudo-failures
# It prints out a failure even when it's not there
'''
clicker = cookie.ClickerState()
clicker.wait(10)
suite.run_test(clicker, ("Total cookies produced:" + str(10.0) +
                 " Current amount of cookies:" + str(10.0) + 
                 " Current time in sec:" + str(10.0) + " CPS: " + str(1.0)),
               "Test #6a: wait(10) from start state")
clicker = cookie.ClickerState()
clicker.cookies_cur_num = 23.0
clicker.wait(10)
suite.run_test(clicker, ("Total cookies produced:" + str(33.0) +
                 " Current amount of cookies:" + str(33.0) + 
                 " Current time in sec:" + str(10.0) + " CPS: " + str(1.0)),
               "Test #6b: wait(10) with 23 cookies")
clicker = cookie.ClickerState()
clicker.time = 23.0
clicker.wait(10)
suite.run_test(clicker, ("Total cookies produced:" + str(10.0) +
                 " Current amount of cookies:" + str(10.0) + 
                 " Current time in sec:" + str(33.0) + " CPS: " + str(1.0)),
               "Test #6c: wait(10) with 23 seconds")
clicker = cookie.ClickerState()
clicker.cps = 10.0
clicker.wait(10)
suite.run_test(clicker, ("Total cookies produced:" + str(100.0) +
                 " Current amount of cookies:" + str(100.0) + 
                 " Current time in sec:" + str(10.0) + " CPS: " + str(10.0)),
               "Test #6d: wait(10) with 10 CPS")
'''

clicker = cookie.ClickerState()
clicker.buy_item("test", 100, 30)
suite.run_test(clicker.get_history(), [(0, None, 0 , 0)], 'Test #7a: buy_item("test", 100, 30) in start state')
clicker.cookies_cur_num = 100.0
clicker.total_cookies = 200.0
clicker.buy_item("test", 100.0, 30.0)
suite.run_test(clicker.get_history(), [(0, None, 0 , 0), (0, "test", 100 , 200)], 'Test #7b: buy_item("test", 100, 30) with 100 current and 200 total cookies')

# simulate_clicker() pseudo test. Again I have no idea how to compare this strings properly
'''
clicker = cookie.ClickerState()
suite.run_test(cookie.simulate_clicker(cookie.provided.BuildInfo(), cookie.SIM_TIME, cookie.strategy_cursor_broken),
               ("Total cookies produced:" + str(1153308849166.0) +
                 " Current amount of cookies:" + str(6965195661.5) + 
                 " Current time in sec:" + str(10000000000.0) + " CPS: " + str(16.1)), "Test #8: simulate_clicker()")
'''
suite.report_results()
               
