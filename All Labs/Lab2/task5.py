task5 = input("Enter any String:")
def rreverse(task5):
    if task5 == "":
        return ""
    else:
        return rreverse(task5[1:])+task5[0]
print("Answer: ",rreverse(task5))
