from interbotix_xs_modules.arm import InterbotixManipulatorXS
# This script closes and opens the gripper twice, changing the gripper pressure half way through
# roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=rx150 in a terminal
# Then change to this directory and type 'python gripper_control.py'

def main():
    arm = InterbotixManipulatorXS("rx150", "arm", "gripper")
    arm.gripper.close(2.0)
    arm.gripper.open(2.0)
    arm.gripper.set_pressure(1.0)
    arm.gripper.close(2.0)
    arm.gripper.open(2.0)

if __name__=='__main__':
    main()
