## @ingroup Analyses-Weights
# Weights_Transport.py
#
# Created:  Apr 2017, Matthew Clarke
# Modified: Oct 2017, T. MacDonald
#           Apr 2020, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Core import Data
from .Weights import Weights

# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

## @ingroup Analyses-Weights
class Weights_Transport(Weights):
    """ This is class that evaluates the weight of Transport class aircraft

    Assumptions:
        None

    Source:
        N/A

    Inputs:
        None

    Outputs:
        None

    Properties Used:
         N/A
    """

    def __defaults__(self):
        """This sets the default values and methods for the tube and wing
        aircraft weight analysis.

        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        N/A
        """
        self.tag = 'transport'

        self.vehicle = Data()
        self.settings = Data()
        self.settings.weight_reduction_factors = Data()

        # Reduction factors are proportional (.1 is a 10% weight reduction)
        self.settings.weight_reduction_factors.main_wing = 0.
        self.settings.weight_reduction_factors.fuselage = 0.
        self.settings.weight_reduction_factors.empennage = 0.  # applied to horizontal and vertical stabilizers

    def evaluate(self, method="SUAVE"):
        """Evaluate the weight analysis.

        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        results

        Properties Used:
        N/A
        """
        # unpack
        vehicle = self.vehicle
        results = SUAVE.Methods.Weights.Correlations.Common.empty_weight(vehicle, settings=self.settings,
                                                                         method_type=method)

        # storing weigth breakdown into vehicle
        vehicle.weight_breakdown = results

        # updating empty weight
        vehicle.mass_properties.operating_empty = results.empty

        # done!
        return results

    def finalize(self):
        """Finalize the weight analysis.

        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        N/A
        """
        self.mass_properties = self.vehicle.mass_properties

        return
