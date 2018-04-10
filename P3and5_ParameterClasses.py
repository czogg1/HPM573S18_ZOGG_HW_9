from enum import Enum
import numpy as np
import scipy.stats as stat
import math as math
import P3and5_InputData as Data
import scr.MarkovClasses as MarkovCls
import scr.RandomVariantGenerators as Random
import scr.ProbDistParEst as Est


class HealthStats(Enum):
    """ health states of patients """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    STROKE_DEAD = 3


class Therapies(Enum):
    """ natural history versus anticoagulation """
    NATURAL_HISTORY = 0
    ANTICOAGULATION = 1


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL

        # transition probability matrix of the selected therapy
        self._prob_matrix = []
        # treatment relative risk
        self._treatmentRR = 0

        # calculate transition probabilities between states
        self._prob_matrix = calculate_prob_matrix()

        # update the transition probability matrix if anticoagulation therapy is being used
        if self._therapy == Therapies.ANTICOAGULATION:
            # calculate transition probability matrix for the combination therapy
            self._prob_matrix = calculate_prob_matrix_combo()

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]


def calculate_prob_matrix():
    """ :returns transition probability matrix for states under natural history """

    prob_matrix = Data.TRANS_MATRIX
    return prob_matrix


def calculate_prob_matrix_combo():
    """:returns transition probability matrix for status under anticoagulation therapy """

    prob_matrix = Data.TRANS_MATRIX_ANTICOAG
    return prob_matrix
