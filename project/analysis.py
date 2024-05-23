# -*- coding: cp1251 -*-
# new
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import numpy as np


def full_word_cloud(df):
    full_wc = " ".join(df.sample(n=df.shape[0])["Title_ru"].str.lower()) # ðàíäîìíàÿ ïåðåñòàíîâêà ñëîâ
    plt.figure(figsize=(19.2, 10.8))

    to_remove = ['íà ', 'äëÿ ', 'è ', 'â ', 'ñ ', 'íàä ', 'ïîä ', 'áåç ', 'êðîìå ', 'ïðè ', 'ïî ', 'î ', '.', ',', ':', ';']
    for strs in to_remove:
        full_wc = full_wc.replace(strs, '') # óáèðàþ ïðåäëîãè

    wc = WordCloud(background_color="black", stopwords=STOPWORDS, max_words=2000,max_font_size=300, width=1920, height=1080)
    wc.generate(full_wc) # ãåíåðèðóþ ìàêñèìóì 2000 ñëîâ (äëÿ ýòîãî è áûëà ïåðåñòàíîâêà, ïîâûøàåì òî÷íîñòü)
    plt.imshow(wc.recolor(colormap= 'viridis' , random_state=17), interpolation="bilinear")
    plt.axis('off')
    plt.savefig("full_word_cloud.png")


def wc_by(df, arr, what):
    df_per = df.sample(n=df.shape[0])
    for v in arr:
        mask = df_per[what] == v
        full_wc = " ".join(df_per[mask]["Title_ru"].str.lower()) # ðàíäîìíàÿ ïåðåñòàíîâêà ñëîâ
        plt.figure(figsize=(19.2, 10.8))

        to_remove = ['íà ', 'äëÿ ', 'è ', 'â ', 'ñ ', 'íàä ', 'ïîä ', 'áåç ', 'êðîìå ', 'ïðè ', 'ïî ', 'î ', '.', ',', ':', ';']
        for strs in to_remove:
            full_wc = full_wc.replace(strs, '') # óáèðàþ ïðåäëîãè

        wc = WordCloud(background_color="black", stopwords=STOPWORDS, max_words=2000,max_font_size=300, width=1920, height=1080)
        wc.generate(full_wc) # ãåíåðèðóþ ìàêñèìóì 2000 ñëîâ (äëÿ ýòîãî è áûëà ïåðåñòàíîâêà, ïîâûøàåì òî÷íîñòü)
        plt.imshow(wc.recolor(colormap= 'viridis' , random_state=17), interpolation="bilinear")
        plt.axis('off')
        plt.savefig(v.replace(" ", "_") + ".png")


def most_com(df, arr, what, fileG):
    fig, axs = plt.subplots(len(arr), figsize=(19.2, 10.8))
    index = 0
    for v in arr:
        lst = " ".join(df[df[what] == v]['Title_ru'].str.lower()).split()
        total = len(lst)
        stat = Counter(lst).most_common(15)
        x_one = np.array([x for x, y in stat])
        y_one = np.array([y for x, y in stat])
        to_remove = ['íà', 'äëÿ', 'è', 'â', 'ñ', 'íàä', 'ïîä', 'áåç', 'êðîìå', 'ïðè', 'ïî', 'î', '.', ',', ':', ';']
        for rm in to_remove:
            tmp = np.argwhere(x_one == rm)
            x_one = np.delete(x_one, tmp);
            y_one = np.delete(y_one, tmp);
        axs[index].bar(x_one, (y_one / total) * 100) 
        axs[index].set_title(v)
        axs[index].set_yticks(np.arange(0, np.max(y_one / total) * 100, 0.2))
        axs[index].set_ylabel('% from total words')
        index += 1
    fig.tight_layout()
    plt.savefig(fileG)
    

def by_topics(df, dictV, arr, what, fileG):
    plt.figure(figsize=(19.2, 10.8))
    nums = []
    for v in arr:
        mask = df[what] == v
        lst = df[mask]['Title_ru'].to_list()
        lst = [x.lower() for x in lst]
        num = 0
        for el in lst:
            if any(x in el for x in dictV):
                num += 1
        nums.append((num / len(lst)) * 100)
    plt.title(dictV[0])
    plt.ylabel('% from total topics')
    plt.bar(arr, nums)
    plt.savefig(fileG)


def checkLetters(df):
    lst_letters_name = df['Student'].to_list()
    lst_letters_name = [len(x.replace(' ', '')) for x in lst_letters_name]
    lst_letters_topic = df['Title_ru'].to_list()
    lst_letters_topic = [len(x.replace(' ', '')) for x in lst_letters_topic]
    count = 0
    for i in range(len(lst_letters_name)):
        if lst_letters_name[i] == lst_letters_topic[i]:
            count += 1

    return count
    
        

df = pd.read_excel("data.xlsx")

