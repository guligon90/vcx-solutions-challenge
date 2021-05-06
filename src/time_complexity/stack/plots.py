# Project imports
from src.graphics.plotting import plot_time_ratios
from src.time_complexity.stack.time_ratio import eval_push_time_ratios


def generate_push_function_tc_plot():
    problem_size = 10000

    time_ratios = eval_push_time_ratios(problem_size)

    plot_time_ratios(
        problem_size,
        time_ratios,
        plot_title=f'Time ratios for Stack.push w/ problem_size={problem_size}'
    )
