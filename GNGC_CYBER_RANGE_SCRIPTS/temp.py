import challenge_info
import admin_config

print("This is the 'get_challanges_settings' command")
print("")
print(str(challenge_info.get_challenge_settings("Generic Travel")))
print("")
print("This is the 'get_category' command")
print("")
print(str(challenge_info.get_category()))
print("This is the 'get_challanges' command")
print("")
print(str(challenge_info.get_challenges("Basic Command Line")))
print("")
print("The following commands come from the Admin_Config.py file")
print("")
print("This command updates the admin_config.json file to include all the challanges and pops in the default data")
print("")
print(str(admin_config.update_challanges()))
print("")
print("This command Updates the data, the change will also be printed using the get_data command")
print("")
print("Before Change ", admin_config.get_data("How Helpful"))
admin_config.update_data("How Helpful", "Enabled", "True")
print("After Change ", admin_config.get_data("How Helpful"))

'''
x = 1
while x == 1:
    challengeName = input('Enter Challenge Catagory: ')
    print(str(challenge_info.get_challenges(challengeName)))
'''