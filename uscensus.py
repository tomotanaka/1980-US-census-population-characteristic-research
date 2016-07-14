
import pymongo
import matplotlib.pyplot as plt
import numpy as np
import pdb
import each_age
import sys
import codecs
def cp65001(name):
    if name.lower() == 'cp65001':
        return codecs.lookup('utf-8')
codecs.register(cp65001)

c = pymongo.MongoClient("localhost", 47017)
db=c.uscensus
coll=db.pop
#print coll.find_one({"f1" : "" })
c_0=coll.find() # read coll into cursor
#c0[0] # show 1st row
age=[1,2,4,5,6,9,13,14,15,16,17,18,19,20,21,24,29,34,44,54,59,61,64,74,84,85]
us_male=[]; us_female=[]; us_t_age=[];us_m_age=[]; us_f_age=[];str_state=[]
for c0 in c_0:
	stf=c0['f1'][0:5];geo_level=c0['f1'][9:11]; geo_State=int(c0['f1'][31:33]); FIPS_State=int(c0['f1'][33:35])
	str1=c0['f1'][0:1600]
	#print str1
	#pdb.set_trace()
	if geo_level=='04':# and stf=='STF1A':  #FIPS_State>0 and geo_State>0:
		c0_str=str(c0['f1'])
		state=c0_str[144:204].strip()
		print state, FIPS_State
		#print c0_str
		#pdb.set_trace()
		state_male, state_female, t_age, m_age, f_age=each_age.ages(c0_str)
		us_male.append(state_male); us_female.append(state_female)
		us_t_age.append(t_age); us_m_age.append(m_age); us_f_age.append(f_age); str_state.append(state)
#	++++++++++++++++++++++++++++++++++++++++++++

sum_us_total=np.sum(np.array(us_t_age))
sum_us_m_age=np.sum(us_m_age, axis=0); sum_us_f_age=np.sum(us_f_age, axis=0)
ab = np.zeros(len(str_state), dtype=[('var1', 'S25'), ('var2', int)])
ab['var1'] = str_state
ab['var2'] = np.sum(us_t_age,axis=1)
pdb.set_trace()

np.savetxt('state_pop.dat', ab, fmt="%25s %12i")
plt.plot(age, m_age)
plt.show()



