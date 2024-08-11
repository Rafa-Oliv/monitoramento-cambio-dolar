import sys
import os
from cx_Freeze import setup, Executable

#build_exe_options = {"packages": ["setuptools"]}

arquivos = ['dollar.ico']

config = Executable(
    script='app.py',
    icon='dollar.ico'
)

setup(
    name="Monitorador cotação Dollar",
    version="1.0",
    description="Monitora a cotação do dolar pelo Google",
    author="Rafael Ribeiro",
    options = {"build_exe": {"include_files": arquivos,}},
    executables=[config]
)
