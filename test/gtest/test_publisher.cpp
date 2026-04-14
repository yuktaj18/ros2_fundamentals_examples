/***
 * Testcases for unit testing of publisher node
 */

 #include <gtest/gtest.h>
 #include "rclcpp/rclcpp.hpp"
 #include "std_msgs/msg/string.hpp"

class MinimalCpp_Publisher;

#define TESTING_EXCLUDE_MAIN
#include "../../src/cpp_minimal_publisher.cpp"

class TestMinimalPublisher : public ::testing::Test
{
  protected:
    void SetUp() override
    {
      rclcpp::init(0,nullptr);

      node = std::make_shared<MinimalCpp_Publisher>();

    }

    void TearDown() override
    {
      node.reset();
      rclcpp::shutdown();

    }
std::shared_ptr<MinimalCpp_Publisher> node;

};


/*
Test node creation
*/

TEST_F(TestMinimalPublisher,TestNodeCreation)
{
  EXPECT_EQ(std::string(node->get_name()),std::string("minimal_cpp_publsiher"));

  auto pub_endpoints = node->get_publishers_info_by_topic("/cpp_example_topic");

  EXPECT_EQ(pub_endpoints.size(), 1u);


}

/****
 * Test msg content
 */

 TEST_F(TestMinimalPublisher,TestMessageContent)
 {
    std::shared_ptr<std_msgs::msg::String> received_msg;

    auto subscription = node->create_subscription<std_msgs::msg::String>(
      "/cpp_example_topic",10,
      [&received_msg](const std_msgs::msg::String::SharedPtr msg)
      {
        received_msg = std::make_shared<std_msgs::msg::String>(*msg);
      }
    );

    node->timerCallback();
    rclcpp::spin_some(node);

    EXPECT_EQ(received_msg->data.substr(0,12),"Hello World!");

 }


 int main(int argc, char** argv)
 {

  testing::InitGoogleTest(&argc, argv);



  return RUN_ALL_TESTS();
 }

