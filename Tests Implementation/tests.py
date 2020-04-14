"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""
import user47_LAyfnSF9Hn_15 as cookie
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
            msg = message + " Computed: " + str(computed)
            msg += " Expected: " + str(expected)
            print msg
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

suite.report_results()
               
