import os


class Parser:
    def __init__(self, names_of_files):
        self.names_of_files = names_of_files

    def get_directories_structure(self):
        structure = dict()
        for file in self.names_of_files:
            structure_of_file = self.get_all_files(file)
            pretty_name = file.split('/')[-1]
            structure[pretty_name] = structure_of_file
        return structure

    def get_all_files(self, file):
        files = list()
        if not os.path.exists(file):
            raise FileNotFoundError(f'{file} is not exist')
        if os.path.isdir(file):
            support_var = self._work_with_directory(file)
            for _ in support_var:
                if len(_) != 0:
                    files.append(_)
        elif file.endswith('.py'):
            files.append(file)
        return files

    def _work_with_directory(self, directory_name):
        files = os.listdir(directory_name)
        result = list()
        for file in files:
            file = directory_name + '/' + file
            if file.endswith('.py'):
                result.append(file)
            elif os.path.isdir(file):
                support_var = self._work_with_directory(file)
                for _ in support_var:
                    if len(_) != 0:
                        result.append(_)
        return result
