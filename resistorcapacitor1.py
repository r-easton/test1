"""RC class starter with simplistic test code.
TPRG 2131 Fall 2024 Test 1
Novemebr, 2024
Ryleigh Easton <ryleigh.easton@dcmail.ca>

TPRG2131-01 Section 202443.13884
This program is strickly my own work. Any material beyond course learning materials that is taken from
the web or other sources is properly cited, givingcredit to the original author(s).
"""

class ResistorCapacitor (object):
    """Model a resistor-capacitor network"""
    def __init__(self, resistance, capacitance, initial=0.0):
        return

    #
    # Mutator methods
    #
    def set_voltage(self, voltage):
        """Set the voltage."""
        return


## Test code (place at bottom of the file)
if __name__ == "__main__":
    print("Self testing...")
    rc1 = ResistorCapacitor(1000.0, 1.0e-6)
    rc1.set_voltage(5.0)
    rc2 = ResistorCapacitor(10.0e3, 22.0e-6, 12.0)
    print("rc1:")
    print(rc1.resistance, rc1.capacitance, rc1.initial_voltage)
    for vtime in range(0, 6):
        stime = vtime * 0.5e-3
        print(stime, rc1.voltage(stime))
    print("rc2:")
    print(rc2.resistance, rc2.capacitance, rc2.initial_voltage)
    for vtime in range(0, 6):
        stime = vtime * 150.0e-3
        print(stime, rc2.voltage(stime))
# done
