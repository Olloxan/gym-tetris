from setuptools import setup, find_packages


def README() -> str:
    """Return the contents of the README file for this project."""
    with open('README.md') as README_file:
        return README_file.read()


setup(
    name='gym_tetris',
    setup_requires=[
        'setuptools-git-version'
    ],
    version_format='{tag}',
    description='Tetris for OpenAI Gym',
    long_description=README(),
    long_description_content_type='text/markdown',
    keywords='OpenAI-Gym Tetris Reinforcement-Learning-Environment',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    url='https://github.com/Kautenja/gym-tetris',
    author='Christian Kauten',
    author_email='kautencreations@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'gym>=0.10.5',
        'Pillow>=5.0.0',
        'numpy>=1.14.2'
    ],
)