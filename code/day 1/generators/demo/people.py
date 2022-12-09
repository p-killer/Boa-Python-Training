import random
import time

names = ['Murthy', 'Kiran', 'Arun', 'Sita', 'Raj', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

'''
t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()     
print("Time taken  with list :{} secs".format(t2-t1))
'''

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()
print("Time taken with Generator :{} secs ".format(t2-t1))

'''
#print ('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print ('Took {} Seconds'.format(t2-t1))

# found memory report 
# with list  Before 15mb and after 319mb
# with generator  Before is 15mb and after 15.6mb   so excellent memory utilization

'''







