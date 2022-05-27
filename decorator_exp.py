import time
import math
 
#
# Retry decorator with exponential backoff
#
# Call a function which returns True/False to indicate success or failure. On
# failure, wait, and try the function again. On repeated failures, wait longer
# between each successive attempt. If the decorator runs out of attempts, then
# it gives up and returns False, but you could just as easily raise some
# exception.
#
# Source: https://wiki.python.org/moin/PythonDecoratorLibrary#Retry
#
 
def retry(tries, delay=3, backoff=2):
    """Retries a function or method until it returns True.
 
    delay sets the initial delay in seconds, and backoff sets the factor by which
    the delay should lengthen after each failure. backoff must be greater than 1,
    or else it isn't really a backoff. tries must be at least 0, and delay
    greater than 0."""
 
    if backoff <= 1:
        raise ValueError("backoff must be greater than 1")
 
    tries = math.floor(tries)
    if tries < 0:
        raise ValueError("tries must be 0 or greater")
 
    if delay <= 0:
        raise ValueError("delay must be greater than 0")
    print("entered try")
    def deco_retry(f):
        print("entered deco")
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay  # make mutable
 
            rv = f(*args, **kwargs)  # first attempt
            while mtries > 0:
                if rv is True:  # Done on success
                    return True
 
                mtries -= 1      # consume an attempt
                time.sleep(mdelay)  # wait...
                mdelay *= backoff  # make future wait longer
 
                rv = f(*args, **kwargs)  # Try again
 
            return False  # Ran out of tries :-(
 
        return f_retry  # true decorator -> decorated function
    return deco_retry  # @retry(arg[, ...]) -> true decorator


