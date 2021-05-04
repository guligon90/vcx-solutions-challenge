# Base imports
from typing import Dict, List, Union, Optional

# Third-party imports
import matplotlib.pyplot as plotter

# Project imports
from src.graphics.common import build_tc_plot_file_path
from src.time_complexity.common import Number, TIME_COMPLEXITIES, TIME_RATIO_SCALE_FACTOR


def plot_time_ratios(
    problem_size: int,
    time_ratios: Dict[str, Union[str, List[Number]]],
    plot_title: str = "Execution time ratios' comparison.",
    show_plot: bool = False,
) -> None:
    """Function that receives the time rations and plot then in a x-y graph."""
    img_file_path: Optional[str] = build_tc_plot_file_path(
        str(time_ratios.get('data_struct_name')),
        str(time_ratios.get('target_name')),
        problem_size
    )

    n_values: List[int] = list(range(1, problem_size + 1))

    # Creating plotting handlers
    figure_handler, axis_handler = plotter.subplots()

    for func_name, ratios in time_ratios.items():
        # Plotting the rations as a function of n
        if isinstance(ratios, list):
            scaled_ratios: List[Number] = [
                ratio * TIME_RATIO_SCALE_FACTOR for ratio in ratios
            ] if TIME_RATIO_SCALE_FACTOR else ratios

            axis_handler.plot(
                n_values,       # X axis
                scaled_ratios,  # Y axis
                TIME_COMPLEXITIES.get(func_name).get('plot_pattern'),
                label=TIME_COMPLEXITIES.get(func_name).get('plot_label')
            )

    # Setting axis labels
    axis_handler.set(
        xlabel=r"Problem size - $n$",
        ylabel=r"Ratio - $T_{meas}(n)/T_{theory}(n)$",
        title=plot_title
    )

    # Creating legend
    axis_handler.legend(
        loc='upper right',
        shadow=True,
    )

    plotter.ylim([0.0, 1.0])

    # Setting plot grid
    axis_handler.grid()

    figure_handler.savefig(img_file_path)

    print(f'Plot image succesfully generated in {img_file_path}')

    if show_plot:
        plotter.show()
