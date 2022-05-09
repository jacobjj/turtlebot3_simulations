#!/usr/bin/env python3
''' Example of a node with to set pose.
'''

from turtlebot3_actions.action import Tb3start
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

class setPoseActionClient(Node):
    ''' An example node that shows how to launch a node for setting pose.
    '''
    def __init__(self):
        super().__init__('set_pose_node')
        self._action_client = ActionClient(self, Tb3start, '/tb3position')

    
    def send_goal(self, x, y=0.0, z=0.0):
        '''
        Sends the message to the client
        :param x: x-coordinate of the robot
        :param y: y-coordinate of the robot
        :param z: z-coordinate of the robot
        '''
        goal_msg = Tb3start.Goal()
        goal_msg.start.x = x
        goal_msg.start.y = y
        goal_msg.start.z = z

        self._action_client.wait_for_server()

        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    action_client = setPoseActionClient()
    
    future = action_client.send_goal(0.5)

    rclpy.spin_until_future_complete(action_client, future)


if __name__=="__main__":
    main()