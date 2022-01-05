# Sentence Making Exercises Generator

Take a list of words and generate sentence making exercises.
Only Traditional Chinese is supported.


## Get started

```bash
git clone [URL of this repo]
cd sentence-making-exercises

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install requests googletrans==3.1.0a0 tqdm
```

## Run

Input:
* words.txt (text file containing list of words; one word per line)

Output:
* questions.txt (text file of the exercise questions)
* alt_questions.txt (text file containing the reference alternative questions for replacement)
* answers.txt (text file of the answers)

You may define your own file names.

Prepare ```words.txt``` then run:
```bash
python main.py path/to/words.txt path/to/questions.txt path/to/alt_questions.txt path/to/answers.txt
```