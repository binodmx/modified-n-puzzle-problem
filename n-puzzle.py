
start_conf_file_name = "Sample_Start_Configuration.txt"
goal_conf_file_name = "Sample_Goal_Configuration.txt"

start_configuration = []
goal_configuration = []

fo = open(start_conf_file_name, "r")
lines = fo.readlines()
for line in lines:
    start_configuration.append(line.strip().split())
fo.close()

fo = open(goal_conf_file_name, "r")
lines = fo.readlines()
for line in lines:
    goal_configuration.append(line.strip().split())
fo.close()

print(start_configuration)
print(goal_configuration)
