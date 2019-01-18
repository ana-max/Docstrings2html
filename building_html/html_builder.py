import os
from jinja2 import Template
from building_html.finder import Finder
template_for_module = 'template/html/template_for_module.html'
template_for_table_of_content = 'template/html/' \
                                'template_for_table_of_content.html'
style_for_module = 'template/css/style_for_modules.css'
style_for_table_of_content = 'template/css/style_for_table_of_content.css'


class Builder:
    def __init__(self, directories_structure):
        self.directories_structure = directories_structure

    def get_all_information(self):
        self.information = dict()
        for directory in self.directories_structure:
            self.information[directory] = dict()
            for file in self.directories_structure[directory]:
                filename = file[file.index(directory)+len(directory)+1:]
                if not filename:
                    filename = directory
                self.information[directory]\
                    .update({filename: {'in_classes': list(),
                                        'out_classes': list()}})
                finder = Finder(file)
                three = finder.get_code_tree()
                for _ in three['in_classes']:
                    self.information[directory][filename]['in_classes']\
                        .append(_)
                for _ in three['out_classes']:
                    self.information[directory][filename]['out_classes']\
                        .append(_)

    def build_html(self):
        os.mkdir('documentation')
        os.mkdir('documentation/classes')
        self.get_all_information()
        self._write_stylies()
        self._build_table_of_content()
        self._build_modules()

    def _write_stylies(self):
        with open(style_for_table_of_content) as s:
            style = s.read()
        with open('documentation/style_for_table_of_content.css', 'w') as s:
            s.write(style)
        with open(style_for_module) as s:
            style = s.read()
        with open('documentation/classes/style_for_modules.css', 'w') as s:
            s.write(style)

    def _build_table_of_content(self):
        with open(template_for_table_of_content) as f:
            template = Template(f.read())
        data_of_module = dict()
        for directory in self.information:
            data_of_module[directory] = list()
            for file in self.information[directory]:
                new_name = file.replace('/', '.')
                new_name = new_name[:new_name.index('.py')]
                data_of_module[directory]\
                    .append(new_name+'.html')
        with open('documentation/docstrings.html', 'w',
                  encoding='utf-8') as f:
            f.write(template
                    .render(data=data_of_module))

    def _build_modules(self):
        with open(template_for_module) as f:
            template = Template(f.read())
        for directory in self.information:
            for file in self.information[directory]:
                new_name = file.replace('/', '.')
                new_name = new_name[:new_name.index('.py')]
                new_name = 'documentation/classes/' + new_name
                with open(new_name + '.html', 'w', encoding='utf-8') as f:
                    f.write(template
                            .render(data=self.information[directory][file],
                                    module_name=new_name))
