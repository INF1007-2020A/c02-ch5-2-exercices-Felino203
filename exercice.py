#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	num_letters = 0
	for chr in text:
		num_letters += int(chr.isalnum())
	return num_letters


	#return len([None for chr in text if chr.isalnum()])

def get_word_length_histogram(text):
	histogram = [0]
	for word in text.split():
		length = get_num_letters(word)
		if length >= len(histogram):
			histogram += [0] * (length - len(histogram) + 1)
		histogram[length] += int(length != 0)
	return histogram

def format_histogram(histogram):
	ROW_CHAR = "*"
	result = ""
	alinment = len(str(len(histogram) - 1))
	for i, element in enumerate(histogram):
		if i == 0:
			continue
		result += f"{i : >{alinment}} {ROW_CHAR * element}" + "\n"
	return result
	# result = [f"{i : >{alinment}} {ROW_CHAR * element}" + "\n" for i, element in enumerate(histogram) if i != 0]

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	height = max(histogram)
	result = ""
	for i in range(height - 1, -1, -1):
		for j, elem in enumerate(histogram):
			if j == 0:
				continue
			if elem >= i + 1:
				result += BLOCK_CHAR
			else:
				result += " "
		result += "\n"
	result += LINE_CHAR * (len(histogram))
	return result


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
