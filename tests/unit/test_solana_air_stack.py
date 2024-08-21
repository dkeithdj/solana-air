import aws_cdk as core
import aws_cdk.assertions as assertions

from solana_air.solana_air_stack import SolanaAirStack

# example tests. To run these tests, uncomment this file along with the example
# resource in solana_air/solana_air_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SolanaAirStack(app, "solana-air")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
