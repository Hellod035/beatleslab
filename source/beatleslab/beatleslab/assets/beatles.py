# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import isaaclab.sim as sim_utils
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.actuators import ImplicitActuatorCfg
from beatleslab.assets import ISAAC_ASSET_DIR
import math

BEATLES_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/beatles/beatles_usd/beatles.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=4
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.6),
        joint_pos={
            "HipR": -0.8,
            "KneeR": math.pi / 2,
            "HubR": 0.0,
            "HipL": 0.8,
            "KneeL": -math.pi / 2,
            "HubL": 0.0
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "Hip": ImplicitActuatorCfg(
            joint_names_expr=[".*Hip.*"],
            effort_limit=25.0,
            velocity_limit=20,
            stiffness={".*": 10.0},
            damping={".*": 1.5},
            armature={".*": 0.01},
        ),
        "Knee": ImplicitActuatorCfg(
            joint_names_expr=[".*Knee.*"],
            effort_limit=25.0,
            velocity_limit=20,
            stiffness={".*": 15.0},
            damping={".*": 1.5},
            armature={".*": 0.01},
        ),
        "Hub": ImplicitActuatorCfg(
            joint_names_expr=[".*Hub.*"],
            effort_limit=25.0,
            velocity_limit=20,
            stiffness={".*": 0.0},
            damping={".*": 0.5},
            armature={".*": 0.01},
        ),
    },
)
