"""Centralized error handling with detailed logging."""

import traceback
import sys
import linecache
from datetime import datetime


def custom_exception_handler(exc_type, exc_value, exc_traceback):
    """Custom exception handler that logs all uncaught exceptions with details.

    Args:
        exc_type: Exception type
        exc_value: Exception instance
        exc_traceback: Traceback object
    """
    # Skip KeyboardInterrupt to allow Ctrl+C to work normally
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    # Get the full traceback
    tb_lines = traceback.format_exception(exc_type, exc_value, exc_traceback)

    print("\n" + "=" * 80)
    print("🔴 EXCEPTION INTERCEPTED")
    print("=" * 80)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Exception Type: {exc_type.__name__}")
    print(f"Exception Message: {str(exc_value)}")

    # Extract the exact error location from the last frame
    if exc_traceback:
        tb = exc_traceback
        # Get to the actual error frame (not our error handler)
        while tb.tb_next:
            tb = tb.tb_next

        frame = tb.tb_frame
        filename = frame.f_code.co_filename
        lineno = tb.tb_lineno
        function = frame.f_code.co_name

        print(f"\n📍 Error Location:")
        print(f"  File: {filename}")
        print(f"  Line: {lineno}")
        print(f"  Function: {function}")

        # Show the actual line of code
        try:
            line = linecache.getline(filename, lineno).strip()
            if line:
                print(f"  Code: {line}")
        except:
            pass

        # Show local variables in the error frame
        print(f"\n📊 Local Variables at Error:")
        for var_name, var_value in frame.f_locals.items():
            # Skip very large objects
            var_str = str(var_value)
            if len(var_str) > 200:
                var_str = var_str[:200] + "..."
            print(f"  {var_name} = {var_str}")

    print("\n📜 Full Stack Trace:")
    print("-" * 80)
    print("".join(tb_lines))
    print("=" * 80)

    # Still exit with error code
    sys.exit(1)


def install_error_handler():
    """Install the custom exception handler for the entire application."""
    sys.excepthook = custom_exception_handler
    print("✅ Enhanced error logging enabled")
    print("   All exceptions will be logged with detailed context\n")
