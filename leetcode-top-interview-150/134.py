class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        lth = len(gas)
        req = [gas[i] - cost[i] for i in range(lth)]

        start = 0
        remain = 0

        for i in range(lth):
            remain += req[i]
            if remain < 0:
                remain = 0
                start = i + 1

        return start
