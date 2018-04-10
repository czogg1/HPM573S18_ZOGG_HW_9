import P3and5_ParameterClasses as P
import P3and5_MarkovModelClasses as MarkovCls
import P3and5_SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# Problem 3 (6 and 7)
# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NATURAL_HISTORY)

# simulate the cohort
simOutputs = cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve under the natural history of disease',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients under the natural history of disease',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# graph histogram of stroke counts
Figs.graph_histogram(
    data=simOutputs.get_stroke_counts(),
    title='Stroke counts of patients under the natural history of disease',
    x_label='Number of strokes',
    y_label='Counts',
    bin_width=1
)

# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs, 'Problem 3. Natural history:')


# Problem 5 (6 and 7)
# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAGULATION)

# simulate the cohort
simOutputs = cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve using anticoagulation therapy',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients using anticoagulation therapy',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# graph histogram of stroke counts
Figs.graph_histogram(
    data=simOutputs.get_stroke_counts(),
    title='Stroke counts of patients using anticoagulation therapy',
    x_label='Number of strokes',
    y_label='Counts',
    bin_width=1
)

# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs, 'Problem 5. Anticoagulation therapy post-stroke:')
