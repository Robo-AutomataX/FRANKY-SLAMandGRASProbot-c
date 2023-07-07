from setuptools import setup

package_name = 'robot_programs'

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
    maintainer_email='brayanelgamesa@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_brazo = robot_programs.publisher_brazo:main',
            'publisher_keyboard = robot_programs.publisher_keyboard:main',
            'subscriber_keyboard = robot_programs.subscriber_keyboard:main',
            'publisher_tfluna = robot_programs.publisher_tfluna:main',
            'subscriber_tfluna = robot_programs.subscriber_tfluna:main'
        ],
    },
)
