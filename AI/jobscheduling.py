# Jobs, Profit, Slot
profit = [15,27,10,100, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2,3,3,3,4] 
profitNJobs = list(zip(profit,jobs,deadline))
profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)
slot = []
for _ in range(len(jobs)):
    slot.append(0)

profit = 0
ans = []

for i in range(len(jobs)):
    ans.append('null')

for i in range(len(jobs)):
        job = profitNJobs[i]
        #check if slot is occupied
        for j in range(job[2], 0, -1):
            if slot[j] == 0:
                ans[j] = job[1]
                profit += job[0]
                slot[j] = 1
                break
        
print("Jobs scheduled buddy:",ans[1:])
print(profit)

# Explanation:

# The code represents a job scheduling problem where each job has a profit and a deadline.

# The profit, jobs, and deadline lists represent the profit, names, and deadlines of the jobs, 
# respectively.

# The profitNJobs list is created by zipping the profit, jobs, and deadline lists together. 
# Each element in profitNJobs contains the profit, job name, and deadline of a job.

# The profitNJobs list is sorted in descending order based on the profit using the 
# sorted function and the lambda function as the key.

# The slot list is initialized with zeros, representing the availability of slots
#  for each deadline.

# The profit variable is initialized to 0.

# The ans list is initialized with 'null' placeholders for each job.

# The first loop iterates over the range of the number of jobs. It appends 'null' 
# to the ans list for each job.

# The second loop iterates over the range of the number of jobs. It selects a job
#  from the sorted profitNJobs list.

# The nested loop checks if there is an available slot for the job's deadline, starting 
# from the job's deadline and moving backwards.

# If an available slot is found (slot[j] == 0), the job name is assigned to the ans list 
# at that slot (ans[j] = job[1]), the profit of the job is added to the total profit 
# (profit += job[0]), the slot is marked as occupied (slot[j] = 1), and the inner loop is terminated using break.

# Finally, the jobs scheduled are printed (excluding the first element in ans which is 'null') 
# and the total profit is printed.

# In summary, the code implements a greedy algorithm for job scheduling. It sorts the jobs in
#  descending order of profit and assigns them to available slots based on their deadlines.
#   The goal is to maximize the total profit by scheduling jobs efficiently.