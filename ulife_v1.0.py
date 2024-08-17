import random  
import time  
import sys  
import tkinter as tk  

# pyinstaller --onefile ulife_v1.0.py

# 定义全局变量
achievement = []

def main():
    # 创建一个tkinter窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏窗口

    # 设置窗口图标
    root.iconbitmap('D:/code/tiny_code/ulife_v1.0/icon.ico')

    # 首先打印一个菜单栏  
    print('--------------------------------------------')  
    print('|大学之旅让我们毕生难忘|')  
    print('|                      |')  
    print('|欢迎来到大学生活模拟器|')  
    print('--------------------------------------------')  

    # 接下来，创建颜值，体质，智力，家境  
    # 这四个属性值都要在0-10之间，总和不要超过20  

    evaluation = ["享乐主义者", "寂寂无名", "有钱能使鬼推磨", "卷王", "平凡的大多数", "中道崩殂", "人生赢家"]
    subject = ["文科", "理科", "工科"]
    while True:  
        print("请输入你的属性值")  
        face = int(input("请输入你的颜值："))  
        strong = int(input("请输入你的体质："))  
        iq = int(input("请输入你的智商: "))  
        home = int(input("请输入你的家境："))  

        # 如果单个属性值超过10,提示用户重新输入  
        if (face > 10 or face < 0):  
            print("颜值输入错误，请重新输入")  
            continue  
        if (strong > 10 or strong < 0):  
            print("体质输入错误，请重新输入")  
            continue  
        if (iq > 10 or iq < 0):  
            print("智商输入错误，请重新输入")  
            continue  
        if (home > 10 or home < 0):  
            print("家境输入错误，请重新输入")  
            continue  
        if (face + strong + iq +home > 20):  
            print("属性值总和错误，请重新输入")  
            continue  
        print("颜值:",face, "体质:",strong,"智商:",iq,"家境:",home)  
        break  

    #接下来生成角色性别  
    # 使用random可以生成随机数  
    point = random.randint(1,3)  
    if point == 1:  
        gender = '男'  
        print("你是一个男孩")
        strong += 1
    elif point == 2:  
        gender = '女'  
        print("你是一个女孩")
        face += 1
    else:  
        gender = '浣熊'  
        print("你是一只浣熊")  
        strong += 2
        face += 2
        iq -= 2
    time.sleep(1)

    # 设置高考分数
    score = random.randint(home*10,750)
    # 根据智商增加高考分数
    score += iq*30
    if score > 750:
        score = 750
    print("你的高考分数是：",score)
    time.sleep(1)

    def end_game(game_score, evaluate):
        print("游戏结束")
        game_score += face + strong + iq + home
        print("您最终的得分为：", game_score)
        if evaluate not in achievement:
            achievement.append(evaluate)
        print(f"您的评价为：{evaluate}({len(achievement)}/7)")
        if len(achievement) == 7:
            print("您已完成所有成就，恭喜！")
        time.sleep(1)
        print("1.重活一世")
        print("2.退出游戏")
        choice = int(input("请输入你的选择(1-2):"))
        while True: 
            if choice == 1:
                main()
            elif choice == 2:
                print("感谢您的游玩，再见！")
                sys.exit(0)
            else:
                print("输入错误，请重新输入")

    def end_year(year_score, home, game_score):
        if year_score > 4:
            year_score = 4
        print(f"本年度绩点为：{year_score} (满绩点为4.0)")
        if year_score > 3.5:
            print("你考的很好，获得了奖学金")
            home += 1
        elif year_score > 2.5:
            print("你成功通过了考试")
        else:
            print("你挂科了，需要补考")
            point = random.uniform(0,1)
            if point > 0.5:
                print("补考通过")
            else:
                print("补考失败，你被学校开除了")
                game_score += 2
                evaluate = evaluation[5]
                end_game(game_score, evaluate)
        time.sleep(1)


    # 根据高考分数选择大学
    if score > 700:
        print("你考上了清华北大,获得了家乡的奖学金")
        home += 2
        face += 1
    elif score > 600:
        print("你考上了985高校")
    elif score > 500:
        print("你考上了普通高校")
    elif score > 400:
        print("你考上了专科")
    else:
        if home > 8:
            print("家里太有钱了，你每天都沉浸于奢靡享乐之中")
            time.sleep(1)
            point = random.uniform(0,1)
            if point > 0.3:
                print("你沉迷于享乐，最终猝死")
                game_score = 0
                evaluate = evaluation[0]
            else:
                print("你醒悟过来，继承了家业，最终成为了一个成功人士")
                game_score = 10
                evaluate = evaluation[2]
            end_game(game_score, evaluate)
        else:
            print("你未考上任何院校，回家种地，度过了一个平淡的人生")
            game_score = 5
            evaluate = evaluation[1]
            end_game(game_score, evaluate)
    time.sleep(1)

    # 选择专业
    print("请选择你的专业：")
    print("1. 文科")
    print("2. 理科")
    print("3. 工科")
    while True:
        subject_choice = int(input("请输入你的选择(1-3):"))
        if subject_choice == 1:
            subject = subject[subject_choice-1]
            face += 4
            strong += 2
            break
        elif subject_choice == 2:
            subject = subject[subject_choice-1]
            iq += 4
            face += 2
            break
        elif subject_choice == 3:
            subject = subject[subject_choice-1]
            home += 4
            iq += 2
            break
        else:
            print("无效的选择，请重新输入")

    print(f"你选择了{subject}")
    time.sleep(1)

    # 大学生活
    # 设置互动选项
    # 学习、运动、娱乐、科研、比赛、实习、社团、就业、创业
    choices = ["学习", "运动", "娱乐", "比赛", "科研", "社团", "实习"]


    # 本科阶段
    year = 1                # 年份
    count = 1               # 选择次数
    shixi = 0               # 实习index
    year_score = 0          # 年度绩点(4分制)
    work_score = 0          # 工作加分(100分制)
    fur_study_score = 0     # 研究生加分(100分制)
    game_score = 0          # 总分
    while True:
        print(f"大学生活的第{year}年，请选择：({count}/6)")
        # 实习（大三才开始有）
        if year == 3:
            shixi = 1
        for i in range(6 + shixi):
            print(f"{i+1}. {choices[i]}")
        choice = int(input("请输入你的选择(数字):"))
        # 学习
        if choice == 1:
            point = random.uniform(0,1)
            if point > 0.97:
                print("你太努力了，导致身体垮掉，最终猝死")
                game_score += 5
                evaluate = evaluation[3]
                end_game(game_score, evaluate)
            elif point > 0.4:
                print("你觉得自己学习很有收获")
                iq += 1
                year_score += 0.8
            else:
                print("你觉得自己没学到什么")
                year_score += 0.3
        # 运动
        elif choice == 2:
            point = random.uniform(0,1)
            strong += 2
            if point > 0.96:
                print("你不小心骨折了")
                strong -= 4
            elif point > 0.4 and strong > 10:
                print("你拥有了八块腹肌")
                face += 2
            else:
                print("你的身体更强壮了")
        # 娱乐
        elif choice == 3:
            point = random.uniform(0,1)
            if point > 0.92:
                print("打游戏获得冠军，获得了奖金")
                home += 1
            elif point > 0.4:
                print("打游戏很开心，但是身体变差了")
                strong -= 1
            else:
                print("打游戏很开心")
        # 比赛
        elif choice == 4:
            home -= 1
            point = random.uniform(0,1)
            if point > 0.96 or iq > 20:
                print("你获得了一等奖")
                face += 1
                year_score += 0.2
                home += 3
                work_score += 15
                fur_study_score += 15
            elif point > 0.4 and iq > 8:
                print("你获得了二等奖")
                face += 1
                year_score += 0.1
                home += 2
                work_score += 8
                fur_study_score += 8
            else:
                print("很不幸，你未获奖")
                year_score += 0.1
        # 科研
        elif choice == 5:
            point = random.uniform(0,1)
            strong -= 1
            if point > 0.7 and iq > 30:
                print("你成功发出一篇SCI论文")
                game_score += 2
                face += 1
                iq += 5
                year_score += 1
                home += 1
                work_score += 50
                fur_study_score += 90
            elif point > 0.4 and iq > 8:
                print("你获得了一项专利")
                year_score += 0.5
                home += 1
                work_score += 20
                fur_study_score += 30
            else:
                print("你没有获得任何成果，但你感觉收获了很多")
                year_score += 0.2
        # 社团
        elif choice == 6:
            point = random.uniform(0,1)
            if point > 0.80 and face > 10:
                print("你成为了漫画社社长")
                game_score += 1
                face += 4
                fur_study_score += 10
            elif point > 0.2:
                print("你成功加入了一个社团")
                face += 1
                fur_study_score += 3
            else:
                print("你未加入任何社团")
        # 实习
        elif choice == 7:
            point = random.uniform(0,1)
            if point > 0.85 and iq > 10:
                print("你获得了鹅厂的实习offer")
                face += 2
                year_score += 1.5
                iq += 1
                work_score += 50
            elif point > 0.4:
                print("你获得了一个不知名的小公司的实习工作")
                face += 1
                year_score += 1.0
                work_score += 20
            else:
                print("你未获得实习工作")
                year_score += 0.5
        # 本科各阶段结算     
        if year == 4 and count == 6:
            break
        if count == 6:
            year += 1
            count = 0
            if iq > 20:
                year_score += random.uniform(iq, 20)*0.1
                end_year(year_score, home, game_score)
                year_score = 0
            else:
                year_score += random.uniform(20, iq)*0.1
                end_year(year_score, home, game_score)
                year_score = 0
        count += 1
        time.sleep(1)

    # 就业&研究生
    print("大学本科的生活已经结束，你的选择是")
    print("1. 就业")
    print("2. 创业")
    print("3. 读研")
    choice = int(input("请输入你的选择(数字):"))
    while True:
        if choice == 1:
            point = random.uniform(0,1)
            if point > 0.5 and work_score > 50 and iq > 8:
                print("你成功找到一份大厂工作")
                game_score += 20
                if iq > 20 and point > 0.7 and face > 10:
                    print("你成为的CEO,走上了人生巅峰")
                    game_score += 100
                evaluate = evaluation[6]
                end_game(game_score, evaluate)
            elif point > 0.2 and work_score > 10:
                print("你成功找到一份普通工作，成为一名社畜")
                game_score += 10
                evaluate = evaluation[1]
                end_game(game_score, evaluate)
            else:
                print("你找不到工作，只能进厂了")
                game_score += 5
                evaluate = evaluation[1]
                end_game(game_score, evaluate)
        elif choice == 2:
            point = random.uniform(0,1)
            if point > 0.4 and iq > 20:
                print("你成功创业，成为了一名企业家")
                game_score += 100
                if iq > 40 and point > 0.5 and face > 10:
                    print("你创建了一家世界500强企业，成为了世界首富")
                    game_score += 1000
                evaluate = evaluation[6]
                end_game(game_score, evaluate)
            elif point > 0.2 and iq > 5:
                print("你和别人一起创业，卖起了羊肉串")
                game_score += 10
                evaluate = evaluation[1]
                end_game(game_score, evaluate)
            else:
                print("你创业失败，进厂喽")
                game_score += 5
                evaluate = evaluation[1]
                end_game(game_score, evaluate)
        elif choice == 3:
            point = random.uniform(0,1)
            if point > 0.4 and fur_study_score > 50 and iq > 8:
                print("你成功考上清北研究生")
                game_score += 20
                if iq > 20 and point > 0.7 and face > 10:
                    print("你成为了一名教授，教书育人")
                    game_score += 100
                evaluate = evaluation[6]
                end_game(game_score, evaluate)
            elif point > 0.2 and fur_study_score > 10:
                print("你成功考上一本高校研究生")
                game_score += 10
                evaluate = evaluation[4]
                end_game(game_score, evaluate)
            else:
                print("你考研失败，只能打工了")
                game_score += 5
                evaluate = evaluation[1]
                end_game(game_score, evaluate)
        else:
            print("无效的选择，请重新输入")

if __name__ == "__main__":
    main()
