# Base imports
from math import log2 as log
from typing import Callable, Dict, TypeVar, Union


Number = TypeVar('Number', float, int)


_poly_time: Number = lambda n, k: n ** k


TimeComplexitiesType = Dict[str, Dict[str, Union[str, Callable[[int, ], Number]]]]


TIME_RATIO_SCALE_FACTOR = 1000


TIME_COMPLEXITIES: TimeComplexitiesType = {
    'linear': {
        'plot_label': r"$T_{theory}(n) = O(n)$",
        'plot_pattern': 'g+',
        'function': lambda n: _poly_time(n, 1),
    },
    'quadratic': {
        'plot_label': r"$T_{theory}(n) = O(n^2)$",
        'plot_pattern': 'k+',
        'function': lambda n: _poly_time(n, 2),
    },
    'cubic': {
        'plot_label': r"$T_{theory}(n) = O(n^3)$",
        'plot_pattern': 'r+',
        'function': lambda n: _poly_time(n, 3),
    },
    'logn': {
        'plot_label': r"$T_{theory}(n) = O(log(n))$",
        'plot_pattern': 'y+',
        'function': lambda n: log(n),
    },
    'nlogn': {
        'plot_label': r"$T_{theory}(n) = O(n log(n))$",
        'plot_pattern': 'b+',
        'function': lambda n: n * log(n),
    },
}
