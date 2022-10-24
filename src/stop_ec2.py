
import boto3  # pip install boto3

def stop_ec2():
    """
    boto3を使って全てのリージョンで起動しているEC2インスタンスを確認し、
    EC2のタグ「AutoStop」の値が「true」の場合のみ停止させる。
    """

    # 全リージョンを取得
    client = boto3.client('ec2')
    regions = client.describe_regions()['Regions']

    # 各リージョン毎に繰り返し
    for region in regions:
        client = boto3.client('ec2', region_name=region['RegionName'])

        # 以下の条件を全て満たすインスタンス一覧を取得
        response = client.describe_instances(Filters=[
            {   # EC2が稼働中
                'Name': 'instance-state-name',
                'Values': ['running'],
            },
            {   # EC2のタグ「AutoStop」の値が「true」
                'Name': 'tag:AutoStop',
                'Values': ['true'],
            },
        ])

        # 一致なしの場合はスキップ
        if len(response['Reservations']) <= 0:
            continue

        # 一致ありの場合はインスタンスID一覧を停止
        instance_ids = []
        for instance_dic in response['Reservations']:
            instance_ids.append(instance_dic['Instances'][0]['InstanceId'])
        response = client.stop_instances(InstanceIds=instance_ids)

        print('[+] stop ec2 on region "%s"' % region['RegionName'])
        print(response)

stop_ec2()
