##################### List ############################

"""list_of_num = []

list_of_num.append(1)
list_of_num.append(2)
list_of_num.append("Madhav")

print(list_of_num)"""

list_of_cloud = ["AWS", "Azure", "Gcp", "oracle"]
list_of_env = ["dev", "test", "prod"]

"""print(list_of_cloud[3])"""
"print(list_of_env[2])"

## I want to do something in test env
"""if list_of_env[1] == 'test':
    print("test environment")"""


## If want to iterate list_of_cloud values/content or List iteration

print(range(10))

"""for i in range(10):
    print("Boom")"""

"""for cloud in list_of_cloud:
    print(cloud)"""

for cloud in list_of_cloud:
    if cloud == "AWS":
        print("AWS is the best cloud")


################ Dictionary #############################

dic_of_cloud = {
    "AWS": "Amazon web services",
    "Azure": "Microsoft Azure",
    "GCP": "Google cloud platform"
}

# Access or getting the values from the dictionary using key

print(dic_of_cloud['AWS'])
print(dic_of_cloud.get('Azure', "Not found"))
print(dic_of_cloud.get('Linode', "Not found"))

# Update the dictionary or adding

dic_of_cloud.update({"Linode":"linode cloud"})

print(list_of_cloud)




