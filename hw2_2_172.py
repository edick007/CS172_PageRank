'''
Homework 2 172 problem 2: Coding page rank algorithm
Edward Dickhoff

Assignment: Write a program (e.g., in Java) to compute the final scores 
of the nodes and the number of iterations needed to converge, if we use 
convergence constant epsilon=0.001.

Assumptions: 
set up is the same as problem one: number of nodes is 5, dampening factor is .7, e = .001
'''
#declare variables for page rank
    #number of pages
n = 5
d = 0.7
    #list holding PR(A), PR(B),...exc...
PR_previous = [1.0, 1.0, 1.0, 1.0, 1.0]
PR_saved_previous = [1.0, 1.0, 1.0, 1.0, 1.0]
PR_current = [0.0, 0.0, 0.0, 0.0, 0.0]
    #stop value for difference between iterations  
e = 0.001
itt = 0

def print_values(values):
    print(*values, sep = "\n") 
    return
    
#check if done
def done_test(prev, curr, saved):
    value = 1
    total = 0
    for i in range(len(PR_current)):
        if(i != 3):
            diff = curr[i] - saved[i]
            #total += abs(diff)
    #print('total diff', total)
        if(abs(diff) <= e):
            value = 0
            break
    return value

#def PR_1():
while (done_test(PR_previous, PR_current, PR_saved_previous) == 1):
    itt += 1
    PR_current = [0.0, 0.0, 0.0, 0.0, 0.0]
    #print('iterations = ',itt)
    #calculate the base iteration PRs
    #Pr1
    rank = (1-d)/n + d*PR_previous[3-1]/1
    PR_current[0] = rank
    #pr2
    rank = (1-d)/n + d*PR_previous[1-1]/1
    PR_current[1] = rank
    #pr3
    rank = (1-d)/n + d*PR_previous[2-1]/2
    PR_current[2] = rank
    #pr4
    rank = (1-d)/n 
    PR_current[3] = rank
    #pr5
    rank = (1-d)/n + d*(PR_previous[2-1]/2) + d*(PR_previous[5-1]/1) + d*(PR_previous[4-1]/1)
    PR_current[4] = rank
    #set PR_previous to be current  
    PR_saved_previous = PR_previous
    PR_previous = PR_current
    #print('saved')
    #print_values(PR_saved_previous)

print('total iterations = ',itt)
print('Answer')
print_values(PR_current)

