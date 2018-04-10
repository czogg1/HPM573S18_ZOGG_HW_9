# simulation settings
POP_SIZE = 2000                         # cohort population size
SIM_LENGTH = 50                         # length of simulation (years)
ALPHA = 0.05                            # significance level for calculating confidence intervals
DELTA_T = 1                             # years

# transition matrix 1
TRANS_MATRIX = [
    [0.75,  0.15,  0.00,  0.10],        # Well
    [0.00,  0.00,  1.00,  0.00],        # Stroke
    [0.00,  0.25,  0.55,  0.20],        # Post-stroke
    [0.00,  0.00,  0.00,  1.00],        # Stroke dead
    ]

# transition matrix 2
TRANS_MATRIX_ANTICOAG = [
    [0.75,  0.15,  0.00,  0.10],        # Well
    [0.00,  0.00,  1.00,  0.00],        # Stroke
    [0.00,  0.16,  0.70,  0.14],        # Post-stroke
    [0.00,  0.00,  0.00,  1.00],        # Stroke dead
    ]
