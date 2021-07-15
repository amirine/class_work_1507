import sys
import settings


def start(args=sys.argv) -> None:
	"""Prints Hello"""
	if args[1] == settings.admin.get('login') and \
	   args[2] == settings.admin.get('password'):
		print(f'You entered!')
	else:
		print(f'Wrong input!')
