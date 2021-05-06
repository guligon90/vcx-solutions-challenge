# Base imports
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

# Project imports
from src.data_structures.stack import Stack
from src.parallel.common import get_cpu_count, ProcessPool, ProcessPoolType, set_low_priority_to_process
from src.time_complexity.common import Number, TimeRatioType, TIME_COMPLEXITIES


def _push_time_ratio_worker(arguments: List[Any]) -> Dict[str, List[Number]]:
    """Worker function that is used by the process poll."""
    ratios: List[Number] = []
    start_time = datetime.now()
    stack, problem_size, function = arguments

    for size in range(1, problem_size + 1):
        print(f'[{function}][{Stack.push.__name__}] size={size}')

        duration: Number = 0
        start = datetime.now()
        stack.push(1)
        duration = (datetime.now() - start).total_seconds()
        stack.pop_all()

        denominator = TIME_COMPLEXITIES[function]['function']
        # ZeroDivisionError checking. log(n) is not defined at n=1
        ratio: Number = duration / denominator(size) \
            if callable(denominator) and denominator(size) != 0 else duration

        ratios.append(ratio)

    duration_in_secs = (datetime.now() - start_time).total_seconds()

    print(f'\tdone in {duration_in_secs} seconds.')
    return {function: ratios}


def eval_push_time_ratios(problem_size: int = 3000) -> Optional[TimeRatioType]:
    """
    Function that calculates the execution time ratios, for the different time complexities.

    Here, a process pool is created in order to speed up the process of generating
    the lists of time ratios, for each time complexity.
    """
    stack: Stack = Stack()

    time_ratios: Dict[str, Union[str, List[Number]]] = {
        func_name: [] for func_name in TIME_COMPLEXITIES
    }

    arguments: List[Any] = [
        (stack, problem_size, function) for function in TIME_COMPLEXITIES
    ]

    pool: ProcessPoolType = ProcessPool(get_cpu_count(), set_low_priority_to_process)

    for response in pool.imap(_push_time_ratio_worker, arguments):
        time_ratios.update(response)

    time_ratios.update({
        'data_struct_name': Stack.__name__.lower(),
        'target_name': Stack.push.__name__,
    })

    return time_ratios
