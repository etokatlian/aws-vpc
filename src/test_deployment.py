from src.ec2.vpc import VPC
from src.client_locator import EC2Client


def main():
	# Create VPC
	ec2_client = EC2Client().get_client()
	vpc = VPC(ec2_client)

	vpc_response = vpc.create_vpc()

	print('VPC created:' + str(vpc_response))

	# Add name tag to VPC
	vpc_name = 'Boto3-VPC'
	vpc_id = vpc_response['Vpc']['VpcId']
	vpc.add_name_tag(vpc_id, vpc_name)

	print('Added ' + vpc_name + ' to ' + vpc_id)

	# Create an IGW
	igw_response = vpc.create_internet_gateway()

	igw_id = igw_response['InternetGateway']['InternetGatewayId']
	vpc.attach_igw_to_vpc(vpc_id, igw_id)


if __name__ == '__main__':
	main()
