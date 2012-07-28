import logging

def logfunc(verbose=False):
    def wrapper(function):
        def inner_wrapper(*args, **kwargs):
            logger = logging.getLogger("function_logger")
            logger.setLevel(logging.INFO)
            logger.addHandler(logging.StreamHandler())
            if verbose:
                msg = "Calling function %s with args %s" % \
                      (function.__name__, " , ".join(["%r" % a for a in args] +
                                                     ["%s=%r" % (k,v) for k, v in kwargs.items()]))
            else:
                msg = "Entering %s" % function.__name__
            logger.info(msg)
            result = function(*args, **kwargs)
            logger.info("Leaving %s", function.__name__)
            return result
        return inner_wrapper
    return wrapper
