import gspread
from random import shuffle
from functools import reduce

sa = gspread.service_account()
sh = sa.open("Test")
wks = sh.worksheet("Слова к урокам")

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


def words_by_lesson(lesson:str) -> list:
	to_return: list = []
	for elem in wks.get_all_values():
		if elem[3] == lesson:
			to_return.append([elem[0], elem[1], elem[2]])
	return to_return

def words_by_lessons(lessons:list) -> list:
	to_return: list = []
	for ind in lessons:
		to_return.append(words_by_lesson(ind))
	for elem in to_return:
		shuffle(elem)
	to_return = flatten_list(to_return)
	shuffle(to_return)
	return to_return

class Data(object):
	"""docstring for Data"""
	def __init__(self):
		super(Data, self).__init__()
		self.words = words_by_lessons([])
		self.index = 0

	def generateWords(self, lessons:list) -> None:
		self.index = 0
		self.words = words_by_lessons(lessons)

	def getWords(self) -> list:
		return self.words

	#starts with second word!!!
	def nextWord(self) -> list:
		self.index += 1
		return self.words[self.index % len(self.words)]

	def prevWord(self) -> list:
		self.index -= 1
		return self.words[self.index % len(self.words)]

		