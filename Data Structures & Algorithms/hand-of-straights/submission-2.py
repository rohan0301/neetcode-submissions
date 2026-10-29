from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hashmap = defaultdict(int)
        hand.sort()
        for card in hand:
            hashmap[card] += 1
        
        '''
        hashmap: { 2: 1, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1}
        temp = [1]
        '''
        count = set()
        while len(hashmap) > len(count):
            temp = []
            for card in hashmap:
                if card in count:
                    continue
                if hashmap[card] == 0:
                    continue
                if temp:
                    if card - 1 == temp[-1]:
                        temp.append(card)
                        hashmap[card] -= 1
                    else:
                        return False
                else:
                    temp.append(card)
                    hashmap[card] -= 1
                if hashmap[card] == 0:
                    if card not in count:
                        count.add(card)
                    #del hashmap[card]
                if len(temp) == groupSize:
                    break
            if len(temp) != groupSize:
                return False
        return True
            

