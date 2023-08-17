from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hobot_audio',
            executable='hobot_audio',
            output='screen',
            arguments=['--ros-args', '--log-level', 'error']
        ),
        Node(
            package='gpt_node',
            executable='gpt_node',
            output='screen',
            parameters=[
                {"gpt_topic_sub": "/audio_asr"},
                {"gpt_topic_pub": "/tts_text"}
            ],
            arguments=['--ros-args', '--log-level', 'error']
        ),
        Node(
            package='hobot_tts',
            executable='hobot_tts',
            output='screen',
            arguments=['--ros-args', '--log-level', 'error']
        )
    ])
