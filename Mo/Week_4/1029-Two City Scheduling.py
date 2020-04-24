"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 
Example 1:

    Input: [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    Explanation: 
    The first person goes to city A for a cost of 10.
    The second person goes to city A for a cost of 30.
    The third person goes to city B for a cost of 50.
    The fourth person goes to city B for a cost of 20.

    The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:
1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""
# The idea is to figure out for each person, how much impact they will have on our company 
# To work this out we can take the absolute value of the city A - city B 
# Then if we sort by smallest impact to highest impact 
# The lower the number the lower impact this person will have 

# Lastly there are 2N people - e.g 2N = Length of the list (if list is 4, 4 people)
# N people much arrive in each city which means 2N/2 = N (e.g 4/2 -> 2)
# Time complexity O(nlogn) and Space Complexity of O(1)
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort the list based on the absolute value of the two cities
        # without lambda we can create the following function
        #costs.sort(key=lambda x: x[0] - x[1])
        def difference(batch_costs): 
            return batch_costs[0] - batch_costs[1]
        
        costs.sort(key=difference)
        # It is guranteed that the number of people will be even (2N)
        cap = len(costs) / 2
        min_cost = 0
        for i in range(len(costs)): 
            if i < cap:
                min_cost += costs[i][0]
            else: 
                min_cost += costs[i][1]
        return min_cost    