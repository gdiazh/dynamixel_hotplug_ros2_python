#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gives dictionary specifying how to link topics together and do the input/output shaping

@author: Elian NEPPEL
@laboratory: Moonshot, Space Robotic Lab, Tohoku University
"""

import numpy as np


# {Higher level pub  : Subscriber to the u2d2_dyna_controller}
angle_map = {
    f"read_joint{1}_{1}": f"angle_port_{0}_mot_{1}",
    f"read_joint{1}_{2}": f"angle_port_{0}_mot_{2}",
    f"read_joint{1}_{3}": f"angle_port_{0}_mot_{3}",
    f"read_joint{1}_{4}": f"angle_port_{0}_mot_{4}",
    f"read_joint{1}_{5}": f"angle_port_{0}_mot_{5}",
    f"read_joint{1}_{6}": f"angle_port_{0}_mot_{6}",
    f"read_joint{1}_{7}": f"angle_port_{0}_mot_{7}",
}

# {Higher level sub  : Publisher to the u2d2_dyna_controller}
set_map = {
    f"ang_joint{1}_{1}_set": f"set_port_{0}_mot_{1}",
    f"ang_joint{1}_{2}_set": f"set_port_{0}_mot_{2}",
    f"ang_joint{1}_{3}_set": f"set_port_{0}_mot_{3}",
    f"ang_joint{1}_{4}_set": f"set_port_{0}_mot_{4}",
    f"ang_joint{1}_{5}_set": f"set_port_{0}_mot_{5}",
    f"ang_joint{1}_{6}_set": f"set_port_{0}_mot_{6}",
    f"ang_joint{1}_{7}_set": f"set_port_{0}_mot_{7}",
}

# {Higher level sub  : input shaping funciton, applied very first on incoming angles}
# here I am applying a saturation on the angles
input_shaping_map = {
    f"ang_joint{1}_{1}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{2}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{3}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{4}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{5}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{6}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{7}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
}

# {Higher level sub  : Set a offset on the angles (before the gain is applied)}
offset_map = {
    f"ang_joint{1}_{1}_set": -0.4672,
    f"ang_joint{1}_{2}_set": 3.2152,
    f"ang_joint{1}_{3}_set": 2.71,
    f"ang_joint{1}_{4}_set": 0.0130,
    f"ang_joint{1}_{5}_set": -0.8201,
    f"ang_joint{1}_{6}_set": 3.9701,
    f"ang_joint{1}_{7}_set": 3.1063,
}

# {Higher level sub  : Set a gain on the angles (can be negative to flip the motor)}
gain_map = {
    f"ang_joint{1}_{1}_set": 1,
    f"ang_joint{1}_{2}_set": 1,
    f"ang_joint{1}_{3}_set": 1,
    f"ang_joint{1}_{4}_set": 1,
    f"ang_joint{1}_{5}_set": 1,
    f"ang_joint{1}_{6}_set": 1,
    f"ang_joint{1}_{7}_set": 1,
}

# {Higher level sub  : output shaping function, applied on outgoing angles}
output_shaping_map = {
    f"ang_joint{1}_{1}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{2}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{3}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{4}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{5}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{6}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
    f"ang_joint{1}_{7}_set": lambda x: min(max(x, -2*np.pi), 2*np.pi),
}
