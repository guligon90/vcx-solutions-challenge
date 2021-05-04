# Base imports
from datetime import datetime
from typing import Callable, Dict, List, Union

# Project imports
from src.time_complexity.common import Number, TIME_COMPLEXITIES
from src.data_structures.stack import Stack


def _execute_problem(_size: int, _stack: Stack) -> Number:
    """
    Target problem.
    If in fact stack.push has O(1) complexity, this problem will have,
    for each increased size, linear or O(n) complexity.
    """
    print(f'\rExecuting problem with size {_size}...', end='')

    start = datetime.now()
    for _ in range(1, _size + 1):
        _stack.push(1)
    duration: float = (datetime.now() - start).total_seconds()

    return duration


def eval_push_time_ratios(problem_size: int = 3000) -> Dict[str, Union[str, List[Number]]]:
    """
    Function that evaluates the time ratios for each complexity type.
    The problem with variable size, executes repeatedly the stack.push()
    """
    stack: Stack = Stack()

    time_ratios: Dict[str, Union[str, List[Number]]] = {
        func_name: [] for func_name in TIME_COMPLEXITIES
    }

    for function, ratios in time_ratios.items():
        print(f'Evaluating now ratios for {function} time complexity:')

        start_time = datetime.now()

        for size in range(1, problem_size + 1):
            duration: Number = _execute_problem(size, stack)
            ratio: Number = 0
            if function.lower() in ['logn', 'nlogn']:
                ratio = duration  # divide by one. log is not defined at n=1
            else:
                den: Callable = TIME_COMPLEXITIES.get(function)['function']
                ratio = duration / den(size)

            ratios.append(ratio)

        time_ratios.update({function: ratios})
        duration_in_secs = (datetime.now() - start_time).total_seconds()

        print(f'\tdone in {duration_in_secs} seconds.')

    time_ratios.update({
        'data_struct_name': Stack.__name__.lower(),
        'target_name': Stack.push.__name__,
    })

    return time_ratios
