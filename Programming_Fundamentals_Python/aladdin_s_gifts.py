from collections import deque


def check_in_table(current_sum, made_gifts):
    if 100 <= current_sum <= 199:
        made_gifts['Gemstone'] += 1
    elif 200 <= current_sum <= 299:
        made_gifts['Porcelain Sculpture'] += 1
    elif 300 <= current_sum <= 399:
        made_gifts['Gold'] += 1
    elif 400 <= current_sum <= 499:
        made_gifts['Diamond Jewellery'] += 1


materials_stack = [int(x) for x in input().split()]
magic_level_deque = deque([int(x) for x in input().split()])
crafted_gifts = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}

while materials_stack and magic_level_deque:
    current_material = materials_stack.pop()
    current_magic_level = magic_level_deque.popleft()
    attempt_sum = current_material + current_magic_level
    if attempt_sum < 100:
        if attempt_sum % 2 == 0:
            current_material *= 2
            current_magic_level *= 3
            attempt_sum = current_material + current_magic_level
        else:
            attempt_sum *= 2
        check_in_table(attempt_sum, crafted_gifts)
    elif attempt_sum > 499:
        attempt_sum /= 2
        check_in_table(attempt_sum, crafted_gifts)
    else:
        check_in_table(attempt_sum, crafted_gifts)
wedding = False
for gift in crafted_gifts:
    if crafted_gifts['Gemstone'] > 0 and crafted_gifts['Porcelain Sculpture'] > 0 or\
             crafted_gifts['Gold'] > 0 and crafted_gifts['Diamond Jewellery'] > 0:
        wedding = True
if wedding:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials_stack:
    print(f'Materials left: {", ".join(str(x) for x in materials_stack)}')
if magic_level_deque:
    print(f'Magic left: {", ".join(str(x) for x in magic_level_deque)}')
for present, number in sorted(crafted_gifts.items()):
    if number:
        print(f'{present}: {number}')
