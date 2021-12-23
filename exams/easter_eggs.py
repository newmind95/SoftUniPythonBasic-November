number_painted_eggs = int(input())
count_red_paint = 0
count_orange_paint = 0
count_blue_paint = 0
count_green_paint = 0

for eggs in range(0, number_painted_eggs):

    color_of_egg = input()

    if color_of_egg == 'red':
        count_red_paint += 1
    elif color_of_egg == 'orange':
        count_orange_paint += 1
    elif color_of_egg == 'blue':
        count_blue_paint += 1
    elif color_of_egg == 'green':
        count_green_paint += 1

print('Red eggs: %d' % count_red_paint)
print('Orange eggs: %d' % count_orange_paint)
print('Blue eggs: %d' % count_blue_paint)
print('Green eggs: %d' % count_green_paint)

max_painted_eggs = count_red_paint
max_color = 'red'

if max_painted_eggs < count_orange_paint:
    max_painted_eggs = count_orange_paint
    max_color = 'orange'
    print('Max eggs: %d -> %s' % (max_painted_eggs, max_color))
elif max_painted_eggs < count_blue_paint:
    max_painted_eggs = count_blue_paint
    max_color = 'blue'
    print('Max eggs: %d -> %s' % (max_painted_eggs, max_color))    
elif max_painted_eggs < count_green_paint:
    max_painted_eggs = count_green_paint
    max_color = 'green'
    print('Max eggs: %d -> %s' % (max_painted_eggs, max_color))
    
