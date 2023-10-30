rm -rf rov/rov.urdf.xml
rm -rf rov.sdf
xacro rov/rov.xacro >> rov.urdf.xml
gz sdf -p rov.urdf.xml >> rov.sdf
cd ~/corews
rm -rf build install log
colcon build
