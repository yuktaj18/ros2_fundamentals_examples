#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class MinimalCpp_Publisher : public rclcpp::Node
{
public :
  MinimalCpp_Publisher():Node("minimal_cpp_publsiher"),count_(0)
   {

    publisher_ = create_publisher<std_msgs::msg::String>(
        "/cpp_example_topic",10);

    timer_ = create_wall_timer(500ms,
        std::bind(&MinimalCpp_Publisher::timerCallback,this));
    RCLCPP_INFO(get_logger(),"Publishing at 2 Hz");
   }
void timerCallback()
{
    auto message = std_msgs::msg::String();
    message.data = "Hello World!" + std::to_string(count_++);
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    publisher_ ->publish(message);
}
private:
size_t count_;
rclcpp::Publisher<std_msgs::msg::String>::SharedPtr
    publisher_;

rclcpp::TimerBase::SharedPtr timer_;

};

#ifndef TESTING_EXCLUDE_MAIN

int main(int argc, char * argv[])
{
    rclcpp::init(argc,argv);

    auto minimal_cpp_publisher_node = std::make_shared<MinimalCpp_Publisher>();
    rclcpp::spin(minimal_cpp_publisher_node);

    rclcpp::shutdown();

    return 0;
}

#endif
