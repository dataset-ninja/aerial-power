from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Aerial Power Infrastructure"
PROJECT_NAME_FULL: str = "Aerial Power Infrastructure Detection Dataset"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
INDUSTRIES: List[Industry] = [Industry.Energy()]
CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_YEAR: int = 2023
HOMEPAGE_URL: str = "https://zenodo.org/record/7781388"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = None
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/aerial-power"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Annotations": "https://zenodo.org/record/7781388/files/Annotations.zip?download=1",
    "Labels": "https://zenodo.org/record/7781388/files/labels.txt?download=1",
    "Test": "https://zenodo.org/record/7781388/files/Test.zip?download=1",
    "Train": "https://zenodo.org/record/7781388/files/Train.zip?download=1",
    "Valid": "https://zenodo.org/record/7781388/files/Valid.zip?download=1",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://ieeexplore.ieee.org/document/9476742/"
CITATION_URL: Optional[str] = "https://zenodo.org/record/7781388"
ORGANIZATION_NAME: Optional[
    Union[str, List[str]]
] = "KIOS Research and Innovation Center of Excellence, University of Cyprus"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.kios.ucy.ac.cy/"
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "industries": INDUSTRIES,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    return settings
