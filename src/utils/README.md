Original function wrapper (before passing in the logger):

```python
def func_wrapper(func):
    """
    Wrapper function to provide start and end logging
    when running functions without interfering with
    other arguments or returned data.
    """
    @functools.wraps(func)
    def log_func_wrapper(*args, **kwargs):
        # logger = [arg for arg in args if isinstance(arg, logging.Logger)][0]
        logger.debug(f"Starting {func.__qualname__} from module:\t{func.__module__}")
        try:
            rtn_data = func(*args, **kwargs)
        except Exception as err:
            logger.critical(pprint.pformat(err))
            raise err
        else:
            return rtn_data
        finally:
            logger.debug(f"Ending {func.__qualname__} from module:\t{func.__module__}")
    return log_func_wrapper
```

Original solution/script wrapper before passing in logging:

```python
def sol_wrapper(func):
    """
    Wrapper function to provide start and end logging
    for entire solution - meant to only run ONCE.
    """
    @functools.wraps(func)
    def log_func_wrapper(*args, **kwargs):
        """
        Wraps function around DEBUG lines to say start & end
        of a solution / script. If the script fails,
        it will log it then gracefully exit so the logs are
        finalized when closing.
        """
        # logger = [arg for arg in args if isinstance(arg, logging.Logger)][0]
        logger.debug(f"{'='*3} Starting of Logs {'='*3}")
        try:
            rtn_data = func(*args, **kwargs)
        except Exception as err:
            # https://stackoverflow.com/a/7787832/10474024
            # logger.critical(f"""There has been an ERROR!!! Be sure to check your logs:
            # {", ".join([item.baseFilename
            #             for item in logger.__dict__['parent'].__dict__['handlers']
            #             if item.__class__.__name__ == "FileHandler"])
            # }""")
            file_names = [h.baseFilename for h in logger.handlers
                        if isinstance(h, logging.FileHandler)]
            logger.critical(f"There's been an ERROR!!! Check your logs: {', '.join(file_names)}")
            logger.debug(pprint.pformat(err))
        else:
            return rtn_data
        finally:
            logger.debug(f'{"="*3} Ending of Logs {"="*3}')
    return log_func_wrapper
```
