def roomallocations(a,b):
    allocation_room = str()
    allocation_room_name = str()
    if labsystems[a][b][0] == 'Free':
        allocation_room = b
        allocation_room_name = a
        labsystems[a][b][0] = 'Allocated'
    else:
            print("sorry,it is already allocated") 
    return [allocation_room, allocation_room_name]

        
if __name__ == "__main__":
    labsystems = {'MCA Lab':{'1':['Free','Good'],'2':['Allocated','Repair'],'3':['Free','Good'] }, 'Cisco Lab':{'1':['Free','Good'],'2':['Free','Good'],'3':['Allocated','Repair']}}
    students = {'Raja': 701, 'Teja': 702, 'Suraj': 770, 'Manikant': 800}
    l=len(students)  
    for i in range(l):
          name=raw_input()
          a=raw_input()
          b=raw_input()
          allocations = roomallocations(a,b)
          print(name + " - " + str(students[name]) + " - " + str(allocations[1]) + " - " + str(allocations[0]))