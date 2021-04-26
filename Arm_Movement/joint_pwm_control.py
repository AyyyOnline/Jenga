from interbotix_xs_modules.arm import InterbotixManipulatorXS

# This script commands currents [mA] to the arm joints
# roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=rx150 in a terminal
# Then change to this directory and type 'python joint_current_control.py'

def main():
    joint_pwms = [0, 100 , 100, 25, 0]
    bot = InterbotixManipulatorXS("rx150", "arm", "gripper")
    bot.dxl.robot_set_operating_modes("group", "arm", "pwm")
    bot.dxl.robot_write_commands("arm", joint_pwms)

if __name__=='__main__':
    main()
