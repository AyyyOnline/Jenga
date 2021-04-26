from interbotix_xs_modules.arm import InterbotixManipulatorXS
# This script makes the end-effector go to a specific pose by defining the pose components
# roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=rx150 in a terminal
# Then change to this directory and type 'python ee_pose_components.py'

def main():
    bot = InterbotixManipulatorXS("rx150", "arm", "gripper")
    bot.arm.go_to_home_pose()
    bot.arm.set_ee_pose_components(x=0.2, y=0.1, z=0.2, roll=1.0, pitch=1.5)
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()

if __name__=='__main__':
    main()
