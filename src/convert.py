# https://zenodo.org/record/7781388

import os
import xml.etree.ElementTree as ET

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)

# https://zenodo.org/record/7781388


# project_name = "Aerial Power Infrastructure"
dataset_paths = ["./APP_DATA/Aerial/Train", "./APP_DATA/Aerial/Test", "./APP_DATA/Aerial/Valid"]
anns_paths = [
    "./APP_DATA/Aerial/Annotations/VOC/Train",
    "./APP_DATA/Aerial/Annotations/VOC/Test",
    "./APP_DATA/Aerial/Annotations/VOC/Valid",
]
batch_size = 10
ds_names = ["Train", "Test", "Valid"]
images_ext = ".jpg"
ann_ext = ".xml"


def create_ann(image_path, anns_path):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    file_name = get_file_name(image_path)

    ann_path = os.path.join(anns_path, file_name + ann_ext)

    if file_exists(ann_path):
        tree = ET.parse(ann_path)
        root = tree.getroot()

        coords_xml = root.findall(".//bndbox")
        for curr_coord in coords_xml:
            left = int(curr_coord[0].text)
            top = int(curr_coord[1].text)
            right = int(curr_coord[2].text)
            bottom = int(curr_coord[3].text)

            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            label = sly.Label(rect, obj_class)
            labels.append(label)

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


obj_class = sly.ObjClass("tbar", sly.Rectangle)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "Aerial Power Infrastructure"
    dataset_path = "APP_DATA/Aerial"
    anns_path = "APP_DATA/Aerial/Annotations/Yolo"
    batch_size = 10
    images_ext = ".jpg"
    ann_ext = ".txt"

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        file_name = get_file_name(image_path)

        ann_path = os.path.join(curr_anns_path, file_name + ann_ext)

        if file_exists(ann_path):
            with open(ann_path) as f:
                content = f.read().split("\n")

                for curr_data in content:
                    if len(curr_data) != 0:
                        curr_data = list(map(float, curr_data.split(" ")))

                        left = int((curr_data[1] - curr_data[3] / 2) * img_wight)
                        right = int((curr_data[1] + curr_data[3] / 2) * img_wight)
                        top = int((curr_data[2] - curr_data[4] / 2) * img_height)
                        bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
                        rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                        label = sly.Label(rectangle, obj_class)
                        labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class = sly.ObjClass("t-bar", sly.Rectangle)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class])
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in os.listdir(dataset_path):
        if ds_name == "Annotations":
            continue
        ds_name = ds_name.lower()

        curr_ds_path = os.path.join(dataset_path, ds_name)
        if dir_exists(curr_ds_path):
            curr_anns_path = os.path.join(anns_path, ds_name)
            dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

            images_names = os.listdir(curr_ds_path)

            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

            for images_names_batch in sly.batched(images_names, batch_size=batch_size):
                img_pathes_batch = [
                    os.path.join(curr_ds_path, image_name) for image_name in images_names_batch
                ]

                img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                anns = [create_ann(image_path) for image_path in img_pathes_batch]
                api.annotation.upload_anns(img_ids, anns)

                progress.iters_done_report(len(images_names_batch))
    return project
