import sys


def start(args=sys.argv) -> None:
	"""Prints Hello"""
	print(f'Hello, {args[-1]}!')
