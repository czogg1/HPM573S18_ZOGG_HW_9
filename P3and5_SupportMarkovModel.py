import P3and5_InputData as Settings
import scr.FormatFunctions as F


def print_outcomes(simOutput, therapy_name):
    """ prints the outcomes of a simulated cohort
    :param simOutput: output of a simulated cohort
    :param therapy_name: the name of the selected therapy
    """
    # mean and confidence interval text of patient survival time
    survival_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_survival_times().get_mean(),
        interval=simOutput.get_sumStat_survival_times().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # mean and confidence interval text of patient stroke count
    stroke_count_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_stroke_counts().get_mean(),
        interval=simOutput.get_sumStat_stroke_counts().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # print outcomes
    print(therapy_name)
    print("  Estimate of the mean survival time in years and {:.{prec}%}CI:".format(1 - Settings.ALPHA, prec=0),
          survival_mean_CI_text)
    print("  Estimate of the mean stroke count and {:.{prec}%}CI:".format(1 - Settings.ALPHA, prec=0),
          stroke_count_CI_text)
    print("")
