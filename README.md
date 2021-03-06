# Fill-in-the-blanks Exercises Generator

Take a list of words and generate fill-in-the-blanks exercises. The target language is Traditional Chinese.

This generator works by using the sentence provider website [查查造句詞典](https://tw.ichacha.net/zaoju/) to search sentences.


## Get started

```bash
git clone [URL of this repository]
cd fill-in-the-blanks-exercises

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install requests beautifulsoup4 tqdm
```

## Run

### Fill words mode

```bash
python main.py ./words.txt ./questions.txt ./alt_questions.txt ./answers.txt
```
* ```./words.txt``` is an input file which you need to provide. You may self-define the file's path and name. For the file content, see below example.
* ```./questions.txt```, ```./alt_questions.txt``` and ```./answers.txt``` are output files. You may also self-define the files' path and name.
* There are optional arguments. You may check with ```python main.py -h```

The input ```words.txt``` looks like:
```
風餐露宿
沉重
步伐
不堪負荷
溶化
失足
幾乎
自作聰明
滿頭大汗
教訓
```

The output ```questions.txt``` looks like:
```
【題目】


**********************************************************************************
溶化   滿頭大汗   風餐露宿   步伐   失足   
**********************************************************************************

1.  作為清除紡織業廢水水流中的不易_____________學成份的一種手段，更應研究廢水處理的電解方法。

2.  活動項目琳瑯滿目，在花園之間有戶外巴比區，許多外來游客見到素食烤料竟如此豐富味美，紛紛詢問并向服務臺采購在沙灘上許多小同修興高采烈的堆沙堡或將身子泡在海面上隨海波晃漾，不亦樂乎同修準備的沙灘活動也讓叁加者玩得_____________，比賽者與啦啦隊皆卯足了勁，盡興忘我。

3.  王冕一路_____________，九十里大站、七十里小站，一徑來到山東濟南府地方。

4.  孩子們又累又餓，拖著沉重的_____________高高興興地回家了。

5.  他們養成了一種謹慎小心的習慣，「只怕自己_____________」，這樣就使一個自由的生活成為不可能。


**********************************************************************************
教訓   不堪負荷   自作聰明   沉重   幾乎   
**********************************************************************************

1.  過去的魯莽的行動已經給了我_____________。

2.  （無）

3.  杰姆身上除了最近出現的怪脾氣外，還添上了一副叫人受不了的_____________的派頭。

4.  這些問題使他的負擔極其_____________。

5.  _____________所有的燈火已經熄滅。
```
* ```（無）``` means no question can be generated. This is because the sentence provider website does not have the resource.

The output ```alt_questions.txt``` stores alternative questions, which may be used to replace some of the default questions in ```questions.txt``` in case the question quality is unsatisfactory. The file ```alt_questions.txt``` looks like:
```
【可用作替換的句子】


**********************************************************************************

1.  溶化
  在這些奇異而迷人的紫、紅、黃三種顏色的花朵面前，不友好的感情_____________了。
  他的臉突然發黑，臉上五官好像_____________了，又好像在變形。
  此心軸_____________之后，在推進劑表面上留有一薄層的合金。
  生活就象一支冰淇淋，在它_____________之前盡情享受吧。
  通過交替的凍結、抽空和_____________來使溶液除氣。

2.  滿頭大汗
  下午的節目則是更激烈的有氧舞蹈，在師姊的指導下，又讓我度過一個_____________的下午，盡管全身的肌肉都在向我抗議，但是我真的好高興可以跟這么多同修一起跳有氧舞蹈。
  正如我們前面所說的，馬車已等在門口。四匹強壯的馬在不耐煩地蹬踏著地面，在臺階前，站著那_____________的阿里，他顯然剛趕了大路回來。
  一個人，帶他太太去看電影，那天剛好是禮拜天，戲院人山人海，大家都在排隊買票，他和他太太也跟著排隊，等得_____________。
  當得知天衣到達的消息，一位師兄來不及把下地的鋤頭帶回家，就騎車趕了30里路而來，進門時已是_____________。
  等到達目的地，倆人已經熱得_____________，氣喘吁吁，于是往就近的榆樹下面一躺，歇歇腳，抽袋煙。

3.  風餐露宿
  他們是美國市中心的一個常見現象：無家可歸的人，_____________。
  有些人在外面_____________完全是出于自愿。

4.  步伐
  最后，他用一種端莊的_____________走到窗子所在的地方。
  它保持著_____________，沿著多少里密扎扎的人群前進。
  你如果想在吃晚飯前趕到家，就得加快_____________。
  他的同伴卻默默地踏著輕松的_____________跟在后面。
  他向她彎下腰，打量著他們踱來踱去的_____________。

5.  失足
  「那么你就是使我妹妹_____________的壞東西了？」珍妮說，理所當然地帶著憤怒的口吻。
  他把這件發生在身上的事作為一樁不幸的落入政治上的異國情調的_____________來談論。
  他激她跳過一個很寬的峽谷，如果她_____________的話，可能會受重傷或送命。
  一_____________成千古恨--永生永世也抹不掉。
  「拯救_____________基督徒的羽絨墊」有了發展。

**********************************************************************************

1.  教訓
  您幾時看到過我違背了您的_____________？
  這一_____________深深影響了我的性格。
  你再管我的事我就要_____________你了。
  你目前還沒有接受_____________的意思。
  明眼人可從中記取寶貴的_____________。

2.  不堪負荷
  （無）

3.  自作聰明
  雖然你們這些_____________的美國人呃我想你們這些家伙叫。
  他總是_____________，因此我們都認為他受罰是自找的。
  但是克利福比他顯得淺薄無聊得多，_____________得多！
  嗨，我剛剛怎么和你說的？不要做_____________的人。
  他真正需要的就是當他在說_____________的臺詞時。

4.  沉重
  她丈夫一死她受到_____________的打擊。
  他在抬_____________的家具時扭傷了腰。
  那只鵝扇著_____________的翅膀飛走了。
  交稅成了我們大家的_____________負擔。
  那個問題_____________地壓在他的心頭。

5.  幾乎
  她的頭發_____________垂到了腰部。
  我們_____________讓浪頭給打倒了。
  她_____________幾分鐘都支持不住。
  我_____________已不再認真考慮她。
  他_____________象父親一樣愛護潘。
```

The output ```answers.txt``` looks like:
```
【答案】


**********************************************************************************

1.  溶化
2.  滿頭大汗
3.  風餐露宿
4.  步伐
5.  失足

**********************************************************************************

1.  教訓
2.  不堪負荷
3.  自作聰明
4.  沉重
5.  幾乎
```

### Fill charactors mode

```bash
python main.py ./words.csv ./questions.txt ./alt_questions.txt ./answers.txt --fill_char_mode
```
* Note the ```--fill_char_mode``` at the end.
* In this mode, an exercise question asks to fill in a single character within a word within a sentence, and there is no pool of words provided.

The input ```words.csv``` looks like:
```
風餐露宿,1
沉重,0
步伐,1
不堪負荷,3
溶化,0
失足,1
幾乎,0
自作聰明,2
滿頭大汗,1
教訓,1
```
* The number after a word is the index (starting from 0) of the character to be hidden in the generated question.

The output ```questions.txt``` looks like:
```
【題目】


**********************************************************************************

1.  他們養成了一種謹慎小心的習慣，「只怕自己失____」，這樣就使一個自由的生活成為不可能。

2.  王冕一路風____露宿，九十里大站、七十里小站，一徑來到山東濟南府地方。

3.  （無）

4.  過去的魯莽的行動已經給了我教____。

5.  杰姆身上除了最近出現的怪脾氣外，還添上了一副叫人受不了的自作____明的派頭。


**********************************************************************************

1.  這些問題使他的負擔極其____重。

2.  活動項目琳瑯滿目，在花園之間有戶外巴比區，許多外來游客見到素食烤料竟如此豐富味美，紛紛詢問并向服務臺采購在沙灘上許多小同修興高采烈的堆沙堡或將身子泡在海面上隨海波晃漾，不亦樂乎同修準備的沙灘活動也讓叁加者玩得滿____大汗，比賽者與啦啦隊皆卯足了勁，盡興忘我。

3.  作為清除紡織業廢水水流中的不易____化學成份的一種手段，更應研究廢水處理的電解方法。

4.  孩子們又累又餓，拖著沉重的步____高高興興地回家了。

5.  ____乎所有的燈火已經熄滅。
```

The other output files ```alt_questions.txt``` and ```answers.txt``` are simlar to those in the standard mode.