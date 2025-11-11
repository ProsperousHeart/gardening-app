"""
Custom logger utility for the repo-template-python project.

This module provides:
- A create_logger function to configure and return a logger with both file and
    console handlers, each with customizable formats and logging levels.
- Decorators (func_wrapper, sol_wrapper) for automatic logging of function and
    solution execution.
- Security best practices: avoids logging sensitive data and uses safe string
    formatting.

Usage:
    from utils.logger import create_logger
    logger = create_logger(file_name="my_log")
    logger.info("This is an info message.")

Note:
    - Log files are stored in a 'logs' directory by default.
    - Do not log sensitive information (passwords, tokens, PII).
    - See Python logging documentation for more details.
"""

import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import date
from typing import Optional
import functools

import pprint

pp = pprint.PrettyPrinter(indent=4)

today = date.today()

# ===========================================================================
# https://docs.python.org/3.12/howto/logging-cookbook.html#how-to-treat-a-logger-like-an-output-stream
# could be used when considering creation of a class instead of a function
# ===========================================================================

# Cache for logger instances to avoid redundant configuration
_logger_cache = {}


# logging levels:  https://docs.python.org/3/library/logging.html#logging-levels
def create_logger(
    file_name: str = "Test_File",
    file_mode: str = "a",
    file_lvl: int = logging.DEBUG,
    console_lvl: int = logging.WARNING,
    # log_loc:str=f"{os.getcwd()}/logs") -> logging.Logger:
    log_loc: Optional[str] = None,
) -> logging.Logger:
    """
    Takes in the following:
        file_name       STR name of file to write to
        file_mode       STR mode to write file (needs to be checked)
        file_lvl        INT must tie in to logging level INTs (else raise error)
        console_level   INT must tie in to logging level INTs (else raise error)
        log_loc         STR by default will use local script's folder/logs

    With provided inputs, creates & returns a logger object
    with specific formatting for file and console needs.

    Returns:
        Logger: Configured logger instance.

    Security:
        - Do not log sensitive data (passwords, tokens, PII).
        - Use safe string formatting.
    """
    # Normalize log_loc for cache key
    if log_loc is None:
        log_loc = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

    # Create cache key from configuration parameters
    cache_key = (file_name, file_mode, file_lvl, console_lvl, log_loc)

    # Return cached logger if available
    if cache_key in _logger_cache:
        return _logger_cache[cache_key]

    # if file for writing logs does not exist, create it
    if not os.path.exists(log_loc):
        os.makedirs(log_loc)

    log_path = os.path.join(log_loc, f"{today}_{file_name}.log")

    # =======================================================================
    # logging to multiple locations
    # https://docs.python.org/3.12/howto/logging-cookbook.html#logging-to-multiple-destinations
    # =======================================================================

    logger = logging.getLogger(__name__)  # root logger from main script
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # logging_buffer = io.StringIO()
    # logger.addHandler(logging.StreamHandler(logging_buffer))

    # Prevent duplicate handlers
    if not logger.handlers:
        # File handler - max 5 files of 1MB each
        # file_handler = logging.FileHandler(log_path, mode=file_mode, encoding="utf-8")
        file_handler = RotatingFileHandler(
            log_path,
            mode=file_mode,
            maxBytes=1024 * 1024,
            backupCount=5,
            encoding="utf-8",
        )
        file_handler.setLevel(file_lvl)
        file_format = logging.Formatter(
            "%(asctime)s %(filename)-15s %(funcName)-18s %(levelname)-8s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

        # Console handler - log to console (sys.stderr)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_lvl)
        console_format = logging.Formatter(
            "%(name)-12s line %(lineno)-s %(levelname)-8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(console_format)
        logger.addHandler(console_handler)

    # Cache the logger before returning
    _logger_cache[cache_key] = logger
    return logger


def func_wrapper(logger):
    """
    Wrapper function to provide start and end logging
    when running functions without interfering with
    other arguments or returned data.
    """

    def decorator(func):
        """
        Decorator to wrap a function with logging functionality.
        It logs the start and end of the function execution,
        and handles exceptions by logging them as critical errors.
        """

        @functools.wraps(func)
        def log_func_wrapper(*args, **kwargs):
            # logger = [arg for arg in args if isinstance(arg, logging.Logger)][0]
            logger.debug(
                "Starting %s from module:\t%s", func.__qualname__, func.__module__
            )
            try:
                rtn_data = func(*args, **kwargs)
            except Exception as err:
                logger.critical(pp.pformat(err))
                raise err
            else:
                return rtn_data
            finally:
                logger.debug(
                    "Ending %s from module:\t%s", func.__qualname__, func.__module__
                )

        return log_func_wrapper

    return decorator


def sol_wrapper(logger):
    """
    Wrapper function to provide start and end logging
    for entire solution - meant to only run ONCE.
    """

    def decorator(func):
        """
        Decorator to wrap a function with logging functionality.
        It logs the start and end of the function execution,
        and handles exceptions by logging them as critical errors.
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
            logger.debug("===== Starting of Logs =====")
            try:
                rtn_data = func(*args, **kwargs)
            except Exception as err:
                # https://stackoverflow.com/a/7787832/10474024
                # logger.critical(f"""There's been an ERROR!!! Check your logs:
                # {", ".join([item.baseFilename
                #             for item in logger.__dict__['parent'].__dict__['handlers']
                #             if item.__class__.__name__ == "FileHandler"])
                # }""")
                file_names = [
                    h.baseFilename
                    for h in logger.handlers
                    if isinstance(h, logging.FileHandler)
                ]
                logger.critical(
                    "There's been an ERROR! Check your logs: %s", ", ".join(file_names)
                )
                logger.debug(pp.pformat(err))
            else:
                return rtn_data
            finally:
                logger.debug("===== Ending of Logs =====")

        return log_func_wrapper

    return decorator
