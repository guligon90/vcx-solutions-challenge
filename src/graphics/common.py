# Base import
from datetime import datetime
from typing import Callable, Optional
import os


PROJECT_ABS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build_tc_plot_file_path(ds_name: str, target_name: str, problem_size: int) -> Optional[str]:
    supported_data_structs = ['stack', 'queue']

    if ds_name.lower() not in supported_data_structs:
        raise NotImplementedError(
            f"The data structure {ds_name} is not supported. Choices are {', '.join(supported_data_structs)}"
        )

    plots_path: Callable[[str, ], str] = lambda _ds_name: os.path.join(
        f'{PROJECT_ABS_PATH}/time_complexity',
        f'{_ds_name}/plots'
    )
    timestamp: str = datetime.strftime(datetime.now(), '%d-%m-%Y_%H-%M-%S')

    return f'{plots_path(ds_name)}/tc_plot_{ds_name}_{target_name}_size_{problem_size}_{timestamp}.png'
