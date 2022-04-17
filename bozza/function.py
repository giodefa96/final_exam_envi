from pathlib import Path
import sys


class SearchingModelPath:


    def __init__(self, searching_model_path=None):
        self.searching_model_path = searching_model_path

    def searching_model_path(name: str):

        """Insert the name string of the model so i can reach for you"""
        try:
            path_home = Path.home()
            path_directory = path_home / 'Desktop/Unimib/Data Science/Second Year/Physics and environmental data lab/Environmental/Materiale Corso/Model Folder'
            path_model = path_directory / name
            if not path_model.exists():
                sys.exit()
            return path_model
        except SystemExit:
            print('Insert string and valid model name')


def searching_model_path(name: str):

    """Insert the name string of the model so i can reach for you"""
    try:
        path_home = Path.home()
        path_directory = path_home / 'Desktop/Unimib/Data Science/Second Year/Physics and environmental data lab/Environmental/Materiale Corso/Final_ex/Model Folder'
        path_model = path_directory / name
        if not path_model.exists():
            sys.exit()
        return path_model
    except SystemExit:
        print('Insert string and valid model name')