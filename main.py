import argparse
import random

from bs4 import BeautifulSoup
from googletrans import Translator
import requests
from tqdm import tqdm


SENTENCE_PROVIDER_WEBSITE = "https://tw.ichacha.net/zaoju/"
REQUEST_SUCCESS_HTML_ID = "sentTabbox"
FOUL_SUBSTRINGS = ["這是一個萬能造句的方法", "更多例句"]
END_CHARS = ["。", "？", "！"]
DEFAULT_END_CHAR = "。"
REPLACE_CHARS = {"“": "「", "”": "」"}
BLANK_WORD_UNDERSCORE = "_____________"
BLANK_CHAR_UNDERSCORE = "____"
GROUP_SEPARATOR = "*************************************************************"
WORD_SEPARATOR = "   "
INDENTION = "  "
NUM_ALT_SENTENCES = 5


def _search_sentences(word):
    # Use website service
    response = requests.get(SENTENCE_PROVIDER_WEBSITE + word + ".html")
    if response.status_code != 200:
        raise f"Sentence provider website ({SENTENCE_PROVIDER_WEBSITE}) is not ready!"

    html_doc = response.text
    soup = BeautifulSoup(html_doc, "html.parser")

    # Check if any sentence is found
    sentences_div = soup.find(id=REQUEST_SUCCESS_HTML_ID)
    if sentences_div is None:
        return []

    # Filter and prettify
    sentences_lis = sentences_div.find_all("li")
    sentences = []
    for sentence_li in sentences_lis:
        sentence = sentence_li.get_text()

        found_foul_substring = False
        for foul_substring in FOUL_SUBSTRINGS:
            if sentence.find(foul_substring) != -1:
                found_foul_substring = True
        
        if found_foul_substring:
            continue
        
        if sentence[-1] not in END_CHARS:
            sentence += DEFAULT_END_CHAR

        for key in REPLACE_CHARS:
            sentence = sentence.replace(key, REPLACE_CHARS[key])

        sentences.append(sentence)

    # Sort by length (longer sentence is often better)
    sentences = sorted(sentences, key=len, reverse=True)

    return sentences


def _simchi_to_trachi(string):
    translator = Translator()
    translation = translator.translate(string, src="zh-CN", dest="zh-TW")
    return translation.text


def _write_questions(word_sentences_list, args):
    with open(args["questions_file"], "w") as f:
        f.write("選詞填充：選出適當的詞語，填在____上。\n\n\n")
        
        groups = [word_sentences_list[i : i + args["questions_per_group"]] for i in range(0, len(word_sentences_list), args["questions_per_group"])]

        for group in groups:
            f.write(GROUP_SEPARATOR + "\n")

            if not args["fill_char_mode"]:
                for word_sentences in group:
                    f.write(word_sentences["word"] + WORD_SEPARATOR)
                f.write("\n")
                f.write(GROUP_SEPARATOR + "\n")

            f.write("\n")

            for i, word_sentences in enumerate(group):
                f.write(str(i + 1) + ".  ")

                word = word_sentences["word"]
                hide_index = word_sentences["hide_index"]
                sentences = word_sentences["sentences"]

                if len(sentences) > 0:
                    sentence = sentences[0]  # take the longest sentence

                    if args["fill_char_mode"]:
                        char_to_hide = word[hide_index]
                        char_hiden_word = word.replace(char_to_hide, BLANK_CHAR_UNDERSCORE)
                        sentence = sentence.replace(word, char_hiden_word)
                    else:
                        sentence = sentence.replace(word, BLANK_WORD_UNDERSCORE)
                else:
                    sentence = "（無）"
                
                f.write(sentence + "\n\n")
            
            f.write("\n")


def _write_alt_questions(word_sentences_list, args):
    with open(args["alt_questions_file"], "w") as f:
        f.write("【選詞填充其他參考句子】\n\n\n")

        groups = [word_sentences_list[i : i + args["questions_per_group"]] for i in range(0, len(word_sentences_list), args["questions_per_group"])]

        for group in groups:
            f.write(GROUP_SEPARATOR + "\n")

            for i, word_sentences in enumerate(group):
                f.write(str(i + 1) + ".  ")

                word = word_sentences["word"]
                hide_index = word_sentences["hide_index"]
                sentences = word_sentences["sentences"]

                f.write(word + "\n")

                if len(sentences) > 0:
                    sentences.pop(0)  # item 0 has been selected as the question
                    for sentence in sentences[:NUM_ALT_SENTENCES]:
                        if args["fill_char_mode"]:
                            char_to_hide = word[hide_index]
                            char_hiden_word = word.replace(char_to_hide, BLANK_CHAR_UNDERSCORE)
                            sentence = sentence.replace(word, char_hiden_word)
                        else:
                            sentence = sentence.replace(word, BLANK_WORD_UNDERSCORE)
                        
                        f.write(INDENTION + sentence + "\n")
                else:
                    f.write(INDENTION + "（無）\n")


def _write_answers(word_sentences_list, args):
    with open(args["answers_file"], "w") as f:
        f.write("【選詞填充答案】\n\n\n")

        groups = [word_sentences_list[i : i + args["questions_per_group"]] for i in range(0, len(word_sentences_list), args["questions_per_group"])]

        for group in groups:
            f.write(GROUP_SEPARATOR + "\n")

            for i, word_sentences in enumerate(group):
                f.write(str(i + 1) + ".  " + word_sentences["word"] + "\n")


def _generate_exercises(args):
    with open(args["words_file"], "r") as f:
        lines = f.readlines()

    results = []  # e.g. [{"word": "風餐露宿", "hide_index": 1, "sentences": ["有些人在外面風餐露宿完全是出於自願。", "他們是美國市中心的一個常見現象：無家可歸的人，風餐露宿。", ...]}, ...]

    for line in lines:
        line = line.strip()
        splitted = line.split(",")
        if len(splitted) == 2:
            word, hide_index = splitted[0], int(splitted[1])
        else:
            word, hide_index = line, None
        
        results.append({"word": word, "hide_index": hide_index})

    for i in tqdm(range(0, len(results))):
        word = results[i]["word"]
        sentences = _search_sentences(word)
        sentences = [_simchi_to_trachi(s) for s in sentences]
        results[i]["sentences"] = sentences

    random.shuffle(results)

    _write_questions(results, args)
    _write_alt_questions(results, args)
    _write_answers(results, args)


def _get_parser():
    parser = argparse.ArgumentParser(description="Sentence making exercises generator")
    parser.add_argument("words_file", help="input words file path")
    parser.add_argument("questions_file", help="output exercise questions file path")
    parser.add_argument("alt_questions_file", help="output exercise alternative questions file path")
    parser.add_argument("answers_file", help="output exercise answers file path")
    parser.add_argument("--fill_char_mode", action="store_true", help="Fill in a charactor within a word, instead of fill in a word")
    parser.add_argument("--questions_per_group", type=int, default=10, help="number of questions per group")
    return parser


if __name__ == "__main__":
    parser = _get_parser()
    args = vars(parser.parse_args())
    
    _generate_exercises(args)