from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='init_template',
      version='0.0.2',
      url='https://github.com/EliasOlie/init-template',
      license='MIT License',
      author='Elias Olie',
      long_description=readme,
      long_description_content_type="text/markdown",
      author_email='contato.eliasolie@gmail.com',
      keywords='Pacote',
      description=u'Criador de templates para novos projetos',
      packages=['init_template'],
      install_requires=['click'],)
