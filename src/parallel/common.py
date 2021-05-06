# Base imports
from multiprocessing import cpu_count, Pool
from multiprocessing.pool import Pool as PoolType
from typing import Optional
import os
import psutil


ProcessPool = Pool
ProcessPoolType = PoolType


def get_cpu_count() -> int:
    return cpu_count()


def _default_priority() -> Optional[int]:
    if psutil.WINDOWS:
        return psutil.BELOW_NORMAL_PRIORITY_CLASS

    if psutil.LINUX:
        return 19

    return None


def set_low_priority_to_process(priority_code: Optional[int] = _default_priority()) -> None:
    """Function called at every process start."""
    process = psutil.Process(os.getpid())

    # Set process to the lowest priority
    if isinstance(priority_code, int):
        process.nice(priority_code)
