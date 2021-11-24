# title : Name check
i=input(print("Please type 0 to exit or 1 to continue"))
i=1
while i>0:
    user_word = input("please write the word you want to check: ")
    word_type = type("cemal")
    print(word_type)
    user_word_type = type(user_word)
    print(user_word_type)
    if  word_type != user_word_type :
        user_word = input("please write the word you want to check again:")
    lenght_user_word = len(user_word)

    loop_times = []
    if int(lenght_user_word % 2) == 1 :
        loop_times = int((lenght_user_word - 1) / 2)
    else :
        loop_times = int(lenght_user_word / 2)
    def word_check():
        i=0
        while i<loop_times :
            i += 1
            if user_word[i-1] == user_word[lenght_user_word - i]:
                continue
            else: print("not")
            break
        print("same")

    word_check()

