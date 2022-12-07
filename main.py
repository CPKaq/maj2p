import maj2p


def main():
    # 创建牌山、手牌及牌河
    wall = maj2p.Wall()
    player = [maj2p.Hand(0), maj2p.HandAuto(1)]
    # 立直、自摸
    riichi = [0, 0]
    tsumo = False
    # 庄家
    dealer = 0
    # 和牌方
    call_win = -1

    # flag
    flag_first_round = True
    flag_riichi_round = [False, False]

    # 配牌
    for p in player:
        for _ in range(13):
            p.draw(wall.get())
        p.sort()

    # wall.print_wall()
    # player[0].print()
    # player[1].print()

    # 打牌
    curr_wind = dealer
    while not wall.is_empty():
        player[curr_wind].draw(wall.get())
        if curr_wind == 0:
            player[0].print('立直' if riichi[0] else '')
            while True:
                input_str = input()
                if input_str == '0':
                    call_win = 0
                    tsumo = True
                    break
                if riichi[0]:
                    player[0].discard(13)
                    break
                if len(input_str) < 1:
                    continue
                if player[0].discard_by_face(maj2p.get_face(input_str[0])):
                    if len(input_str) > 1:
                        riichi[0] = 2 if flag_first_round else 1
                    break
                else:
                    print(f"{input_str} not found!")
            player[0].print('立直' if riichi[0] else '')
        else:
            if player[1].is_win():
                call_win = 1
                tsumo = True
                break
            discard = player[curr_wind].discard(13)
            input_str = input()
            if input_str == '0':
                player[0].draw(discard)
                call_win = 0
                break

        if call_win != -1:
            break
        curr_wind = (curr_wind + 1) % 2
        flag_first_round = False

    # 结算
    han = player[call_win].win()
    han.check_win(riichi=riichi[0], tsumo=tsumo)
    # if riichi[0] == 2:
    #     han.append_yaku("两立直", 2)
    # elif riichi[0] == 1:
    #     han.append_yaku("立直", 1)
    if flag_first_round == 9:
        han.append_yakuman("天和")
    elif wall.wall_remain() == 0:
        han.append_yaku("海底捞月", 1)
    if han.is_win:
        han.stat()
        print(han.score)
    else:
        print("Not win")

# while True:
#     main()


main()
