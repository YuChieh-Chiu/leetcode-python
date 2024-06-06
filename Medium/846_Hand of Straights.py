class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        thought:
        - len(hand) % groupSize should equal to 0; otherwise, the list cannot be rearrange
        - if `groupSize` == 1, then it can 100% be rearrange
        - sort the list `hand`
        - greedy search from the min number : 
            - pass greedy search -> continue
                - if comes to the last number, check whether the number == last_number + 1 or not
                - if not, just check whether there's a number in `hand` == last number + 1
                - check the next step is in a new sub-list or in the existing sub-list
            - otherwise, return False
        """
        if len(hand) % groupSize != 0:
            return False
        else:
            if groupSize == 1:
                return True
            else:
                hand = sorted(hand, reverse=False)                
                loop = 1
                last_num = hand[0]
                hand.remove(last_num)
                while True:   
                    if (len(hand) == 1):
                        if (last_num + 1) == hand[0]:
                            return True         
                        else:
                            return False                
                    if (last_num + 1) in hand:
                        last_num += 1
                        hand.remove(last_num)
                    else:
                        return False
                    if (loop + 1) % groupSize == 0:
                        loop = 1
                        last_num = hand[0]
                        hand.remove(last_num)
                    else:
                        loop += 1               