faculties = ["Ìàòåìàòèêà è ìåõàíèêà", "Ïðîöåññû óïðàâëåíèÿ", "Ìàòåìàòèêà è êîìïüþòåðíûå íàóêè"]
positions = ["äîöåíò", "ïðîôåññîð", "àññèñòåíò"]
years = ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
level = ['áàêàëàâðèàò', 'ìàãèñòðàòóðà']
advisors1 = ['Ïîãîæåâ Ñåðãåé Âëàäèìèðîâè÷', 'Ïëàòîíîâ Àëåêñåé Âèêòîðîâè÷']
advisors2 = ['Ïîòîöêàÿ Èðèíà Þðüåâíà', 'Ìàòðîñîâ Àëåêñàíäð Âàñèëüåâè÷', 'Áàëûêèíà Þëèÿ Åôèìîâíà']

ML_dict = ['ìàøèííîå îáó÷åíèå', 'ìàøèí', 'îáó÷', 'íåéðî', 'íåéðîñåò', 
          'ãëóáîê', 'ðåãðåñ', '3d', 'èçîáðàæ', 'áèîìåòð', 'ñâåðòî÷', "ñâ¸ðòî÷"
          'ñâåðòê','èíòåëëåêò', 'àíàëèç', 'äàííû', 'èè', 'âåñ', 'îáðàáîòê', 
          'åñòñòâåíí', 'llm', 'ÿçûê', 'ðåêóððåíò', 'ðàçìåðí', 'êëàññèôèêàö', 
          'ïàðàìåòð', ' ïîòåð', 'ïîãðåøíîñò', 'ïðèçíàê', 'ðåãóëÿðèçàö', 'àãåíò', "âûáîðê", 'äàòàñåò'
          'ðàñïîçí', ' ëèö', "òðàíñôîðìåð", "ïðåäñêàçàí", "äàòà"]

NM_dict = ['÷èñëåííûå ìåòîäû', 'äèôôåðåíö', 'óðàâíåí', 'ïðîèçâîäí',
          'èíòåãð', 'ñòîõàñòè÷åñê', 'ñòîõàñòè÷', '÷èñëåíí', 'ãðàäèåíò', 'ïîãðåøíîñò', 
          'îïòèìàëüí', 'îïòèìèçàö', 'ðóíãå', 'êóòòû', 'îïðåäåëåí', 'óñòîé÷èâ', 'ëèíåéí', 
          'ñïóñê', 'ìàòðèö', 'ñîáñòâåí', 'èíòåðïîëÿö', 'òðàíñöåíäåíò', "ðàçëîæåí", 
          "èòåðàöèîíí", "ðàçíîñòí", "àïïðîêñèìàö", "áèëèíåéí"]

GT_dict = ["òåîðèÿ èãð", "èãð", "íåø", "àóìàí", "çåëòåí", "íýø", "õàðñàíüè", "âèêðè", 
           "ìèððëèñ", "øåëëèíã", "àêåðëîô", "ñïåíñ", "ñòèãëèö", "ãóðâèö", "ó÷àñòíèê", 
           "íåîïðåäåëåííîñò", "íåîïðåäåë¸ííîñò", "èíòåðåñ", "âçàèìîñâÿçàííîñòü", "ïîâåäåí", 
           "ïðàâèë", "êîîïåðàòèâí", "êîàëèö", "ñòðàòåã", "ïîáåä", "âûèãðûø", "ïîðàæåí", 
           "êîíôðîíòàö", "äèëåìì", "çàêëþ÷åíí", "çàêëþ÷¸íí", "íåêîîïåðàòèâ", "ïðåñëåä", "ñèììåòðè÷í",
           "íåñèììåòðè÷", "øàãîâ", "ìàòàèãð", "ñòîõàñò", "øàõìàò", "ìàò÷èíã", "ñåòåâûå èãðû", "äèôôåðåíö",
           "àíòàãîíèñòè÷åñêèå", "øàã"]

df['Graduation'] = df['Graduation'].apply(str)
wc_by(df, faculties, "Faculty")
most_com(df, faculties, 'Faculty', "barchart.png")
wc_by(df, positions, "Position")
most_com(df, positions, "Position", "barchartPositions.png")
most_com(df, years, 'Graduation', "barchartGraduation.png")
most_com(df, level, 'Level', "barchartLevel.png")
most_com(df, advisors1, 'Advisor', "barchartAdvisor1.png")
most_com(df, advisors2, 'Advisor', "barchartAdvisor1.png")
by_topics(df, ML_dict, years, 'Graduation', 'MLbyYears.png')
by_topics(df, NM_dict, years, 'Graduation', 'NMbyYears.png')
by_topics(df, GT_dict, years, 'Graduation', 'GTbyYears.png')
by_topics(df, ML_dict, level, 'Level', 'MLbyLevel.png')
by_topics(df, NM_dict, level, 'Level', 'NMbyLevel.png')
by_topics(df, GT_dict, level, 'Level', 'GTbyLevel.png')
by_topics(df, ML_dict, faculties, 'Faculty', 'MLbyFaculty.png')
by_topics(df, NM_dict, faculties, 'Faculty', 'NMbyFaculty.png')
by_topics(df, GT_dict, faculties, 'Faculty', 'GTbyFaculty.png')
print(checkLetters(df))
