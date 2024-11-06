from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pretty_mails/__init__.py
from pretty_mails import __version__ as version

setup(
	name="pretty_mails",
	version=version,
	description="Pretty Mails is a Frappe plugin that streamlines and optimizes your email templates by cleaning up and enhancing their styles using SCSS (Sassy CSS). Designed to simplify template management, this plugin converts complex inline CSS into well-organized SCSS, making your email designs cleaner, responsive, and more maintainable.",
	author="SVNIX Solutions",
	author_email="contact@svnix.solutions",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
