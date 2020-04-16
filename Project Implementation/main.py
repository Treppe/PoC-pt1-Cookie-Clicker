"""
Cookie Clicker Simulator
"""

import simpleplot
import math
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._cookies_num = 0.0
        self._time = 0.0
        self._cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        output = ("Total cookies produced:" + str(self._total_cookies) +
                 " Current amount of cookies:" + str(self._cookies_num) + 
                 " Current time in sec:" + str(self._time) + " CPS: " + str(self._cps))
        return output
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._cookies_num
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        history = list(self._history)
        return history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        time = math.ceil((cookies - self.get_cookies()) / self.get_cps())
        if time < 0 :
            time = 0.0
        return float(time)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self._total_cookies += self.get_cps() * time
            self._cookies_num += self.get_cps() * time
            self._time += time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost <= self.get_cookies():
            self._cookies_num -= cost
            self._cps += additional_cps
            self._history.append((self.get_time(), item_name, cost, self._total_cookies))

   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    build_clone = build_info.clone()
    clicker = ClickerState()
    while clicker.get_time() <= duration:
        time_left = duration - clicker.get_time()
        item = strategy(clicker.get_cookies(), clicker.get_cps(), clicker.get_history(), time_left, build_clone)
        if item == None: 
            clicker.wait(time_left)
            break
        time_elapse = clicker.time_until(build_clone.get_cost(item))
        if time_elapse > time_left:
            clicker.wait(time_left)
            return clicker
        clicker.wait(time_elapse)
        clicker.buy_item(item, build_clone.get_cost(item), build_clone.get_cps(item))
        build_clone.update_item(item)
    return clicker

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cookies += cps*time_left
    cheapest_cost = float('inf')
    cheapest_item = None
    for item in build_info.build_items():
        item_cost = build_info.get_cost(item)
        if item_cost <= cookies and item_cost < cheapest_cost:
            cheapest_cost = item_cost
            cheapest_item = item
    return cheapest_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    cookies += cps * time_left
    expensive_cost = float('-inf')
    expensive_item = None
    for item in build_info.build_items():
        item_cost = build_info.get_cost(item)
        if item_cost <= cookies and item_cost > expensive_cost:
            expensive_cost = item_cost
            expensive_item = item
    return expensive_item

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    cookies = cps * time_left
    max_cps_cost = float('-inf')
    best_item = None
    for item in build_info.build_items():
        item_cost = build_info.get_cost(item)
        item_cps = build_info.get_cps(item)
        item_cps_cost = item_cps / item_cost
        if item_cost <= cookies and item_cps_cost > max_cps_cost:
            max_cps_cost = item_cps_cost
            best_item = item
    return best_item
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    #history = state.get_history()
    #print history
    #history = [(item[0], item[3]) for item in history]
    #simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    
    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)


run()
    

