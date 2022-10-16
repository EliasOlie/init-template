#!/usr/bin/env python3
import os
import click
import json

ROOT = os.path.dirname(__file__)

EXEC_PATH = os.getcwd()
TEMPLATE_REPO = "https://github.com/EliasOlie/ts-setup.git"

try:
    with open(f"{ROOT}/user_settings.json", "rb") as json_file:
        jf = json.load(json_file)
    DEFAULT_USER_TEMPLATE = jf["default_template"]
    DEFAULT_LANGUAGE = jf["default_language"]
except:
    click.echo(click.style("Parece que você ainda não configurou suas predefinições padrão, usaremos as nossas ;)", fg="yellow"))

TEMPLATES = [
    
    {"@EliasOlie/typescript": "https://github.com/EliasOlie/ts-setup.git"},
]

PATH_HELP_MESSAGE = """
(pt-BT) O caminho onde você deseja criar o projeto.

EX ".", "./repo"

"""

TEMPLATE_HELP_MESSAGE = """
(pt-BR) Qual template você deseja, o valor padrão é um projeto minimalista de TS
"""


@click.group()
def cli():
    pass


@cli.command()
@click.option("--language", "-l", prompt=True)
@click.option("--default-template", "-dt", prompt=True)
def setup(language, default_template):
    if os.path.exists(f"{ROOT}/user_settings.json"):
        with open(f"{ROOT}/user_settings.json", "rb") as json_file:
            jf = json.load(json_file)
            user_defalt_language = jf["default_language"]
            user_default_template = jf["default_template"]
            click.echo(click.style(
                f"Você já configurou as opções da seguinte maneira:\nIdioma padrão: {user_defalt_language}\nTemplate padrão: {user_default_template}\n\nPara alterar use a opção \"config\"", fg="yellow"))
    else:
        with open(f"{ROOT}/user_settings.json", "w+") as json_file:
            json.dump({"default_template": default_template,
                      "default_language": language}, json_file)

        click.echo(click.style("Configurações salvas!", fg="green"))


@cli.command()
@click.option("--language", "-l", prompt=True)
@click.option("--default-template", "-dt", prompt=True)
def config(language, default_template):
    if os.path.exists(f"{ROOT}/user_settings.json"):
        with open(f"{ROOT}/user_settings.json", "w+") as json_file:
            json.dump({"default_template": default_template,
                      "default_language": language}, json_file)

        click.echo(click.style("Configurações salvas!", fg="green"))
    else:
        click.echo(click.style(
            "Você ainda não configurou suas opções padrões, use \"setup\" para configurar", fg="red"))

@cli.command()
@click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
@click.option("--template", "-t", help=TEMPLATE_HELP_MESSAGE)
def setup_no_git(path, template):
    if template is None:
        selected_template = map(lambda x: x.get(DEFAULT_USER_TEMPLATE), TEMPLATES)
        template = [i for i in list(selected_template) if i is not None][0]
    else:
        selected_template = map(lambda x: x.get(template), TEMPLATES)
        template = [i for i in list(selected_template) if i is not None][0]


    click.echo(click.style("Inicializando...", fg="blue"))

    os.system(f"git clone {template} {path}")

    os.system("rm -rf ./.git")
    click.echo(click.style("Feito", fg="green"))


@cli.command()
@click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
@click.option("--template", "-t", help=TEMPLATE_HELP_MESSAGE)
def setup_git(path, template):
    if template is None:
        selected_template = map(lambda x: x.get(DEFAULT_USER_TEMPLATE), TEMPLATES)
        template = [i for i in list(selected_template) if i is not None][0]
    else:
        selected_template = map(lambda x: x.get(template), TEMPLATES)
        template = [i for i in list(selected_template) if i is not None][0]
    
    click.echo(click.style("Inicializando...", fg="blue"))

    os.system(f"git clone {template} {path}")

    click.echo(click.style("Preparando repositório", fg="yellow"))
    os.system("rm -rf ./.git")
    os.system("git init")

    click.echo(click.style("Feito", fg="green"))


@cli.command()
@click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
@click.option("--template", "-t", help=TEMPLATE_HELP_MESSAGE)
@click.option("--remote-origin", "--origin", prompt=True)
def setup_git_origin(path, template, remote_origin):
    if template is None:
        selected_template = map(lambda x: x.get(DEFAULT_USER_TEMPLATE), TEMPLATES)
        template = [i for i in list(selected_template) if i is not None][0]
    else:
        selected_template = map(lambda x: x.get(template), TEMPLATES)
        template = [i for i in list(selected_template) if i is not None][0]

    click.echo(click.style("Inicializando...", fg="blue"))

    os.system(f"git clone {template} {path}")

    click.echo(click.style("Preparando repositório", fg="yellow"))
    os.system("rm -rf ./.git")
    os.system("git init")
    click.echo(click.style("Adicionando origem remota", fg="yellow"))
    os.system(f"git remote add origin {remote_origin}")
    click.echo(click.style("Feito", fg="green"))


# @cli.command()
# @click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
# @click.option("--template", "-t", default=TEMPLATE_REPO, help=TEMPLATE_HELP_MESSAGE)
# def setup_no_git(path, template):
#     click.echo(click.style("Inicializando...", fg="blue"))

#     os.system(f"git clone {template} {path}")

#     os.system("rm -rf ./.git")
#     click.echo(click.style("Feito", fg="green"))


# @cli.command()
# @click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
# @click.option("--template", "-t", default=TEMPLATE_REPO, help=TEMPLATE_HELP_MESSAGE)
# def setup_git(path, template):
#     click.echo(click.style("Inicializando...", fg="blue"))

#     os.system(f"git clone {template} {path}")

#     click.echo(click.style("Preparando repositório", fg="yellow"))
#     os.system("rm -rf ./.git")
#     os.system("git init")

#     click.echo(click.style("Feito", fg="green"))


# @cli.command()
# @click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
# @click.option("--template", "-t", default=TEMPLATE_REPO, help=TEMPLATE_HELP_MESSAGE)
# @click.option("--remote-origin", "--origin", prompt=True)
# def setup_git_origin(path, template, remote_origin):
#     click.echo(click.style("Inicializando...", fg="blue"))

#     os.system(f"git clone {template} {path}")

#     click.echo(click.style("Preparando repositório", fg="yellow"))
#     os.system("rm -rf ./.git")
#     os.system("git init")
#     click.echo(click.style("Adicionando origem remota", fg="yellow"))
#     os.system(f"git remote add origin {remote_origin}")
#     click.echo(click.style("Feito", fg="green"))


if __name__ == '__main__':
    cli()
