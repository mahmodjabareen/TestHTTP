import os
import uuid
uuid = str(uuid.uuid4())
arr =["{}.txt".format(uuid)]
if not os.path.exists("output"):
  os.mkdir("output")
for i in arr:
  f = open("output/{}".format(i), "a")
  f.write("Now the file has more content! {}".format(i))
  f.close()
