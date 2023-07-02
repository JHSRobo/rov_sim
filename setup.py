from setuptools import setup

package_name = 'rov_sim'

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
    maintainer='James Randall',
    maintainer_email='randallj24@student.jhs.net',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'depth_sensor = rov_sim.depth_sensor:main',
            'gpio_control = rov_sim.gpio_control:main'

        ],
    },
)