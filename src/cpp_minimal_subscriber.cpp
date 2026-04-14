#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using std::placeholders::_1;

class MinimalSubscriberCpp : public rclcpp::Node

{

  public :
  MinimalSubscriberCpp () : Node("cpp_minimal_subscriber")
  {
    subscriber_ = create_subscription<std_msgs::msg::String>
    (
      "/cpp_example_topic",
      10,
      std::bind(
        &MinimalSubscriberCpp::topicCallback,
        this,
        _1

      )
    );

  }

  void topicCallback(const std_msgs::msg::String & msg) const
  {
    RCLCPP_INFO_STREAM(get_logger(),"I heard :"<< msg.data.c_str());
  }
private :
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscriber_;


};


int main(int argc, char* argv[])
{
  rclcpp::init(argc,argv);
  auto minimal_cpp_subscriber_node = std::make_shared<MinimalSubscriberCpp>();
  rclcpp::spin(minimal_cpp_subscriber_node);
  rclcpp::shutdown();

  return 0;
}