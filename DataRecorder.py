import rospy
from hunter_msgs.msg import HunterStatus

def callback(data):
    """Callback function to handle incoming data from the topic."""
    with open("hunter_status_log.txt", "a") as file:
        # Write the linear velocity and steering angle to the file
        file.write(f"Linear Velocity: {data.linear_velocity}, Steering Angle: {data.steering_angle}\n")

def listener():
    """Initialize ROS node and subscribe to the topic."""
    rospy.init_node('hunter_status_listener', anonymous=True)
    rospy.Subscriber("hunter_msgs/HunterStatus", HunterStatus, callback)

    # Keep the node running
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
