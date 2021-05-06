# Base imports
import sys

# Project imports
from src.time_complexity.stack.plots import (
    generate_push_function_tc_plot,
)


if __name__ == '__main__':
    try:
        generate_push_function_tc_plot()
        sys.exit(0)
    except Exception as exc:
        print(f'{exc.__class__.__name__}: {str(exc)}')
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        sys.exit(0)
