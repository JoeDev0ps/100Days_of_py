## TASK ONE - Reeborg's World: Hurdles
#
# My attempt
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# for _ in range(6):
#     move()
#     jump()




## TASK TWO - Reeborg's World: Hurdles 2, the random flag placement
#
# My attempt
# 
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
## can re-write function as 'while not at_goal():'
#
# while at_goal() != True:
#     jump()
#
## changed the jump function so we moved first, used while loop to jump if not at goal




## TASK THREE - Reeborg's World: Hurdles 3, the random hurdle placement
#
# My attempt
# 
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#   
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#   
# while True:
#     if wall_in_front() == True:
#         jump()
#     elif wall_in_front() == False and at_goal() == False:
#         move()
#     else:
#         break
# 
## TUTOR CODE
# 
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()




## TASK FOUR - Reeborg's World: Hurdles 4, the random hurdle height
#
# My attempt
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#  
# def jump():
#     if wall_in_front() == True:
#         turn_left()
#     elif wall_in_front() and right_is_clear() != True:
#         move()
#     elif wall_in_front() and right_is_clear() == True:
#         turn_right()
#         move()
#         turn_right()
#         move()
#         if right_is_clear() == True and wall_in_front() != True:
#             move()
#             if right_is_clear() == True and wall_in_front() == True:
#                 turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
#
## 2nd Attempt - Works sometimes
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# 
# def jump():
#     turn_left()
#     while wall_in_front() != True and right_is_clear() != True:
#         move()
#     if right_is_clear() == True:
#         turn_right()
#         move()
#         turn_right()
#         move()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     elif right_is_clear() != True and wall_in_front != True:
#         move()
#     else:
#         turn_left() 
#
# Can remove last 2 lines from else statement and works, 20 lines!
# Can alter line 8/132 and change while loop to 'wall_on_right()'
#
# TUTOR CODE
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#  
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()




## TASK FIVE - Reeborg's World: Maze
#
# TUTOR CODE
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
#
# Doesn't work
# Come back AFTER Day 15 to debug ^ code




# TOP TIP
# For loops are great for iterating and doing something with each item
# While loops are great for endlessly functioning until a condition is met
# While loops present danger in form of infinite loop