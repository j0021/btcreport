from setuptools import setup

progver="0.1.1"

setup(
    name="btcreport",
    version=progver,
    py_modules=["btcreport"],
    install_requires=[
        "btcget==0.0.*",
        "prettytable==3.9.0"
    ],
    entry_points={
        "console_scripts":[
            "btcreport=btcreport:main"
        ]
    }
)