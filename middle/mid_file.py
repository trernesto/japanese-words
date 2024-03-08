from back.data import words_by_lesson
from back.data import words_by_lessons
from back.data import Data
import eel

data = Data()

@eel.expose
def hello():
	print("hello world!")

@eel.expose
def words_by_lesson_py(lesson:str) -> None:
	#return words_by_lesson(lesson)
	print(words_by_lesson(lesson))

@eel.expose
def words_by_lessons_py(lessons:list) -> None:
	#return words_by_lessons(lessons)
	data.generateWords(lessons)
	#word, kanji, translate
	words = data.nextWord()
	eel.showWord(words[0], words[1], words[2])

@eel.expose
def nextWord() -> None:
	words = data.nextWord()
	eel.showWord(words[0], words[1], words[2])

@eel.expose
def prevWord() -> None:
	words = data.prevWord()
	eel.showWord(words[0], words[1], words[2])