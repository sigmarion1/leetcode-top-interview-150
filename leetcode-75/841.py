class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = []
        stack.extend(rooms[0])
        history = {0}

        while stack:
            room = stack.pop()

            if room in history:
                continue

            stack.extend(rooms[room])
            history.add(room)

        return len(history) == len(rooms)
