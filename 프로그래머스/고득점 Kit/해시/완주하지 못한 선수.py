def solution(participant, completion):
    
    completion_name = dict()
    
    for name in completion:
        if completion_name.get(name) == None:
            completion_name[name] = 1
        else:
            completion_name[name] += 1
    
    for name in participant:
        if completion_name.get(name) == None:
            return name
        
        if completion_name[name] == 1:
            del completion_name[name]
        else:
            completion_name[name] -= 1