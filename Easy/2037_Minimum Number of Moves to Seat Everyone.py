class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
        thought:
        - we need to move 1 step each time to let the position of students all equal to the position of seats
        - we need to find the min move steps
        - the idea is that every student should find the closest seat from he/she
            - sort two list
            - do minus calculation between students and seats index by index
        """
        steps = 0
        seats = sorted(seats)
        students = sorted(students)
        for (seat, student) in zip(seats, students):
            steps += abs(seat - student)
        return steps
