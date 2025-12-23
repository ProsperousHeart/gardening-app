"""
Example script demonstrating robust, testable logging and decorator usage.

- Uses logger utility from src.utils.logger with RotatingFileHandler for safe,
    production-ready logging.
- All functions are decorated with logger-injecting decorator factories for
    flexible log routing.
- When run as a script, logs go to the production log file.
- When tested, logs can be redirected to a test log file for isolation.

Functions:
    str_func(input_str): Returns a formatted string, logs input and errors.
    print_hi(): Prints 'Hi' and logs the call.
    main(): Runs example functions and logs various messages.

Usage:
    Run directly for production logging, or import and redecorate in tests for
    test log isolation.
"""

from src.utils.logger import create_logger, func_wrapper, sol_wrapper


# even in W mode it appends because of the RotatingFileHandler
log_obj = create_logger(file_name="Template_Repo", file_mode="w")


@func_wrapper(log_obj)
# @func_wrapper
def str_func(input_str: str) -> str:
    """
    Returns a formatted string with the input.

    Args:
        input_str (str): The input string.

    Returns:
        str: A formatted string.
    Raises:
        TypeError: If input_str is None.
    """
    if input_str is None:
        log_obj.error("str_func called with None input.")
        raise TypeError("Input cannot be None")
    log_obj.debug("str_func called with input_str='%s'", input_str)
    return f"You sent:  {input_str}"


@func_wrapper(log_obj)
# @func_wrapper
def print_hi():
    """Prints 'Hi' and logs the call."""
    log_obj.info("print_hi called.")
    print("Hi")


@sol_wrapper(log_obj)
# @sol_wrapper
def main():
    """
    Main function to execute the script.
    """
    print_hi()
    # try:
    #     result = str_func("Hello, World!")
    #     logger.info("str_func result: %s", result)
    # except TypeError as e:
    #     logger.error("Error in str_func: %s", e)
    str_func("Hello, World!")
    log_obj.warning("This is the end!")
    log_obj.critical("This is a critical message, but not an error.")
    log_obj.error("This is an error message, but not an exception.")


if __name__ == "__main__":
    main()
