# 다리를 지나는 트럭
# 이 코드는 아래 문제의 이해를 돕기 위해 만들어 졌습니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
import os
from time import sleep

# 문제 풀이
from collections import deque
def solution(bridge_length, weight, truck_weights):
    global answer, input_param
    input_param = bridge_length, weight, truck_weights
    # initailize variables
    answer = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)

    # problem solving
    while trucks:
        view(bridge_length, bridge)
        answer += 1
        bridge.popleft()
        if sum(bridge) + trucks[0] <= weight:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)

    # answer만 구하기 위해서라면 아래 4줄의 코드를
    ''' answer += bridge_length ''' # 로 대체해도 됩니다.
    while bridge:
        view(bridge_length, bridge)
        answer += 1
        bridge.popleft()
    view(bridge_length, bridge)
    return answer

# 화면 출력을 위한 코드입니다 문제풀이와 관련 없습니다.
def view(bridge_length,bridge):
    global answer, input_param
    unit_length, padding = 6, 3
    sky_depth, land_depth = 6, 3
    width, height, side_length = (bridge_length+4) * unit_length + padding*2 - 1, 10, unit_length*2
    border = ['•']*(width + 2)
    output = [border]+[['•']+[' ']*width+['•'] for _ in range(height)]+[border]
    os.system('clear') # 화면을 지웁니다.

    trucks_on_the_bridge =' '+''.join([f'[{x:>2}]  ' if x else ' '*6 for x in list(bridge)+[0]*(bridge_length-len(bridge))]) + ' '
    side = ['◼']*(unit_length*2)
    objects_left_side = '⇮🢕🢕 ⇮ ⇮ 🠹 '*(side_length//10)+'⇮🢕🢕 ⇮ ⇮ 🠹 '[:side_length%10]
    objects_right_side = ' 🢙 🢕🢕 🠱🠭  '*(side_length//10)+' 🢙 🢕🢕 🠱🠭  '[:side_length%10]
    bridge_= ' '+' '.join(['◼◼◼◼◼']*bridge_length)+' '
    
    time_info = f'time: {answer:>2}s'
    param_names = ["bridge_length", "weight", "truck_weights"]
    param_info = [f'{x:>2}' if type(x) is int else ', '.join([str(a) for a in x]) for x in input_param]

    for j in range(len(time_info)):
        output[2][j+padding] = time_info[j]
    
    for i in range(len(param_info)-1):
        for j in range(len(param_names[i])+1):
            output[i+2][j+width//3] = ''.join([*param_names[i],':'])[j]
        for j in range(len(param_info[i])):
            output[i+2][j+15+width//3] = param_info[i][j]

    for i in range(land_depth+1):
        for j in range(side_length):
            output[sky_depth+1+i][padding+j] = side[j]
            output[sky_depth+1+i][-padding-side_length+j] = side[j]
    
    for j in range(len(bridge_)):
        output[sky_depth+1][padding+side_length+j] = bridge_[j]
    
    for j in range(side_length):
        output[sky_depth][padding+j] = objects_left_side[j]
        output[sky_depth][-padding-side_length+j] = objects_right_side[j]
    
    for j in range(len(bridge_)):
        output[sky_depth][padding+side_length+j] = trucks_on_the_bridge[j]

    draw(output) # 화면을 그립니다.
    sleep(1) # 1초 대기합니다.

def draw(output):
    print('\n'.join([''.join(line) for line in output]))

solution(4, 14, [7, 4, 5, 6])