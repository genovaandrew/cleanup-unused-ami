import boto3
import argparse

REGION_NAME = "us-east-1"

ec2_client = boto3.client("ec2", region_name=REGION_NAME)


def get_all_owner_amis() -> set:
    """returns set of user owned AMIs"""
    owner_amis = ec2_client.describe_images(Owners=["self"])
    all_amis = set()

    for image in owner_amis["Images"]:
        all_amis.add(image["ImageId"])

    return all_amis


def get_used_amis() -> set:
    """returns set of used AMIs"""
    EC2_RESOURCE = boto3.resource("ec2", region_name=REGION_NAME)
    instances = EC2_RESOURCE.instances.all()

    instances_set = set(instances)
    amis_used = set()

    for instance in instances_set:
        amis_used.add(instance.image.id)

    return amis_used


if __name__ == "__main__":
    flags = argparse.ArgumentParser()
    flags.add_argument(
        "-f", "--force", default=False, action="store_true", help="actually delete AMIs"
    )
    args = flags.parse_args()

    used_amis = get_used_amis()
    all_amis = get_all_owner_amis()

    unused_amis = all_amis - used_amis

    print("Unused AMIs:")
    for ami in unused_amis:
        print(ami)
        if args.force is True:
            ec2_client.deregister_image(ImageId=ami)
