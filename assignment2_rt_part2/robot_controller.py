import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        # Publisher for controlling the robot
        self.pub_cmd_vel = self.create_publisher(Twist, '/cmd_vel', 10)

    def control_robot(self):
        """Control the robot's movement based on user input."""
        # Get linear velocity with range validation
        while True:
            try:
                linear_x = float(input("Enter the linear velocity (between -5 and 5): "))
                if -5 <= linear_x <= 5:
                    break
                else:
                    print("Invalid input. Linear velocity must be between -5 and 5.")
            except ValueError:
                print("Invalid input. Linear velocity must be a number.")

        # Get angular velocity with range validation
        while True:
            try:
                angular_z = float(input("Enter the angular velocity (between -5 and 5): "))
                if -5 <= angular_z <= 5:
                    break
                else:
                    print("Invalid input. Angular velocity must be between -5 and 5.")
            except ValueError:
                print("Invalid input. Angular velocity must be a number.")

        # Create a Twist message and populate with user input
        robot_vel = Twist()
        robot_vel.linear.x = linear_x
        robot_vel.angular.z = angular_z

        # Publish to the cmd_vel topic to move the robot
        self.pub_cmd_vel.publish(robot_vel)

        # Stop the robot after 1 second
        self.get_logger().info("Moving robot... (stopping after 1 second)")
        time.sleep(1) # Sleep for 1 second
        robot_vel.linear.x = 0.0
        robot_vel.angular.z = 0.0
        self.pub_cmd_vel.publish(robot_vel)
        self.get_logger().info("Robot stopped.")

def main(args=None):
    rclpy.init(args=args)

    robot_controller = RobotController()

    # Main loop to control the robot
    try:
        while rclpy.ok():
            robot_controller.control_robot()
    except KeyboardInterrupt:
        pass  

    # Clean up after node shutdown
    robot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()