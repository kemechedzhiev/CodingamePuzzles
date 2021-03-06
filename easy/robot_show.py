# TODO Two rooms are connected by a service duct allowing floor-sweeping bots to move between the rooms.
#  The duct is very narrow, just wide enough for one bot to pass through.
#  The bots do not have visual, lazer, radar or anything to detect obstacles.
#  Their only sensory is touching. If they meet in the duct, they will bump into each other.
#  Collision will cause each of them to turn around to continue moving in the opposition direction.
#  Bob finds that it is very interesting to watch the bots bumping and bouncing back and forth.
#  He prepared a longer transparent duct and put more bots into it, wishing to watch a sequence
#  of bumping and bouncing "bot-show". He designed some starting locations for the bots and then
#  turned them all ON at the same time.
#  - assume the bots move at a constant speed of 1 meter/second,
#  - assume the bots have a diameter small enough to be negligible in calculation of travel distance,
#  - assume no bot will go from the rooms into the duct during "show-time",
#  - assume Bob is free to arrange every bot to face it either Left or Right before starting the show...
#  What is the longest possible time for the bots to run around in the duct until all bots exit?


def time_on_the_duct(position_on_duct):
    temp_result = list()
    for entry in position_on_duct:
        temp_result.append(max(entry, length - entry))
    return max(temp_result)


if __name__ == '__main__':
    # print('Mission started')
    length = int(input())
    number_of_bots = int(input())
    position = [int(i) for i in input().split(' ')]
    print(time_on_the_duct(position))
