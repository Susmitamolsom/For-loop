birds=["Belle","Coco","Juniper","Lilly","Snow"]
i=False
for iter in birds:
    print(iter)
    if i and iter in "Snow":
        break
else:
    print("No birds left")