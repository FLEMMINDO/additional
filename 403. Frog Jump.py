def canCross(stones):
    if stones[1] != 1:
        return False
    else:
        queue = [(1,1)]
        seen = set()
        last_stone = stones[-1]
        stones = set(stones)

        while queue:

            stone_num,k = queue.pop(0)

            if stone_num == last_stone:
                return True

            for neib in [k-1,k,k+1]:
                next_pos = stone_num+neib
                if next_pos == stone_num:
                    continue

                if next_pos in stones and (next_pos,neib) not in seen:
                    queue.append((next_pos, neib))
                    seen.add((next_pos,neib))
    return False


print(canCross([0,1,3,5,6,8,12,17]))