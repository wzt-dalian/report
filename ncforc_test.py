from lsreader import BinoutReader
from lsreader import BINOUT_DataType as bdt
from matplotlib import pyplot as plt
import os


#data preparation
cwd = os.getcwd()
data_path = os.path.join(cwd, "binout0000")
br = BinoutReader(data_path)
nid = 110
contact_id = 62
time =         br.get_data(bdt.BINOUT_NCFORC_X, cid=contact_id)
num_timestep = br.get_data(bdt.BINOUT_NCFORC_NUM_TIMESTEP, cid=contact_id)
mydict = {}
mydict["x-force"] = bdt.BINOUT_NCFORC_FORCE_X
mydict["y-force"] = bdt.BINOUT_NCFORC_FORCE_Y
mydict["z-force"] = bdt.BINOUT_NCFORC_FORCE_Z
scalar = [[0 for col in range(num_timestep)] for row in range(len(mydict))]

#extract the data from binoutreader->ncforc branch
for index, enum in enumerate(mydict.values()):
        scalar[index] = br.get_data(enum, id=nid,cid=contact_id)

#plot the curves using matplotlib
fig,ax1=plt.subplots()
for index, key in enumerate(mydict.keys()):
    lgd = key + f" of node-{nid}"
    ax1.plot(time,scalar[index],label=lgd)
ax1.legend()
ax1.grid()
ax1.set(xlabel='Time', ylabel="Force", title="BinoutReader->NcForc example")
plt.show()
