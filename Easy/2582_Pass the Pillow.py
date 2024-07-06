class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """
        thought:
        - the location of pillow at every second is as below:
            - round 0 -> 1~(n-1) seconds : 1~n person
            - round 1 -> (n-1)~(n-1)*2 seconds : n~1 person
            - round 2 -> (n-1)*2~(n-1)*3 seconds : 1~n person
        - so we can do the following steps:
            (1) use `time // (n-1) & time % (n-1)` to get the round `d` and the remaining `r`
                - if round % 2 == 0, remaining+1 = answer
                - if round % 2 != 0, n-remaining+1 = answer
        - Note that at the first second, pillow sent from the first person to the second.
        """
        d = time // (n-1)
        r = time % (n-1)
        if d % 2 == 0:
            return r+1
        else:
            return (n-1)-r+1
