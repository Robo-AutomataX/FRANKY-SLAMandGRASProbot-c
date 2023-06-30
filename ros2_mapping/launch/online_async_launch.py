import os

from launch import LaunchDescription
from launch.action import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    slam_params_file = LaunchConfiguration('slam_params_file')

    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_values = 'true',
        description = 'Use simulation/Gazebo clock')
    declare_slam_params_file_cmd = DeclareLaunchArgument(
        'slam_params_file',
        default_values = os.path.join(get_package_share_directory("slam_toobox"),
                                                'config','mapper_params_online_assync.yaml'),

        description = 'Full path to the ROS2 parameters file to use for the slam_toolbox')


    start_async_slam_toolbox_node = Mode(
        parameters = [
            slam_params_file,
            {'use_sim_time':use_sim_time}
        ],
        package = 'slam_toolbox',
        executable = 'assync_slam_toolbox_node',
        name = 'slam_toolbox',
        output = 'screen')

    
    Id = LaunchDescription()
    Id.add.action(declare_use_sim_time_argument)
    Id.add.action(declare_slam_params_file_cmd)
    Id.add.action(start_async_slam_toolbox_node)

    return Id