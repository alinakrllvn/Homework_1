# Your code here 𓆉𓆝 𓆟 𓆞 𓆝 𓆟𓇼

text = """
[Куплет 1]  
В истерике кружилась мама Валя  
На заднем фоне замер папа Толя  
В радиусе метра воцарился жесточайший хаос  
Когда всем понятно стало: сын остался без диплома  
Мама, не кричи, хватит плакать, не смей      
Я не спорю — надо, но послушай отец:  
Есть у меня своя волна, и на своей волне  
Меня где-то поджидает успех  

[Предприпев]      
Боже, как хотел я увидеть свет  
И, как посчитал бы нужным жить, мечтал  
И вот однажды, как обычно, я летал во сне  
Вдруг увидел солнце — и тогда себе я сказал:  

[Припев]  
Я выбираю — жить в кайф!    
Я выбираю — жить в кайф!
Я выбираю — жить в кайф!       
Я выбираю — жить в кайф!

[Куплет 2]  
Это был сон, в котором я
Не прогорал, не огорчал родных и не нуждался ни в чём
В котором мне не пришлось скрывать глаза       
И лгать давним знакомым: мол, в жизни моей всё хорошо  
В моём рюкзаке пару маек, носки     
И пускай начало оставляет желать лучшего        
Все, кто меня помнит — знает, я не был таким  
А значит, и у вас получится     

[Предприпев]  
Ведь всё, что я хотел, это видеть свет  
И, как посчитал бы нужным жить, мечтал  
И вот однажды, как обычно, я летал во сне         
Вдруг услышав музыку — я сам себе сказал:  

[Припев]  
Я выбираю — жить в кайф!    
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!      
Я выбираю — жить в кайф!      

[Предприпев]  
Боже, как хотел я увидеть свет  
И, как посчитал бы нужным жить, мечтал  
И вот однажды, как обычно, я летал во сне             
Вдруг увидел солнце — и тогда себе я сказал:  

[Припев]  
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!         
Я выбираю — жить в кайф!
"""

# Your code here 𓆉𓆝 𓆟 𓆞 𓆝 𓆟𓇼


dict_ = dict()
ls = text.split("\n")
ls_num = []
for i in range(len(ls)):
    try:
        if ls[i][0] == '[':
            ls_num.append(i)
    except:
        pass
# разбитие песни на блоки
dif_name = 1
for i in range(len(ls_num)):
    try:
        if ls[ls_num[i]][1: ls[ls_num[i]].index(']')].lower() not in dict_:
            dict_[ls[ls_num[i]][1: ls[ls_num[i]].index(']')].lower()] = '\n'.join(ls[ls_num[i] + 1: ls_num[i + 1]])
        else:
            if dict_[ls[ls_num[i]][1: ls[ls_num[i]].index(']')].lower()].split() != '\n'.join(
                    ls[ls_num[i] + 1: ls_num[i + 1]]).split():
                for _ in range(2):
                    dict_[ls[ls_num[i]][1: ls[ls_num[i]].index(']')].lower() + ' ' + str(dif_name)] = '\n'.join(
                        ls[ls_num[i] + 1: ls_num[i + 1]])
                    dif_name += 1
    except:
        pass
# выбор подпункта
inp = input("Задание: ")
if inp == '1':
    inp = input("1: ")
    print(dict_[inp])

elif inp == '2':
    max_len = max(len(i) for i in ls)
    for i in ls:
        try:
            if i[0] != '[':
                print(i.center(max_len))
        except:
            print(i.center(max_len))

elif inp == '3':
    # обработка (удаление лишних знаков)
    er = ['!', ' —', '.', ':', ',']
    for i in er:
        text = text.replace(i, '')
        for z in dict_:
            dict_[z] = dict_[z].replace(i, '')
    text = text.lower().split()

    # выбор того что хотим делать
    inp = input("что-то: ")
    set_sing = set()
    if inp == 'песня':
        # уникальные слова в песне
        for i in dict_:
            set_sing |= set(dict_[i].lower().split())
    # уникальные слова в куплете
    elif inp == 'куплет':
        text = []
        for i in dict_:
            if 'куплет' in i:
                set_sing |= set(dict_[i].lower().split())
                text += dict_[i].lower().split()

    # подсчёт слов
    dict__ = dict()
    for i in set_sing:  # dict__ = {i : text.count(i)  for i in set_sing}
        count = 0
        for z in text:
            if z == i:
                count += 1
        dict__[i] = count
    # вывод слов
    for _ in range(3):
        m_v = max(dict__.values())
        for i in dict__:
            if dict__[i] == m_v:
                m_key = i
        print(f'\"{m_key}\" - {m_v} раз')
        dict__[m_key] = -1