import subprocess as sp
import os
import time
def install_aws_cli():
	
	# Downloading AWS CLI V2
	print("Downloading aws cli v2...")
	a,b=sp.getstatusoutput("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip'")
	if a==0:
	  print("Successfully downloaded AWS CLI V2")
	else:
	  print("Please Try again to download")

	# Unziping the AWS CLI V2
	sp.getoutput("yum install unzip -y")
	sp.getoutput("unzip awscliv2.zip")

	# Installing the AWS CLI V2
	sp.getoutput("sudo ./aws/install")

	print("Now AWS CLI V2 is successfully configured")

def configure_aws_cli():
    # Configuring aws cli in local system with IAM credentials
    print("Enter the credentials for configuring aws cli\n")
    os.system("aws configure")
    print("Credentials successfully configured")

def create_key_pair():
    # Creating a new Key pair
    key_name=input("Enter the name for key pair: ")
    status,output=sp.getstatusoutput("aws ec2 create-key-pair --key-name {}".format(key_name))
    if status==0:
        print("Key-pair creation done successfully!!")
    else:
        print("Error: Either the key name is incorrect or aws cli not configred")
        create_key_pair()

def del_key_pair():
    # Deleting an existing Key pair
    key_name=input("Enter the name for key pair to be deleted: ")
    status,output=sp.getstatusoutput("aws ec2 delete-key-pair --key-name {}".format(key_name))
    if status==0:
        print("Key-pair deletion done successfully!!")
    else:
        print("Error: Either the key name is incorrect or key is already deleted")
        del_key_pair()

def create_security_group():
    # Creating a Security Group
    gname=input("Enter the security group name: ")
    des=input("Enter the description for the security group: ")
    status,output=sp.getstatusoutput("aws ec2 create-security-group  --group-name {}  --description '{}'".format(gname,des))
    if status==0:
        print("Security group creation done successfully!!")
    else:
        print("Error: The field name are provided empty. Please try again! ")
        create_security_group()

def del_security_group():
    # Deleting Security Group
    gname=input("Enter the group name to be deleted: ")
    status,output=sp.getstatusoutput("aws ec2 delete-security-group --group-name {}".format(gname))
    if status==0:
        print("Security group deletion done successfully!!")
    else:
        print("Error: The field name is provided empty. Please try again! ")
        del_security_group()

def launch_ec2_instance():
    # Launching an EC2 instance
    print("""Enter your choice:
            Press 1: For Amazon Linux AMI
            Press 2: For Red Hat Linux AMI
            Press 3: For Ubuntu Linux AMI""")
    ch=int(input())
    if ch==1:
        ami="ami-0e306788ff2473ccb"
    elif ch==2:
        ami="ami-052c08d70def0ac62"
    elif ch==3:
        ami="ami-0cda377a1b884a1bc"
    
    # Number of instances
    count=int(input("Enter the number of instances you want to launch"))
    print("""Press 1: To create a new key-pair
            Press 2: Use the existing key-pair""")
    ch=int(input())
    if ch==1:
        create_key_pair()
        key=input("Enter the key name")
    elif ch==2:
        key=input("Enter the key name")
    os.system("aws ec2 run-instances --image-id {} --instance-type t2.micro --count {} --key-name {}".format(ami,count,key))
    print("Launched Instance successfully!!")

if __name__=="__main__":
    os.system("clear")
    print("Welcome to the Python Integration Program with AWS CLI")
    while True:
        print("""
        Press 0: For exit
        Press 1: For downloading & installing AWS CLI V2
        Press 2: For configuring AWS CLI V2
        Press 3: For creating an AWS Key Pair
        Press 4: For deleting an AWS Key Pair
        Press 5: For creating a Security Group
        Press 6: For deleting a Security Group
        Press 7: Launch an EC2 instance""")
        ch=int(input())

        if ch==0:
            print("Thanks for using the program!!!")
            time.sleep(2)
            os.system("clear")
            exit()
        elif ch==1:
            install_aws_cli()
        elif ch==2:
            configure_aws_cli()
        elif ch==3:
           create_key_pair()
        elif ch==4:
            del_key_pair()
        elif ch==5:
            create_security_group()
        elif ch==6:
            del_security_group()
        elif ch==7:
            launch_ec2_instance()

        input("Press Enter to continue")
        os.system("clear")
