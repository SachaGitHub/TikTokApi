import setuptools



setuptools.setup(
    name="PyTikTokAPI",
    packages=setuptools.find_packages(),
    version="0.0.1",
    license='MIT',
    author="Sacha",
    description="Unofficial TikTok API in Python",
    long_description="no desc",
    long_description_content_type="text/markdown",
    url="https://github.com/SachaGitHub/TikTokApi",
    keywords=['tiktok', 'python', 'api', 'tiktok-api', 'tiktok api'],
    install_requires=[
        'requests',
        'bs4',
        "time",
        "json"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    include_package_data=True
)
