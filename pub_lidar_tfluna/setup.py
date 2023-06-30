from setuptools import setup

package_name = 'pub_lidar_tfluna'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='brayan',
    maintainer_email='brayan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
            'talker = pub_lidar_tfluna.publisher_function:main',
            'listener = pub_lidar_tfluna.subscriber_function:main',
            'test_node = pub_lidar_tfluna.example:main',
            'test_node1 = pub_lidar_tfluna.example1:main',
            'draw_circle = pub_lidar_tfluna.draw_circle:main',
            'pose_subscriber = pub_lidar_tfluna.pose_subscriber:main',
            'direc_publisher = pub_lidar_tfluna.direct_publisher:main',
            'direc_subscriber = pub_lidar_tfluna.direct_subscriber:main',
            'direc_brazo = pub_lidar_tfluna.direct_brazo:main'
        ],
    },
)
