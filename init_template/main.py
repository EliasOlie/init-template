#!/usr/bin/env python3
import os
import click
import json
from messages import *

ROOT = os.path.dirname(__file__)

EXEC_PATH = os.getcwd()
TEMPLATE_REPO = "https://github.com/EliasOlie/ts-setup.git"
DEFAULT_LANGUAGE = "en-US"

try:
    with open(f"{ROOT}/user_settings.json", "rb") as json_file:
        jf = json.load(json_file)
    DEFAULT_USER_TEMPLATE = jf["default_template"]
    DEFAULT_LANGUAGE = jf["default_language"]
except (FileNotFoundError):
    click.echo(click.style(
        "Parece que você ainda não configurou suas predefinições padrão, usaremos as nossas ;)", fg="yellow"))


TEMPLATES = {
    "templates": [
        {"@EliasOlie/typescript": "https://github.com/EliasOlie/ts-setup.git"},
    ]
}

try:
    with open(f"{ROOT}/user_templates.json", "rb") as json_file:
        jf = json.load(json_file)
        TEMPLATES = jf["templates"]
except (FileNotFoundError):
    with open(f"{ROOT}/user_templates.json", "w+") as json_file:
        jf = json.dump(TEMPLATES, json_file)


@click.group()
def cli():
    ...


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
        with open(f"{ROOT}/user_settings.json", "w+") as json_file:
            json.dump({"default_template": default_template,
                      "default_language": language}, json_file)

        click.echo(click.style("Configurações salvas!", fg="green"))


@cli.command()
@click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
@click.option("--template", "-t", help=TEMPLATE_HELP_MESSAGE)
def setup_no_git(path, template):
    if template is None:
        with open(f"{ROOT}/user_settings.json", "rb") as json_file:
            template = json_file["default_template"]
    else:
        with open(f"{ROOT}/user_templates.json", "rb") as json_file:
            json_object = json.load(json_file)
            templates: list = json_object["templates"]
            for template_dict in templates:
                for key, value in template_dict.items():
                    if key == template:
                        template = value
                        break
                    else:
                        template = template
                        break
                break

    click.echo(click.style("Inicializando...", fg="blue"))

    os.system(f"git clone {template} {path}")
    os.system(f"cd ./{path}")

    os.system("rm -rf ./.git")
    click.echo(click.style("Feito", fg="green"))


@cli.command()
@click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
@click.option("--template", "-t", help=TEMPLATE_HELP_MESSAGE)
def setup_git(path, template):
    if template is None:
        with open(f"{ROOT}/user_settings.json", "rb") as json_file:
            template = json_file["default_template"]
    else:
        with open(f"{ROOT}/user_templates.json", "rb") as json_file:
            json_object = json.load(json_file)
            templates: list = json_object["templates"]
            for template_dict in templates:
                for key, value in template_dict.items():
                    if key == template:
                        template = value
                        break
                    else:
                        template = template
                        break
                break

        click.echo(click.style("Inicializando...", fg="blue"))

        os.system(f"git clone {template} {path}")

        click.echo(click.style("Preparando repositório", fg="yellow"))
        os.system(f"cd ./{path} && git init")

        click.echo(click.style("Feito", fg="green"))


@cli.command()
@click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
@click.option("--template", "-t", help=TEMPLATE_HELP_MESSAGE)
@click.option("--remote-origin", "--origin", prompt=True)
def setup_git_origin(path, template, remote_origin):
    if template is None:
        with open(f"{ROOT}/user_settings.json", "rb") as json_file:
            template = json_file["default_template"]
    else:
        with open(f"{ROOT}/user_templates.json", "rb") as json_file:
            json_object = json.load(json_file)
            templates: list = json_object["templates"]
            for template_dict in templates:
                for key, value in template_dict.items():
                    if key == template:
                        template = value
                        break
                    else:
                        template = template
                        break
                break

    click.echo(click.style("Inicializando...", fg="blue"))

    os.system(f"git clone {template} {path}")
    click.echo(click.style("Preparando repositório", fg="yellow"))
    os.system(f"cd./{path} && git init")
    click.echo(click.style("Adicionando origem remota", fg="yellow"))
    os.system(f"cd./{path} && git remote add origin {remote_origin}")
    click.echo(click.style("Feito", fg="green"))


@cli.command()
@click.option("--alias", "-a", help=ALIAS_HELP_MESSAGE)
@click.option("--template", "-t", help=TEMPLATE_HELP_MESSAGE)
def add_template(alias, template):
    if alias is None:
        click.echo(click.style(
            "Vocë precisa informar um alias para o repositário", fg="red"))
        return

    with open(f"{ROOT}/user_templates.json", "rb") as json_file:
        json_object = json.load(json_file)
        templates: list = json_object["templates"]
        templates.append({alias: template})
        with open(f"{ROOT}/user_templates.json", "w+") as json_file:
            json.dump({"templates": templates}, json_file)


@cli.command()
def list_templates():
    click.echo(click.style("Listando templates:", fg="blue"))
    with open(f"{ROOT}/user_templates.json", "rb") as json_file:
        json_object = json.load(json_file)
        templates: list = json_object["templates"]
        if templates == []:
            click.echo(click.style(
                "Vocë ainda não configurou nenhum template", fg="yellow"))
            return
        for template in templates:
            for key, value in template.items():
                click.echo(click.style(f"\t• {key}: {value}", fg="green"))


if __name__ == '__main__':
    cli()
