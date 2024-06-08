# file_path = "C:/Users/hiva laptop/Desktop/project/lib_azadegan.txt"

# with open(file_path, "r") as file:
#     lineList = file.readlines()

# newName = "Alch"
# name = "alchemist"

# # Initialize a flag to check if replacement happened
# replacement_done = False

# # Modify the specific line if it matches the criteria
# for i in range(len(lineList)):
#     firstline = lineList[i].find("_")
    
#     if firstline != -1 and name == lineList[i][0:firstline]:
#         print("done")
#         lineList[i] = newName + lineList[i][firstline:]
#         replacement_done = True
#         break

# # Write all lines back to the file, including the modified line
# with open(file_path, "w") as file:
#     file.writelines(lineList)

# if not replacement_done:
#     print("No matching line found.")
