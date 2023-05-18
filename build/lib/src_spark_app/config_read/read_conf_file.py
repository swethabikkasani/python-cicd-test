def read_config_file(conf_path):
    aws_vars = {}

    with open(conf_path, "r") as aws_conf:
        for line in aws_conf:
            name, var = line.partition("=")[::2]
            aws_vars[name.strip()] = var

    if str(aws_vars["assumeRole"]).strip() == "false":
        raise Exception("Application not allowed to use AWS credentials assumeRole is false")

    aws_access_key = str(aws_vars["awsAccessKeyId"]).strip().replace('"', '')
    aws_secret_access_key = str(aws_vars["awsSecretAccessKey"]).strip().replace('"', '')
    role_arn = str(aws_vars["assumeRoleArn"]).strip().replace('"', '')

    return aws_access_key, role_arn
