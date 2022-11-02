n = int(input())
nums = set(range(1, n + 1))
while True:
    quest = input()
    if quest == 'HELP':
        break
    quest = set(int(x) for x in quest.split())
    if len(nums & quest) > len(nums) / 2:
        print('YES')
        nums &= quest
    else:
        print('NO')
        nums &= nums - quest

print(' '.join([str(x) for x in sorted(nums)]))
