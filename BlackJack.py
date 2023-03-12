import random
import sys

#トランプのカードの設定
Love = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Diamond = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Clover = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Spade = [1,2,3,4,5,6,7,8,9,10,11,12,13]
All_Card = []
All_Card.extend(Love)
All_Card.extend(Diamond)
All_Card.extend(Clover)
All_Card.extend(Spade)




def BlackJack():
    print("ブラックジャックをはじめます。")
    #プレイヤー1枚目の操作
    player_card1 = random.choice(All_Card)
    print("あなたの1枚目は" + str(player_card1) + "です。")
    if player_card1 >10:
        player_card1 = 10
    if player_card1 == 1:
        player_card1 = int(input("Aを引きました。1or11を選んで入力してください。"))
    #プレイヤー2枚目の操作
    player_card2 = random.choice(All_Card)
    print("あなたの2枚目は" + str(player_card2) + "です。")
    if player_card2 >10:
        player_card2 = 10
    if player_card2 == 1:
        player_card2 = int(input("Aを引きました。1or11を選んで入力してください。"))
    player_card_sum = player_card1 + player_card2
    print("現在のカードの合計は" + str(player_card_sum) + "です。")
    #ディーラー1枚目の操作
    dealer_card1 = random.choice(All_Card)
    print("ディーラーの1枚目のカードは" + str(dealer_card1) + "です")
    if dealer_card1 >10:
        dealer_card1 = 10
    if dealer_card1 == 1:
        dealer_card1 = 11
    #プレイヤーがヒットするかステイするかの操作
    choice_number1 = int(input("hitする場合は" + str(1) + "をstandする場合は" + str(2) + "を入力してください。"))
    count = 2
    player_hand=[0]
    while choice_number1 == 1:
        player_card3 = random.choice(All_Card)
        if player_card3 >10:
            player_card3 = 10
        if player_card3 == 1:
            player_card3 = int(input("Aを引きました。1or11を選んで入力してください。"))
        count += 1
        player_hand.append(player_card3)
        print("あなたの" + str(count) + "枚目のカードは" + str(player_card3) + "です。")
        choice_number1 = int(input("hitする場合は" + str(1) + "をstandする場合は" + str(2) + "を入力してください。"))
    else:
        pass
    player_card_sum = player_card_sum + sum(player_hand)
    print("あなたの合計は" + str(player_card_sum) + "です。この数でディラーと勝負します。")
    if player_card_sum > 21:
        print("あなたはバーストしました。あなたの負けです。")
        sys.exit()
    #ディーラー2枚目の操作
    dealer_card2 = random.choice(All_Card)
    print("ディーラーの2枚目のカードは" + str(dealer_card2) + "です")
    if dealer_card2 >10:
        dealer_card2 = 10
    if dealer_card2 == 1:
        if dealer_card2 + 11 > 21:
            dealer_card2 = 1
        else:
            dealer_card2 = 11    
    dealer_card_sum = dealer_card1 + dealer_card2
    #ディーラー3枚目以降の操作
    if dealer_card_sum  > 16:
        print("ディーラーの合計は" + str(dealer_card_sum) + "です")
    elif dealer_card_sum < 17:
        dealer_hand = [0]
        card_sum = 0
        count1 = 2
        while dealer_card_sum < 17:
            dealer_card3 = random.choice(All_Card)
            count1 += 1
            print("ディーラーの" + str(count1) + "枚目のカードは" + str(dealer_card3) + "です。")
            if dealer_card3 >10:
                dealer_card3 = 10
            if dealer_card3 == 1:
                if dealer_card_sum + 11 > 21:
                    dealer_card3 = 1
                else:
                    dealer_card3 = 11
            dealer_card_sum = dealer_card_sum + dealer_card3
        else:
            dealer_card_sum = dealer_card_sum + card_sum
            print("ディーラーの合計は" + str(dealer_card_sum) + "です")
    #比較の操作

    if dealer_card_sum == player_card_sum:
        print("引き分けです。")
    elif dealer_card_sum > player_card_sum and dealer_card_sum < 22:
        print("ディーラーの勝ちです。")
    elif dealer_card_sum < player_card_sum and player_card_sum < 22:
        print("あなたの勝ちです。おめでとうございます。")
    elif dealer_card_sum > 21:
        print("ディーラーがバーストしたのであなたの勝ちです。")

    print("これにてブラックジャックを終了します。")


BlackJack()






    


              
        







    